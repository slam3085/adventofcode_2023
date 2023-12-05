def parse_input(lines):
	objects = []
	i = 0
	while i < len(lines):
		object = []
		cur = lines[i]
		if "seeds" in cur:
			object = (cur.split(': ')[0], [int(i) for i in cur.split(': ')[1].split(" ")])
			i += 1
		elif "map" in cur:
			object.append(cur)
			i += 1
			cur = lines[i]
			while i < len(lines) and cur != '':
				cur = lines[i]
				if cur != '':
					object.append([int(i) for i in cur.split(" ")])
				i += 1
		else:
			i += 1
		if object:
			objects.append(object)
	return objects


def apply_map(current, _map):
	res = []
	for c in current:
		transformed = None
		for dest_range_start, source_range_start, range_length in _map:
			if source_range_start <= c < source_range_start + range_length:
				transformed = dest_range_start + (c - source_range_start)
				break
		if transformed is None:
			transformed = c
		res.append(transformed)
	return res


def find_intersection(c_start, c_range_length, source_range_start, range_length):
	c_end = c_start + c_range_length - 1
	source_range_end = source_range_start + range_length - 1
	intersection_start = max(c_start, source_range_start)
	intersection_end = min(c_end, source_range_end)
	if intersection_start <= intersection_end:
		intersection_range_length = intersection_end - intersection_start + 1
		return (intersection_start, intersection_range_length)
	else:
		return None


def apply_map_2(current, _map):
	res = []
	for c_start, c_range_length in current:
		transformed = []
		_map.sort(key=lambda x: x[1])

		for dest_range_start, source_range_start, range_length in _map:
			intersection = find_intersection(c_start, c_range_length, source_range_start, range_length)
			if intersection:
				intersection_start, intersection_range_length = intersection
				if intersection_start != c_start:
					transformed_start = c_start
					transformed_range_length = intersection_start - c_start
					if transformed_range_length > 0:
						transformed.append((transformed_start, transformed_range_length))
						c_start += transformed_range_length
						c_range_length -= transformed_range_length
				transformed_start = dest_range_start + c_start - source_range_start
				transformed_range_length = intersection_range_length
				transformed.append((transformed_start, transformed_range_length))
				c_start += intersection_range_length
				c_range_length -= intersection_range_length
		if c_range_length > 0:
			transformed.append((c_start, c_range_length))
		res += transformed
	return res


def p1(filename):
	objects = []
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	objects = parse_input(lines)
	current = objects.pop(0)[1]
	while objects:
		_map = objects.pop(0)[1:]
		current = apply_map(current, _map)
	return min(current)


def p2(filename):
	objects = []
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	objects = parse_input(lines)
	current_raw = objects.pop(0)[1]
	current = [(current_raw[i], current_raw[i + 1]) for i in range(0, len(current_raw), 2)]
	while objects:
		_map = objects.pop(0)[1:]
		current = apply_map_2(current, _map)
	return min((i[0] for i in current))


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
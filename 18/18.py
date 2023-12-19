def get_neighbours(i, j):
	return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]


def p1(filename):
	lines = []
	exterior = set()
	interior_seeds = set()
	i, j = 0, 0
	with open(filename) as f:
		for line in f:
			lines.append(line.strip().split(' '))
	# dig path
	for direction, steps, color in lines:
		steps = int(steps)
		if direction == 'R':
			for k in range(1, steps + 1):
				exterior.add((i, j + k))
				interior_seeds.add((i + 1, j + k))
			j += steps
		elif direction == 'L':
			for k in range(1, steps + 1):
				exterior.add((i, j - k))
				interior_seeds.add((i - 1, j - k))
			j -= steps
		elif direction == 'U':
			for k in range(1, steps + 1):
				exterior.add((i - k, j))
				interior_seeds.add((i - k, j + 1))
			i -= steps
		elif direction == 'D':
			for k in range(1, steps + 1):
				exterior.add((i + k, j))
				interior_seeds.add((i + k, j - 1))
			i += steps
	interior_seeds -= exterior
	# dig interior
	interior = set()
	queue = interior_seeds.copy()
	while queue:
		i, j = queue.pop()
		for n_i, n_j in get_neighbours(i, j):
			if (n_i, n_j) not in exterior and (n_i, n_j) not in interior:
				interior.add((n_i, n_j))
				queue.add((n_i, n_j))
	return len(interior | exterior)


def get_direction(direction_code):
	mapping = {
		0: 'R',
		1: 'D',
		2: 'L',
		3: 'U'
	}
	return mapping[direction_code]


def p2(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip().split(' '))
	i, j = 0, 0
	coords = [(i, j)]
	perimeter = 0
	for _, _, item in lines:
		hex_code = item.replace('(', '').replace(')', '').replace('#', '')
		distance = int(hex_code[:5], 16)
		direction = get_direction(int(hex_code[-1]))
		if direction == 'R':
			j += distance
		elif direction == 'L':
			j -= distance
		elif direction == 'D':
			i += distance
		elif direction == 'U':
			i -= distance
		perimeter += distance
		coords.append((i, j))
	cumsum1 = 0
	cumsum2 = 0
	for i in range(len(coords) - 1):
		cumsum1 += (coords[i][0] * coords[i + 1][1])
		cumsum2 += (coords[i + 1][0] * coords[i][1])
	area = int(abs(cumsum1 - cumsum2) / 2 + perimeter / 2 + 1)
	return area


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
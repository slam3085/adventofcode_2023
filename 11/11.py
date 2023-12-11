def rows_to_expand(lines):
	rows = []
	for i, line in enumerate(lines):
		is_empty = True
		for char in line:
			if char != '.':
				is_empty = False
				break
		if is_empty:
			rows.append(i)
	return rows


def cols_to_expand(lines):
	transposed = list(map(list, zip(*lines)))
	cols = rows_to_expand(transposed)
	return cols


def solve(filename, rate):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	galaxies = []
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if char == '#':
				galaxies.append([i, j])
	rows = rows_to_expand(lines)
	cols = cols_to_expand(lines)
	# expand
	for g in galaxies:
		diff = 0
		for r in rows:
			if g[0] > r:
				diff += rate - 1
		g[0] += diff
	for g in galaxies:
		diff = 0
		for c in cols:
			if g[1] > c:
				diff += rate - 1
		g[1] += diff
	# find distance for all pairs
	total_distance = 0
	for g1 in galaxies:
		for g2 in galaxies:
			if not (g1[0] == g2[0] and g1[1] == g2[1]):
				distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
				total_distance += distance
	return int(total_distance / 2)


if __name__ == '__main__':
	print(f"p1: {solve('input.txt', 2)}")
	print(f"p2: {solve('input.txt', 1000000)}")
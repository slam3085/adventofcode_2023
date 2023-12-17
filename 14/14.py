def fix_field(field):
	res = []
	n_rows = len(field)
	n_cols = len(field[0])
	res.append(['#'] * (n_cols + 2))
	for line in field:
		res.append(['#'] + line + ['#'])
	res.append(['#'] * (n_cols + 2))
	return res


def rotate_clockwise(matrix):
    transposed = [list(row) for row in zip(*matrix)]
    return [row[::-1] for row in transposed]


def rotate_counterclockwise(matrix):
    transposed = [list(row) for row in zip(*matrix)]
    return transposed[::-1]


def tilt_west(field):
	tilted = []
	for line in field:
		res = []
		i = 0
		while i < len(line):
			if line[i] == '#':
				res.append('#')
				i += 1
			else:
				n_rocks = 0
				n_empty = 0
				while i < len(line) and line[i] != '#':
					if line[i] == '.':
						n_empty += 1
					elif line[i] == 'O':
						n_rocks += 1
					i += 1
				res += ['O'] * n_rocks + ['.'] * n_empty
		tilted.append(res)
	return tilted


def tilt_north(field):
	f = rotate_counterclockwise(field)
	tilted = tilt_west(f)
	return rotate_clockwise(tilted)


def tilt_south(field):
	f = rotate_clockwise(field)
	tilted = tilt_west(f)
	return rotate_counterclockwise(tilted)


def tilt_east(field):
	f = rotate_clockwise(rotate_clockwise(field))
	tilted = tilt_west(f)
	return rotate_counterclockwise(rotate_counterclockwise(tilted))


def spin_cycle(field):
	return tilt_east(tilt_south(tilt_west(tilt_north(field))))


def evaluate_load(field):
	load = 0
	n_rows = len(field) - 2
	for i in range(1, len(field) - 1):
		n_stones = 0
		for j in range(1, len(field[0]) - 1):
			if field[i][j] == 'O':
				n_stones += 1
		load += n_stones * (n_rows - i + 1)
	return load


def print_field(f):
	for line in f:
		print(''.join(line))


def to_string(field):
	return '\n'.join((''.join(line) for line in field))


def to_field(string_field):
	return [ch for ch in string_field.split('\n')]


def p1(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(list(line.strip()))
	field = fix_field(lines)
	tilted = tilt_north(field)
	load = evaluate_load(tilted)
	return load


def p2(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(list(line.strip()))
	field = fix_field(lines)
	# loop to identify all states
	states = []
	states.append(to_string(field))
	for i in range(1000):
		field = spin_cycle(field)
		field_string = to_string(field)
		if field_string == states[0]:
			break
		else:
			states.append(field_string)
	# solution
	n_cycles = 1000000000
	n_states = len(states)
	return evaluate_load(to_field(states[n_cycles % n_states]))


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
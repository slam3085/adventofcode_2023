from collections import namedtuple

Beam = namedtuple("Beam", "i j direction")

right = 0
down = 1
left = 2
up = 3


def check_bounds(i, j, field):
	max_i = len(field)
	max_j = len(field[0])
	return (0 <= i < max_i) and (0 <= j < max_j)


def iterate(beam, field, traverse=True):
	next_i, next_j, direction = beam.i, beam.j, beam.direction
	if traverse:
		if direction == right:
			next_j += 1
		elif direction == down:
			next_i += 1
		elif direction == left:
			next_j -= 1
		elif direction == up:
			next_i -= 1
	# out of field
	if not check_bounds(next_i, next_j, field):
		return []
	# continue
	if field[next_i][next_j] == '.':
		return [Beam(next_i, next_j, direction)]
	# mirrors
	# /
	if field[next_i][next_j] == '/':
		if direction == left:
			direction = down
		elif direction == right:
			direction = up
		elif direction == down:
			direction = left
		elif direction == up:
			direction = right
		return [Beam(next_i, next_j, direction)]
	# \
	if field[next_i][next_j] == '\\':
		if direction == left:
			direction = up
		elif direction == right:
			direction = down
		elif direction == down:
			direction = right
		elif direction == up:
			direction = left
		return [Beam(next_i, next_j, direction)]
	# splitters
	if field[next_i][next_j] == '-':
		if direction in (left, right):
			return [Beam(next_i, next_j, direction)]
		elif direction in (up, down):
			return [Beam(next_i, next_j, left), Beam(next_i, next_j, right)]
	if field[next_i][next_j] == '|':
		if direction in (up, down):
			return [Beam(next_i, next_j, direction)]
		elif direction in (left, right):
			return [Beam(next_i, next_j, up), Beam(next_i, next_j, down)]
	return []


def create_start_beams(i, j, field):
	max_i = len(field)
	max_j = len(field[0])
	if i == 0 and j == 0:
		return [Beam(0, 0, right), Beam(0, 0, down)]
	if i == 0 and j == max_j - 1:
		return [Beam(0, 0, left), Beam(0, 0, down)]
	if i == max_i - 1 and j == 0:
		return [Beam(0, 0, up), Beam(0, 0, right)]
	if i == max_i - 1 and j == max_j - 1:
		return [Beam(0, 0, up), Beam(0, 0, left)]
	if i == 0:
		return [Beam(i, j, down)]
	if i == max_i - 1:
		return [Beam(i, j, up)]
	if j == 0:
		return [Beam(i, j, right)]
	if j == max_j - 1:
		return [Beam(i, j, left)]



def solve(beams, field):
	energized = [['.' for j in range(len(field[0]))] for i in range(len(field))]
	all_previous_beams = set()
	while beams:
		new_beams = []
		# fill field and memorize beams
		for b in beams:
			energized[b.i][b.j] = '#'
			all_previous_beams.add(b)
			for new_beam in iterate(b, field):
				if new_beam not in all_previous_beams:
					new_beams.append(new_beam)
		beams = new_beams
	ans = 0
	for line in energized:
		ans += sum((1 for ch in line if ch == '#'))
	return ans

def p1(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	beams = iterate(Beam(0, 0, right), lines, traverse=False)
	return solve(beams, lines)


def p2(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	# generate all start points
	start_indices = set()
	max_i = len(lines)
	max_j = len(lines[0])
	for i in range(max_i):
		start_indices.add((i, 0))
		start_indices.add((i, max_j - 1))
	for j in range(max_j):
		start_indices.add((0, j))
		start_indices.add((max_i - 1, j))
	# create start beams
	start_beams = []
	for i, j in start_indices:
		start_beams += create_start_beams(i, j, lines)
	# solve
	max_ans = 0
	for start_beam in start_beams:
		beams = iterate(start_beam, lines, traverse=False)
		ans = solve(beams, lines)
		if ans > max_ans:
			max_ans = ans
	return max_ans


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
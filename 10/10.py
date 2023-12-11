from collections import defaultdict


def is_valid_step(_cur, _next, _dir):
	if _dir == 'up':
		if _cur in ('S', '|', 'L', 'J') and _next in ('|', '7', 'F', 'S'):
			return True

	elif _dir == 'down':
		if _cur in ('S', '|', '7', 'F') and _next in ('|', 'L', 'J', 'S'):
			return True
	
	elif _dir == 'left':
		if _cur in ('S', '-', '7', 'J') and _next in ('-', 'L', 'F', 'S'):
			return True
	
	elif _dir == 'right':
		if _cur in ('S', '-', 'F', 'L') and _next in ('-', 'J', '7', 'S'):
			return True
	
	return False


def get_available_steps(lines, c_i, c_j, visited):
	all_steps = [
		(c_i - 1, c_j,     'up'   ),
		(c_i + 1, c_j,     'down' ),
		(c_i,     c_j - 1, 'left' ),
		(c_i,     c_j + 1, 'right')
	]
	# check bounds
	all_steps = [step for step in all_steps if 0 <= step[0] < len(lines)]
	all_steps = [step for step in all_steps if 0 <= step[1] < len(lines[0])]
	#check if valid step
	all_steps = [step for step in all_steps if is_valid_step(lines[c_i][c_j], lines[step[0]][step[1]], step[2])]
	# check if not visited
	all_steps = [step for step in all_steps if (step[0], step[1]) not in visited]
	return all_steps
	
	 

def find_start(lines):
	for i in range(len(lines)):
		for j in range(len(lines[0])):
			if lines[i][j] == 'S':
				return i, j


def solve(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	# p1
	s_i, s_j = find_start(lines)
	c_i, c_j = s_i, s_j
	visited = set((c_i, c_j))
	neighbours = defaultdict(set)
	path_length = 1
	while True:
		available_steps = get_available_steps(lines, c_i, c_j, visited)
		if not available_steps:
			break
		
		for item in available_steps:
			neighbours[(c_i, c_j)].add((item[0], item[1]))
		neighbours[(available_steps[0][0], available_steps[0][1])].add((c_i, c_j))

		c_i, c_j, _ = available_steps[0]
		visited.add((c_i, c_j))
		path_length += 1
	print(f"p1: {path_length // 2}")
	# p2
	# fix neighbours
	for k, v in neighbours.items():
		if len(v) != 2:
			lost = k
	for k, v in neighbours.items():
		if lost in v:
			neighbours[lost].add(k)
	# solution
	area = 0
	for i, line in enumerate(lines):
		line = line.replace('S', 'L') # lazy hack
		pipes_crossed = 0
		j = 0
		while j < len(line):
			if (i, j) in visited:
				if line[j] == '|':
					pipes_crossed += 1
				elif line[j] == 'L':
					while (i, j + 1) in neighbours and (i, j + 1) in neighbours[(i, j)]:
						j += 1
					if line[j] == '7':
						pipes_crossed += 1
				elif line[j] == 'F':
					while (i, j + 1) in neighbours and (i, j + 1) in neighbours[(i, j)]:
						j += 1
					if line[j] == 'J':
						pipes_crossed += 1
			else:
				if pipes_crossed % 2 == 1:
					area += 1
			j += 1
	print(f"p2: {area}")


if __name__ == '__main__':
	solve('input.txt')
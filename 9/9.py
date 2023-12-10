def is_zero(line):
	for i in line:
		if i != 0:
			return False
	return True


def diffs(line):
	return [line[i] - line[i - 1] for i in range(1, len(line))]


def forward(line):
	res = [line]
	while not is_zero(res[-1]):
		res.append(diffs(res[-1]))
	return res


def backward(line):
	res = list(reversed(forward(line)))
	res[0].append(0)
	for i in range(1, len(res)):
		res[i].append(res[i][-1] + res[i - 1][-1])
	return list(reversed(res))


def backward_2(line):
	res = list(reversed(forward(line)))
	res[0].append(0)
	for i in range(1, len(res)):
		res[i].insert(0, res[i][0] - res[i - 1][0])
	return list(reversed(res))


def p1(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append([int(i) for i in line.split(" ")])
	ans = 0
	for line in lines:
		ans += backward(line)[0][-1]
	return ans


def p2(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append([int(i) for i in line.split(" ")])
	ans = 0
	for line in lines:
		ans += backward_2(line)[0][0]
	return ans


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
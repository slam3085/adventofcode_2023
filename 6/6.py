def get_number_of_ways_to_win(t, d):
	res = 0
	for speed in range(1, t):
		my_distance = speed * (t - speed)
		if my_distance > d:
			res += 1
	return res


def p1(filename):
	times = []
	distances = []
	ans = 1
	with open(filename) as f:
		for line in f:
			if "Time" in line:
				times = [int(i) for i in line.replace("Time:", '').strip().split(' ') if i != '']
			elif "Distance" in line:
				distances = [int(i) for i in line.replace("Distance:", '').strip().split(' ') if i != ' ' and i != '']
	for t, d in zip(times, distances):
		ans *= get_number_of_ways_to_win(t, d)
	return ans


def p2(filename):
	time = None
	distance = None
	with open(filename) as f:
		for line in f:
			if "Time" in line:
				time = int(line.replace("Time:", '').replace(' ', '').strip())
			elif "Distance" in line:
				distance = int(line.replace("Distance:", '').replace(' ', '').strip())
	return get_number_of_ways_to_win(time, distance)


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
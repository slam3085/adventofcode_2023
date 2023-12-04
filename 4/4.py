def parse_line(line):
	card_n = int(line.split(': ')[0].replace('Card ', ''))
	winning_numbers = [int(i) for i in line.split(': ')[1].split(' | ')[0].split(' ') if i != '']
	my_numbers = [int(i) for i in line.split(': ')[1].split(' | ')[1].split(' ')  if i != '']
	return card_n, winning_numbers, my_numbers


def increment_points(points):
	if points == 0:
		points += 1
	else:
		points *= 2
	return points


def p1(filename):
	total_points = 0
	with open(filename) as f:
		for line in f:
			points = 0
			card_n, winning_numbers, my_numbers = parse_line(line)
			winning_numbers = set(winning_numbers)
			for n in my_numbers:
				if n in winning_numbers:
					points = increment_points(points)
			total_points += points
	return total_points


def p2(filename):
	with open(filename) as f:
		cards = []
		multipliers = {}
		for line in f:
			card_n, winning_numbers, my_numbers = parse_line(line)
			cards.append((card_n, winning_numbers, my_numbers))
			multipliers[card_n] = 1
		for card_n, winning_numbers, my_numbers in cards:
			winning_numbers = set(winning_numbers)
			n_copies = 0
			for n in my_numbers:
				if n in winning_numbers:
					n_copies += 1
			for i in range(0, n_copies):
				multipliers[card_n + 1 + i] += (multipliers[card_n])
		return sum((i for i in multipliers.values()))


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
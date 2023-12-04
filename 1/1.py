mapping = {
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9",
}

reversed_mapping = {
	''.join(reversed(k)): v for k, v in mapping.items()
}

for i in range(1, 10):
	mapping[str(i)] = str(i)
	reversed_mapping[str(i)] = str(i)


def first_digit(s):
	for item in s:
		if item.isdigit():
			return item


def real_first_digit(s):
	min_index = 1e9
	value = None

	for d in mapping.keys():
		index = s.find(d)
		if index != -1 and index < min_index:
			min_index = index
			value = d
	return mapping[value]


def last_digit(s):
	for item in reversed(s):
		if item.isdigit():
			return item


def real_last_digit(s):
	min_index = 1e9
	value = None
	s = ''.join(reversed(s))

	for d in reversed_mapping.keys():
		index = s.find(d)
		if index != -1 and index < min_index:
			min_index = index
			value = d
	return reversed_mapping[value]


def get_calibration_value(s):
	return int(first_digit(s) + last_digit(s))


def get_real_calibration_value(s):
	return int(real_first_digit(s) + real_last_digit(s))


def p1(filename):
	total = 0
	with open(filename) as f:
		for line in f:
			total += get_calibration_value(line)
	return total


def p2(filename):
	total = 0
	with open(filename) as f:
		for line in f:
			total += get_real_calibration_value(line)
	return total


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
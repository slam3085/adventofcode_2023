from collections import defaultdict


def my_hash(string):
	res = 0
	for ch in string:
		res += ord(ch)
		res *= 17
		res %= 256
	return res


def p1(filename):
	ans = 0
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	for line in lines:
		for item in line.split(','):
			ans += my_hash(item)
	return ans


def p2(filename):
	boxes = defaultdict(list)
	focal_lengths = {}
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	for line in lines:
		for item in line.split(','):
			# assign
			if '=' in item:
				label, focal_length = item.split('=')
				box_index = my_hash(label)
				focal_length = int(focal_length)
				# already exists
				if label in boxes[box_index]:
					focal_lengths[label] = focal_length
				# new
				else:
					boxes[box_index].append(label)
					focal_lengths[label] = focal_length
			# remove
			elif '-' in item:
				label = item.replace('-', '')
				box_index = my_hash(label)
				# remove if exists
				if label in boxes[box_index]:
					boxes[box_index] = [item for item in boxes[box_index] if item != label]
					focal_lengths.pop(label)
	# evaluate focusing power
	focusing_power = 0
	for label, focal_length in focal_lengths.items():
		box_index = my_hash(label)
		current = box_index + 1
		current *= (boxes[box_index].index(label) + 1)
		current *= focal_length
		focusing_power += current
	return focusing_power


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
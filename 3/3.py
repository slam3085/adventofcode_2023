def get_numbers_coords(field):
	numbers_coords = [] # (number, row_n, col_start, col_end)
	for i, row in enumerate(field):
		j = 0
		while j < len(row):
			if row[j].isdigit():
				number = row[j]
				row_n = i
				col_start = j
				col_end = j
				j += 1
				while j < len(row) and row[j].isdigit():
					number += row[j]
					col_end = j
					j += 1
				numbers_coords.append((int(number), row_n, col_start, col_end))
			else:
				j += 1
	return numbers_coords


def get_star_coords(field):
	star_coords = []
	for i, row in enumerate(field):
		for j, v in enumerate(row):
			if v == '*':
				star_coords.append((i, j))
	return star_coords


def p1(filename):
	field = []
	with open(filename) as f:
		for line in f:
			field.append(line.replace('\n', ''))
	numbers_coords = get_numbers_coords(field)
	part_sum = 0
	for number, row_n, col_start, col_end in numbers_coords:
		is_adjacent = False
		for i in range(row_n - 1, row_n + 2):
			for j in range(col_start - 1, col_end + 2):
				if 0 <= i < len(field) and 0 <= j < len(field[0]):
					if not (field[i][j].isdigit() or field[i][j] == '.'):
						is_adjacent = is_adjacent or True
		if is_adjacent:
			part_sum += number
	return part_sum


def p2(filename):
	gear_ratio_sum = 0
	field = []
	with open(filename) as f:
		for line in f:
			field.append(line.replace('\n', ''))
	numbers_coords = get_numbers_coords(field)
	star_coords = get_star_coords(field)
	for star_i, star_j in star_coords:
		adjacent_count = 0
		adjacent_numbers = []
		for number, row_n, col_start, col_end in numbers_coords:
			number_is_right = (star_i == row_n) and ((star_j + 1) == col_start)
			number_is_left = (star_i == row_n) and ((star_j - 1) == col_end)
			number_is_up = (star_i - 1 == row_n) and ((col_start - 1) <= star_j <= (col_end + 1))
			number_is_down = (star_i + 1 == row_n) and ((col_start - 1) <= star_j <= (col_end + 1))
			if number_is_right or number_is_left or number_is_up or number_is_down:
				adjacent_count += 1
				adjacent_numbers.append(number)
		if adjacent_count == 2:
			gear_ratio_sum += adjacent_numbers[0] * adjacent_numbers[1]
	return gear_ratio_sum


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
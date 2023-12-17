def find_rows(lines):
	rows = set()
	for i, _ in enumerate(lines):
		is_reflection = True
		left = list(reversed(lines[:i]))
		right = lines[i:]
		for l, r in zip(left, right):
			if l != r:
				is_reflection = False
		if is_reflection and len(left) > 0:
			rows.add(len(left))
	return rows


def find_cols(lines):
	rotated = [''.join(item) for item in zip(*lines[::-1])]
	return find_rows(rotated)


def invert_pixel(img, i, j):
	img = [list(line) for line in img]
	symbol = img[i][j]
	new_symbol = '.'
	if symbol == '.':
		new_symbol = '#'
	img[i][j] = new_symbol
	return [''.join(line) for line in img]


def generate_inverted(img):
	res = []
	max_i = len(img)
	max_j = len(img[0])
	for i in range(max_i):
		for j in range(max_j):
			res.append(invert_pixel(img, i, j))
	return res


def solve(filename):
	# input
	images = []
	lines = []
	with open(filename) as f:
		for line in f:
			l = line.strip()
			if l != '':
				lines.append(l)
			else:
				images.append(lines)
				lines = []
	images.append(lines)
	# p1
	reflection_lines = {}
	total_rows = 0
	total_cols = 0
	for k, img in enumerate(images):
		rows = find_rows(img)
		cols = find_cols(img)
		if rows:
			total_rows += list(rows)[0]
		if cols:
			total_cols += list(cols)[0]
		reflection_lines[k] = (rows, cols)
	print(f"p1: {total_cols + 100 * total_rows}")
	# p2
	total_rows = 0
	total_cols = 0
	for k, img in enumerate(images):
		for fixed_image in generate_inverted(img):
			new_rows = find_rows(fixed_image) - reflection_lines[k][0]
			if new_rows:
				total_rows += new_rows.pop()
				break
			new_cols = find_cols(fixed_image) - reflection_lines[k][1]
			if new_cols:
				total_cols += new_cols.pop()
				break
	print(f"p2: {total_cols + 100 * total_rows}")


if __name__ == '__main__':
	solve('input.txt')
def parse_line(s):
	game_id = int(s.split(': ')[0].replace('Game ', ''))
	games = []
	for game in s.split(': ')[1].split(';'):
		balls = game.split(', ')
		for b in balls:
			game = {}
			if 'red' in b:
				game['red'] = int(b.replace(' red', ''))
			elif 'green' in b:
				game['green'] = int(b.replace(' green', ''))
			elif 'blue' in b:
				game['blue'] = int(b.replace(' blue', ''))
			games.append(game)
	return (game_id, games)


def p1(filename):
	max_red = 12
	max_green = 13
	max_blue = 14
	ids_sum = 0
	with open(filename) as f:
		for line in f:
			game_id, games = parse_line(line)
			is_possible = True
			for g in games:
				red = g.get('red', 0)
				green = g.get('green', 0)
				blue = g.get('blue', 0)
				if red > max_red or green > max_green or blue > max_blue:
					is_possible = False
					break
			if is_possible:
				ids_sum += game_id
	return ids_sum

def p2(filename):
	sum_power = 0
	with open(filename) as f:
		for line in f:
			_, games = parse_line(line)
			red = 0
			green = 0
			blue = 0
			for g in games:
				red = max(red, g.get('red', 0))
				green = max(green, g.get('green', 0))
				blue = max(blue, g.get('blue', 0))
			sum_power += red * green * blue
	return sum_power



if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
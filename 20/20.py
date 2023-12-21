import math


major_conjunctions = {'zc': 1e9, 'xt': 1e9, 'mk': 1e9, 'fp': 1e9}


def parse_input(filename):
	types = {'output': 'output', 'rx': 'rx'}
	links = {}
	flip_flops = {}
	conjunctions = {}
	with open(filename) as f:
		for line in f:
			_in, _out = line.strip().split(' -> ')
			if _in == 'broadcaster':
				_type = 'broadcaster'
			elif _in[0] == '%':
				_type = 'flip-flop'
				_in = _in[1:]
			elif _in[0] == '&':
				_type = 'conjunction'
				_in = _in[1:]
			_out = _out.split(', ')
			types[_in] = _type
			links[_in] = _out
	for k, v in types.items():
		if v == 'flip-flop':
			flip_flops[k] = False
		elif v == 'conjunction':
			conjunctions[k] = {}
	for k, values in links.items():
		for v in values:
			if types[v] == 'conjunction':
				conjunctions[v][k] = False
	return types, links, flip_flops, conjunctions


def push_button(types, links, flip_flops, conjunctions, i):
	n_low, n_high = 1, 0
	signal_queue = [('broadcaster', False)]
	while signal_queue:
		sender, signal = signal_queue.pop(0)
		if sender in major_conjunctions and signal:
			major_conjunctions[sender] = min(major_conjunctions[sender], i)
		receivers = links[sender]
		if signal == True:
			n_high += len(receivers)
		elif signal == False:
			n_low += len(receivers)
		for r in receivers:
			if types[r] == 'flip-flop':
				if signal == False:
					flip_flops[r] = not flip_flops[r]
					if flip_flops[r]:
						signal_queue.append((r, True))
					else:
						signal_queue.append((r, False))
			elif types[r] == 'conjunction':
				conjunctions[r][sender] = signal
				all_high = True
				for k, v in conjunctions[r].items():
					all_high &= v
				if all_high:
					signal_queue.append((r, False))
				else:
					signal_queue.append((r, True))
	return n_low, n_high


def p1(filename):
	types, links, flip_flops, conjunctions = parse_input(filename)
	n_low_total, n_high_total = 0, 0
	for i in range(1000):
		n_low, n_high = push_button(types, links, flip_flops, conjunctions, i)
		n_low_total += n_low
		n_high_total += n_high
	return n_low_total * n_high_total


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def p2(filename):
	types, links, flip_flops, conjunctions = parse_input(filename)
	for i in range(1, int(1e4)):
		push_button(types, links, flip_flops, conjunctions, i)
		periods_found = True
		for k, v in major_conjunctions.items():
			periods_found = periods_found and v < 1e5
		if periods_found:
			break
	ans = 1
	for k, v in major_conjunctions.items():
		ans = lcm(ans, v)
	return ans


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
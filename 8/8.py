import itertools
from math import gcd


class Node:
	value = None
	left = None
	right = None
	
	def __str__(self):
		return f"{self.value} = ({self.left}, {self.right})"


def read_instructions_nodes(filename):
	with open(filename) as f:
		nodes = {}
		for i, line in enumerate(f):
			line = line.strip()
			if i == 0:
				instructions = line
			elif i > 1:
				node = Node()
				node.value = line.split(' = ')[0]
				node.left = line.split(' = ')[1].split(', ')[0].replace('(', '')
				node.right = line.split(' = ')[1].split(', ')[1].replace(')', '')
				nodes[node.value] = node
	return instructions, nodes


def p1(filename):
	instructions, nodes = read_instructions_nodes(filename)
	current = nodes['AAA']
	end = nodes['ZZZ']
	steps = 0
	for dir in itertools.cycle(instructions):
		if current.value == end.value:
			break
		steps += 1
		if dir == 'L':
			current = nodes[current.left]
		elif dir == 'R':
			current = nodes[current.right]
	return steps


def p2(filename):
	instructions, nodes = read_instructions_nodes(filename)
	current = [nodes[n] for n in nodes if nodes[n].value.endswith('A')]
	z_reached = {i: None for i in range(len(current))}
	steps = 0
	for dir in itertools.cycle(instructions):
		# check
		for i, c in enumerate(current):
			if c.value.endswith('Z') and z_reached[i] == None:
				z_reached[i] = steps
		# iterate
		steps += 1
		if dir == 'L':
			current = [nodes[c.left] for c in current]
		if dir == 'R':
			current = [nodes[c.right] for c in current]
		# check if all periods available
			n_periods = 0
			for v in z_reached.values():
				if v != None:
					n_periods += 1
			if n_periods == len(current):
				break
	# find LCM of periods
	res = 1
	for i in range(len(current)):
		res = int(res * z_reached[i] / gcd(res, z_reached[i]))
	return res


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
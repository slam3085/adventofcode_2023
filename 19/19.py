def parse_rule(description):
	category = description[0]
	op = description[1]
	value = int(description.split(':')[0][2:])
	workflow = description.split(':')[1]
	return (category, op, value, workflow)


def parse_workflow(line):
	name, rules = line.split('{')[0], line.split('{')[1].replace('}', '')
	rules = rules.split(',')
	for i in range(len(rules) - 1):
		rules[i] = parse_rule(rules[i])
	return name, rules


def parse_part(description):
	part = {}
	for item in description.replace('{', '').replace('}', '').split(','):
		if 'x=' in item:
			part['x'] = int(item.replace('x=', ''))
		elif 'm=' in item:
			part['m'] = int(item.replace('m=', ''))
		elif 'a=' in item:
			part['a'] = int(item.replace('a=', ''))
		elif 's=' in item:
			part['s'] = int(item.replace('s=', ''))
	return part


def evaluate_workflow(workflow, part):
	for category, op, value, out in workflow[:-1]:
		if (op == '>' and part[category] > value) or (op == '<' and part[category] < value):
			return out
	return workflow[-1]


def evaluate(part, workflows):
	start_wf = 'in'
	res = evaluate_workflow(workflows[start_wf], part)
	while res not in ('A', 'R'):
		res = evaluate_workflow(workflows[res], part)
	if res == 'A':
		return True
	elif res == 'R':
		return False


def p1(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	workflows = {}
	ratings = []
	is_workflow = True
	for line in lines:
		if line == '':
			is_workflow = False
			continue
		if is_workflow:
			workflow_name, workflow = parse_workflow(line)
			workflows[workflow_name] = workflow
		else:
			ratings.append(parse_part(line))
	ans = 0
	for r in ratings:
		if evaluate(r, workflows):
			ans += sum(r.values())
	return ans


def partition_hypercube(hypercube, category, op, value):
	hyp1, hyp2 = hypercube.copy(), hypercube.copy()
	hyp1[category], hyp2[category] = [], []
	for _min, _max in hypercube[category]:
		if _max < value:
			hyp1[category].append((_min, _max))
		elif _min > value:
			hyp2[category].append((_min, _max))
		elif _min <= value <= _max:
			if op == '<':
				hyp1[category].append((_min, value - 1))
				hyp2[category].append((value, _max))
			elif op == '>':
				hyp1[category].append((_min, value))
				hyp2[category].append((value + 1, _max))
	return hyp1, hyp2


def evaluate_workflow_2(hypercube, workflow, workflows):
	results = []
	for category, op, value, out in workflows[workflow][:-1]:
		hypercube1, hypercube2 = partition_hypercube(hypercube, category, op, value)
		if op == '>':
			hypercube1, hypercube2 = hypercube2, hypercube1
		results.append((hypercube1, out))
		hypercube = hypercube2
	results.append((hypercube, workflows[workflow][-1]))
	return results


def evaluate_hypercube(hypercube):
	res = 1
	for k, v in hypercube.items():
		if v:
			res *= (v[0][1] - v[0][0] + 1)
		else:
			res *= 0
	return res


def p2(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	workflows = {}
	for line in lines:
		if line == '':
			break
		workflow_name, workflow = parse_workflow(line)
		workflows[workflow_name] = workflow
	hypercube = {'x': [(1, 4000)], 'm': [(1, 4000)], 'a': [(1, 4000)], 's': [(1, 4000)]}
	results = []
	results += evaluate_workflow_2(hypercube, 'in', workflows)
	ans = 0
	while results:
		hypercube, res = results.pop(0)
		if res == 'A':
			ans += evaluate_hypercube(hypercube)
		elif res == 'R':
			continue
		else:
			results += evaluate_workflow_2(hypercube, res, workflows)
	return ans


if __name__ == '__main__':
	print(f"p1: {p1('input.txt')}")
	print(f"p2: {p2('input.txt')}")
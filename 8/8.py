import math

data = []
with open('8.txt') as f:
    data = f.read().splitlines()
inst = list(data[0])
network = {}
for line in data:
    if "=" in line:
        node, vals = line.split(" = ")
        left, right = vals.split(", ")
        left = left.split("(")[1]
        right = right.split(")")[0]
        if node not in network:
            network[node] = (left, right)


def count_steps_to_ZZZ(instructions):
    current_node = 'AAA'
    steps = 0

    for instruction in instructions:
        if instruction == 'L':
            current_node = network[current_node][0]
        elif instruction == 'R':
            current_node = network[current_node][1]
        
        steps += 1

        if current_node == 'ZZZ':
            return steps
    
    return count_steps_to_ZZZ(instructions + instructions)

instructions = data[0]  # Replace with your input
steps = count_steps_to_ZZZ(instructions)
print(steps)


def count_steps_to_ZZZ_ending_with_Z(start):
	pos = start
	idx = 0
	while not pos.endswith('Z'):
		d = inst[idx%len(inst)]
		pos = network[pos][0 if d=='L' else 1]
		idx += 1
	return idx
ret = 1
for start in network:
	if start.endswith('A'):
		ret = math.lcm(ret, count_steps_to_ZZZ_ending_with_Z(start))
print("p2", ret)
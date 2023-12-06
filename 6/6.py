import re

data = [line.strip() for line in open("6.txt").readlines()]

my_regex = r'\d+'
line1 = re.findall(my_regex, data[0])
line2 = re.findall(my_regex, data[1])

product = 1

def w2w(time, distance):
    time = int(time)
    distance = int(distance)
    ways = 0

    for h_t in range(time):
        speed = h_t
        travel_distance = speed * (time - h_t)
        if travel_distance > distance:
            ways += 1
    return ways

for i, j in zip(line1, line2):
    product *= w2w(i, j)

print("Part 1: ", product)

# 2nd part
time = "".join(line1)
distance = "".join(line2)

print("Part 2: ", w2w(time, distance))
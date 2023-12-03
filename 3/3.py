import re
from collections import defaultdict


total = 0
engine = []
number_of_gears = defaultdict(list)

def consider_number_neighbors(start_y, start_x, end_y, end_x, num):
  global number_of_gears
  for y in range(start_y, end_y+1):
    for x in range(start_x, end_x+1):
      if y >= 0 and y < len(engine) and x >= 0 and x < len(engine[y]):
        if engine[y][x] not in '0123456789.':
          if engine[y][x] == '*':
            number_of_gears[ (y,x) ].append(num)
          return True
  return False

num_pattern = re.compile('\d+')

for line in open('3.txt').readlines():
  engine.append( line.strip() )

for row_num in range(len(engine)):
  for match in re.finditer(num_pattern, engine[row_num]):
    if consider_number_neighbors(row_num-1, match.start()-1, row_num+1, match.end(), int(match.group(0))):
      total += int(match.group(0))

print(total)

rat_total = 0
for k,v in number_of_gears.items():
  if len(v) == 2:
    rat_total += v[0] * v[1]
print(rat_total)
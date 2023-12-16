import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
grid = open('16.txt').read().strip().split('\n')

rows = len(grid)
columns = len(grid[0])

DR = [-1,0,1,0]
DC = [0,1,0,-1]
def step(curr_row,curr_col,d):
  return (curr_row+DR[d], curr_col+DC[d], d)

def score(sr,sc,sd):
  position = [(sr,sc,sd)]
  seen_tiles = set()
  seen_tiles2 = set() # pt 2
  while True:
    NP = []
    if not position:
      break
    for (curr_row,curr_col,d) in position:
      #print(curr_row,curr_col,d)
      if 0 <= curr_row < rows and 0 <= curr_col < columns:
        seen_tiles.add((curr_row,curr_col))
        if (curr_row,curr_col,d) in seen_tiles2:
          continue
        seen_tiles2.add((curr_row,curr_col,d))
        ch = grid[curr_row][curr_col]
        if ch=='.':
          NP.append(step(curr_row,curr_col,d))
        elif ch=='/':
          # up right down left
          NP.append(step(curr_row,curr_col,{0:1, 1:0, 2:3, 3:2}[d]))
        elif ch=='\\':
          NP.append(step(curr_row,curr_col,{0:3, 1:2, 2:1, 3:0}[d]))
        elif ch=='|':
          if d in [0,2]:
            NP.append(step(curr_row,curr_col,d))
          else:
            NP.append(step(curr_row, curr_col, 0))
            NP.append(step(curr_row, curr_col, 2))
        elif ch=='-':
          if d in [1,3]:
            NP.append(step(curr_row,curr_col,d))
          else:
            NP.append(step(curr_row, curr_col, 1))
            NP.append(step(curr_row, curr_col, 3))
        else:
          assert False
    position = NP
  return len(seen_tiles)

print("Part 1:",score(0,0,1))
ans = 0
for curr_row in range(rows):
  ans = max(ans, score(curr_row,0,1))
  ans = max(ans, score(curr_row,columns-1,3))
for curr_col in range(columns):
  ans = max(ans, score(0,curr_col,2))
  ans = max(ans, score(rows-1,curr_col,0))
print("Part 2:", ans)
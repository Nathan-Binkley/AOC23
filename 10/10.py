import sys
from collections import defaultdict, deque
import math

def create_2d_array_from_file(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        # Read each line and split by whitespace
        lines = file.readlines()
        lines = [list(line.strip()) for line in lines]
    
    # Convert the elements to integers
    array_2d = [[element for element in line] for line in lines]
    return array_2d

grid = create_2d_array_from_file("10.txt")

start = None
start_adj = []
adj = defaultdict(list)
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        neighbors = []
        if cell == "|":
            neighbors = [(i-1, j), (i+1, j)]
        elif cell == "-":
            neighbors = [(i, j-1), (i, j+1)]
        elif cell == "L":
            neighbors = [(i-1, j), (i, j+1)]
        elif cell == "J":
            neighbors = [(i-1, j), (i, j-1)]
        elif cell == "7":
            neighbors = [(i+1, j), (i, j-1)]
        elif cell == "F":
            neighbors = [(i+1, j), (i, j+1)]
        elif cell == "S":
            start = (i, j)
        for x, y in neighbors:
            if x >= 0 and x < len(grid) and y >= 0 and y < len(row):
                adj[(i, j)].append((x, y))

adj_start = []
for vert in adj:
    for vert2 in adj[vert]:
        if vert2 == start:
            adj_start.append(vert)
adj[start] = adj_start

INF = 1000000000
dst = defaultdict(lambda: INF)
bfs_queue = deque()
bfs_queue.append(start)
dst[start] = 0
ans = (0, start)
while len(bfs_queue) > 0:
    curcell = bfs_queue.popleft()
    for nxt in adj[curcell]:
        if dst[nxt] == INF:
            dst[nxt] = dst[curcell] + 1
            ans = max(ans, (dst[nxt], nxt))
            bfs_queue.append(nxt)
print("Part 1: ", ans[0])


# Part 2:

# Special thanks to AOC Subreddit for hints on how to tackle this... tricky problem.
adj = defaultdict(list)
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        neighbors = []
        if cell == "|":
            neighbors = [(2*i-1, 2*j), (2*i+1, 2*j)]
        elif cell == "-":
            neighbors = [(2*i, 2*j-1), (2*i, 2*j+1)]
        elif cell == "L":
            neighbors = [(2*i-1, 2*j), (2*i, 2*j+1)]
        elif cell == "J":
            neighbors = [(2*i-1, 2*j), (2*i, 2*j-1)]
        elif cell == "7":
            neighbors = [(2*i+1, 2*j), (2*i, 2*j-1)]
        elif cell == "F":
            neighbors = [(2*i+1, 2*j), (2*i, 2*j+1)]
        elif cell == "S":
            start = (2*i, 2*j)
        for x, y in neighbors:
            if x >= 0 and x < 2*len(grid) and y >= 0 and y < 2*len(row):
                adj[(2*i, 2*j)].append((x, y))

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        xs = []
        if i > 0: xs.append(2*i-1)
        if i+1 < len(grid): xs.append(2*i+1)
        ys = []
        if j > 0: ys.append(2*j-1)
        if j+1 < len(row): ys.append(2*j+1)
        for new_x in xs:
            adj[(new_x, 2*j)].append((2*i, 2*j))
        for new_y in ys:
            adj[(2*i, new_y)].append((2*i, 2*j))
                
inv_start = []
indeg = defaultdict(int)
for vert in adj:
    for vert2 in adj[vert]:
        indeg[vert2] += 1
        if vert2 == start:
            inv_start.append(vert)
for vert in inv_start:
    if indeg[vert] > 0:
        adj[start].append(vert)

INF = math.inf
dst = defaultdict(lambda: INF)
bfs_queue = deque()
bfs_queue.append(start)
dst[start] = 0
ans = (0, start)
inloop = set()
while len(bfs_queue) > 0:
    curcell = bfs_queue.popleft()
    inloop.add(curcell)
    for nxt in adj[curcell]:
        if dst[nxt] == INF:
            dst[nxt] = dst[curcell] + 1
            ans = max(ans, (dst[nxt], nxt))
            bfs_queue.append(nxt)

ans2 = 0
visited = set()
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if (2*i, 2*j) in inloop or (2*i, 2*j) in visited:
            continue
        added_to_queue = set()
        cur_queue = deque()
        cur_queue.append((2*i, 2*j))
        added_to_queue.add((2*i, 2*j))
        enclosed = True
        while len(cur_queue) > 0:
            curr_x, curr_y = cur_queue.popleft()
            # print(i, j, cx, cy)
            for new_x, new_y in [(curr_x-1, curr_y), (curr_x+1, cy), (curr_x, curr_y-1), (curr_x, curr_y+1)]:
                if (new_x, new_y) in inloop or (new_x, new_y) in added_to_queue:
                    continue
                assert((new_x, new_y) not in visited)
                if new_x < 0 or new_x >= 2*len(grid) or new_y < 0 or new_y >= 2*len(row):
                    enclosed = False
                    continue
                cur_queue.append((new_x, new_y))
                added_to_queue.add((new_x, new_y))
        for c in added_to_queue:
            if c[0] % 2 == 0 and c[1] % 2 == 0 and enclosed:
                ans2 += 1
            visited.add(c)

print("Part 2: ", ans2)


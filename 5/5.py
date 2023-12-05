seeds = [2041142901, 113138307, 302673608, 467797997, 1787644422, 208119536, 143576771, 99841043, 4088720102, 111819874, 946418697, 13450451, 3459931852, 262303791, 2913410855, 533641609, 2178733435, 26814354, 1058342395, 175406592]
# seeds = [79, 14, 55, 13]
seed_finals = []

with open('5.txt', 'r') as f:
    lines = f.readlines()
sources = []
destinations = []
maps = []
for line in lines:
    # print(line)
    if line.endswith("map:\n"):
        # print(1)
        sources = []
        destinations = []
        continue
    
    if line != '\n':
        # print("Here")
        destination, source, distance = line.split()
        distance = int(distance)
        destination = int(destination)
        source = int(source)
        # print("line found: ", destination, source, distance)

        destination_range = (destination, destination + distance)
        source_range = (source, source + distance)
        sources.append(source_range)
        destinations.append(destination_range)
        # print(sources, destinations)
        # print("range", source_range, destination_range)
        
        
    else: #calculate where it goes
        # print()
        # print(sources,"\n", destinations)
        # print("calculating")
        for i, seed in enumerate(seeds):
            # print("seed", seed)
            for j, source in enumerate(sources):
                # print("source", source)
                if seed >= source[0] and seed <= source[1]:
                    destination_range = destinations[j]
                    # print("seed", seed, "in range", source)
                    # print("destination range", destination_range)
                    seeds[i] = destination_range[0] + (seed - source[0])
                    # print("new seed", seeds[i])
                    break
        destinations = []
        sources = []
            
print("Part 1:", min(seeds))

# Part 2

with open('5.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    
# seeds = list(int(s) for s in lines.pop(0).split(': ')[1].split())
# lines.pop(0)
maps = []
current = []
for l in lines:
    # print(l)
    if l.endswith('map:'):
        # print("yes")
        current = []
        continue
    if l == '\n':
        maps.append(current)
        continue
    current.append(tuple(int(n) for n in l.split()))
maps.append(current)

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

def p2(seeds, maps):
    def map_range(seed_range, map_list):
        result = []
        seed_start, seed_len = seed_range
        for dest, source, range_len in sorted(map_list, key=lambda x:x[1]):
            offset = dest - source
            if seed_start >= source and seed_start < source + range_len:
                res_start = seed_start + offset
                
                if source + range_len >= seed_start + seed_len:
                    result.append((res_start, seed_len))
                else:
                    new_seed_len = seed_start + seed_len - source - range_len
                    result.append((res_start, seed_len - new_seed_len))
                    seed_len = new_seed_len
                    seed_start = source + range_len
        if not result:
            result.append(seed_range)
        return result
    
    my_list = []
    for sp in pairwise(seeds):
        seed_ranges = [sp]
        for m in maps:
            new_s = []
            for s in seed_ranges:
                new_s.extend(map_range(s, m))
            seed_ranges = new_s[:]
        my_list.append(min(x for x, _ in seed_ranges))
    return min(my_list)
            
print("Part 2:", p2(seeds[:], maps[:]))
    
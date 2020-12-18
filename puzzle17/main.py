import sys
from itertools import product

def count_gen(generator):
    return sum(1 for x in generator)

def count_active_neighbors(cube_coord, cubes):
    def generate_neighbors():
        for direction in filter(lambda x: x != (0,0,0), product((-1,0,1),(-1,0,1),(-1,0,1))):
            yield (cube_coord[0]+direction[0], cube_coord[1]+direction[1], cube_coord[2]+direction[2])
    return count_gen(filter(lambda n: n in cubes and cubes[n], generate_neighbors()))

def visualize(cubes):
    min_max = (min(map(lambda c:c[0], cubes.keys())), max(map(lambda c:c[0], cubes.keys())))
    zrange = (min(map(lambda c:c[2], cubes.keys())), max(map(lambda c:c[2], cubes.keys())))
    print("z: {}: min/max: {}".format(zrange, min_max))
    for z in range(zrange[0], zrange[1]+1):
        print("z = {}".format(z))
        layer = []
        for y in range(min_max[0], min_max[1]+1):
            row = []
            for x in range(min_max[0], min_max[1]+1):
                cube = (x,y,z)
                row.append("#" if (x,y,z) in cubes and cubes[(x,y,z)] else ".")
            layer.append("".join(row))
        print("\n".join(layer))
        print("\n")

cubes = {}

x = y = z = 0
for c in sys.stdin.read():
    if c == '\n':
        y += 1
        x = 0
        continue
    if c == '#':
        cubes[(x,y,z)] = True
    else:
        cubes[(x,y,z)] = False
    x += 1


visualize(cubes)
print("START")

for c in range(6):
    new_cubes = {}
    for x in range(min(map(lambda c: c[0], cubes.keys())) - 1, max(map(lambda c: c[0], cubes.keys()))+1):
        for y in range(min(map(lambda c: c[1], cubes.keys()))-1, max(map(lambda c: c[1], cubes.keys()))+1):
            for z in range(min(map(lambda c: c[2], cubes.keys()))-1, max(map(lambda c: c[2], cubes.keys()))+1):
                cube = (x,y,z)
                active_neighbors = count_active_neighbors(cube, cubes)
                print("neighbors of {}: {}".format(cube, active_neighbors))
                if cube in cubes and cubes[cube]:
                    print("Setting active {} with {} to {}".format(cube, active_neighbors, 2 <= active_neighbors <= 3))
                    new_cubes[cube] = 2 <= active_neighbors <= 3
                else:
                    print("Setting inactive {} with {} to {}".format(cube, active_neighbors, active_neighbors == 3))
                    new_cubes[cube] = active_neighbors == 3
    visualize(new_cubes)
    print(" ======= ======= =======")
    cubes = new_cubes

print("Part1: {}".format(list(filter(lambda c: c, cubes.values()))))
print("Part1: {}".format(count_gen(filter(lambda c: c[1], cubes.items()))))

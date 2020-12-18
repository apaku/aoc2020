import sys
from itertools import product

def count_gen(generator):
    return sum(1 for x in generator)

def count_active_neighbors(cube_coord, cubes):
    def generate_neighbors():
        axis_count = len(list(cubes.keys())[0])
        all_directions = product(*[(-1,0,1) for axis in range(axis_count)])
        for direction in filter(lambda x: x != axis_count * (0,), all_directions):
            cube = tuple([cube_coord[axis] + direction[axis] for axis in range(axis_count)])
            yield cube
    return count_gen(filter(lambda n: n in cubes and cubes[n], generate_neighbors()))

def visualize(cubes):
    additional_ranges = []
    x_y_range = (min(map(lambda c: c[0], cubes.keys())), max(map(lambda c: c[0], cubes.keys())))
    for axis in range(2, len(list(cubes.keys())[0])):
        additional_ranges.append(list(range(min(map(lambda c: c[axis], cubes.keys())), max(map(lambda c: c[axis], cubes.keys()))+1)))
    print("Additional axes: {}".format(additional_ranges))
    additional_axes_combos = product(*additional_ranges)
    for axis_combo in additional_axes_combos:
        print("{}".format(axis_combo))
        layer = []
        for y in range(x_y_range[0], x_y_range[1]+1):
            row = []
            for x in range(x_y_range[0], x_y_range[1]+1):
                cube = tuple([x,y] + list(axis_combo))
                row.append("#" if cube in cubes and cubes[cube] else ".")
            layer.append("".join(row))
        print("\n".join(layer))
        print("\n")

def simulate(start):
    cubes = start
    axis_count = len(list(cubes.keys())[0])
    for c in range(6):
        new_cubes = {}
        axis_ranges = []
        for axis in range(axis_count):
            axis_ranges.append(list(range(min(map(lambda c: c[axis], cubes.keys())) - 1, max(map(lambda c: c[axis], cubes.keys()))+2)))
        all_cubes = product(*axis_ranges)
        for cube in all_cubes:
            active_neighbors = count_active_neighbors(cube, cubes)
            if cube in cubes and cubes[cube]:
                new_cubes[cube] = 2 <= active_neighbors <= 3
            else:
                new_cubes[cube] = active_neighbors == 3

        visualize(new_cubes)
        print(" ======= ======= =======")
        cubes = new_cubes
    return cubes

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

initial_cubes = cubes

print("PART1")
visualize(cubes)

cubes = simulate(cubes)

print("Part1: {}".format(count_gen(filter(lambda c: c[1], cubes.items()))))

print("PART2")
cubes = {}
for c,v in initial_cubes.items():
    cubes[(c[0], c[1], c[2], 0)] = v

visualize(cubes)

cubes = simulate(cubes)
print("Part2: {}".format(count_gen(filter(lambda c: c[1], cubes.items()))))


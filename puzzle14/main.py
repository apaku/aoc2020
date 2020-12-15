
import sys

mask = None
memory = {}
instructions = sys.stdin.readlines()

def apply_mask(value, mask_as_str):
    bin_str = f'{value:036b}'
    target = []
    for (i,c) in enumerate(mask_as_str):
        if c == 'X':
            target.append(bin_str[i])
        else:
            target.append(c)
    return int(''.join(target), 2)

for instr in instructions:
    if instr[:3] == 'mem':
        value = instr[instr.index(" = ")+3:]
        addr = instr[4:instr.index("]")]
        memory[addr] = apply_mask(int(value), mask)
    else:
        mask = instr.strip().replace("mask = ", "")

print("Part1: {}".format(sum(memory.values())))

memory = {}
mask = None

def apply_mask_part2(value, mask_as_str):
    bin_str = f'{value:036b}'
    target = [[]]
    for (i,c) in enumerate(mask_as_str):
        if c == '0':
            for t in target:
                t.append(bin_str[i])
        elif c == '1':
            for t in target:
                t.append("1")
        elif c == 'X':
            newtargets = []
            for t in target:
                newtargets.append(t + ["0"])
                t.append("1")
            target += newtargets
    for t in target:
        yield int("".join(t), 2)

for instr in instructions:
    if instr[:3] == 'mem':
        value = instr[instr.index(" = ")+3:]
        for addr in apply_mask_part2(int(instr[4:instr.index("]")]), mask):
            memory[addr] = int(value)
    else:
        mask = instr.strip().replace("mask = ", "")

print("Part2: {}".format(sum(memory.values())))

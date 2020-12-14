
import sys

mask = None
memory = {}

def apply_mask(value, mask_as_str):
    bin_str = f'{value:036b}'
    target = []
    for (i,c) in enumerate(mask_as_str):
        if c == 'X':
            target.append(bin_str[i])
        else:
            target.append(c)
    return int(''.join(target), 2)

for instr in sys.stdin.readlines():
    if instr[:3] == 'mem':
        value = instr[instr.index(" = ")+3:]
        addr = instr[4:instr.index("]")]
        memory[addr] = apply_mask(int(value), mask)
    else:
        mask = instr.strip().replace("mask = ", "")

print("Part1: {}".format(sum(memory.values())))

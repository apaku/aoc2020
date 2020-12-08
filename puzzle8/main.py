import sys

accumulator = 0

def nop(idx, data):
    return idx + 1

def acc(idx, arg):
    global accumulator
    accumulator += arg
    return idx + 1

def jmp(idx, arg):
    return idx + arg


def parse(instructions):
    ops = {"nop": nop, "acc": acc, "jmp": jmp}
    program = []
    for instr in instructions:
        (op, data) = tuple(instr.split(" "))
        program.append((ops[op],int(data)))
    return program

instructions = parse(sys.stdin.readlines())


def run_program(instructions):
    curidx = 0
    lines_executed = set()
    while 0 <= curidx < len(instructions):
        (op, arg) = instructions[curidx]
        if curidx in lines_executed:
            return False
        lines_executed.add(curidx)
        curidx = op(curidx, arg)
    return True

run_program(instructions)
print("Part1: {}".format(accumulator))

for i in range(len(instructions)):
    if instructions[i][0] == acc:
        continue
    accumulator = 0
    newinstr = nop if instructions[i][0] == jmp else jmp
    newinstructions = instructions[:i] + [(newinstr, instructions[i][1])] + instructions[i+1:]
    finished_successfully = run_program(newinstructions)
    if finished_successfully:
        print("Part2: {}".format(accumulator))
        break

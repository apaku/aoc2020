import sys

import operator

def has_precedence(op, op_str):
    if op == operator.add and op_str == "*":
        return True
    elif op == operator.add and op_str == "+":
        return True
    return False

def calculate(expression, precedence_fn):
    ops = []
    queue = []
    expression = expression.replace(" ", "")
    for c in expression:
        if c == "+" or c == "*":
            while len(ops) > 0 and precedence_fn(ops[-1], c) and ops[-1] != "(":
                queue.append(ops.pop())
            ops.append(operator.add if c == "+" else operator.mul)
        elif c == "(":
            ops.append(c)
        elif c == ")":
            while ops[-1] != "(":
                queue.append(ops.pop())
            ops.pop()
        else:
            queue.append(int(c))

    while len(ops) > 0:
        queue.append(ops.pop())

    result = []
    for item in queue:
        if item == operator.mul or item == operator.add:
            assert(len(result) > 1)
            op1 = result.pop()
            op2 = result.pop()
            result.append(item(op1, op2))
        else:
            result.append(item)
    assert(len(result) == 1)
    return result.pop()
expressions = [line.strip() for line in sys.stdin.readlines()]

def part1(expression):
    return calculate(expression, lambda x, y: True)

print("Part1: {}".format(sum(map(part1, expressions))))

def part2(expression):
        return calculate(expression, has_precedence)
print("Part2: {}".format(sum(map(part2, expressions))))

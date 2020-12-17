import sys

initial_numbers = list(map(lambda s: int(s), sys.stdin.readline().strip().split(",")))

def play(numbers, end_at):
    def speak(num, turn, spoken):
        if num in spoken:
            spoken[num] = (spoken[num][1], turn)
        else:
            spoken[num] = (-1, turn)
        return num

    spoken = {}

    for (i,num) in enumerate(initial_numbers):
        spoken[num] = (-1, i + 1)

    turn = len(initial_numbers) + 1
    lastnum = initial_numbers[-1]
    print("Start at: {} {} {} for {} turns".format(turn, lastnum, spoken, end_at))
    while turn < end_at:
        if lastnum in spoken and spoken[lastnum][0] == - 1:
            lastnum = speak(0, turn, spoken)
        elif lastnum in spoken and spoken[lastnum][0] != - 1:
            lastnum = speak(spoken[lastnum][1] - spoken[lastnum][0], turn, spoken)
        else:
            print("ERROR: {} {} {}".format(turn, lastnum, spoken))
            raise Exception("Blah")
        turn += 1
        if turn % 1000000 == 0:
            print("Turn: {} {}".format(turn, turn < end_at))
    return lastnum

print("Part1: {}".format(play(initial_numbers, 2021)))
print("Part2: {}".format(play(initial_numbers, 30000001)))

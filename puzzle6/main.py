import sys
import string

groups = list(sys.stdin.read().strip().split("\n\n"))
sum_questions = 0
for group in groups:
    questions = set()
    for c in group:
        if c == "\n" or c == " ":
            continue
        questions.add(c)
    sum_questions += len(questions)

print("Part1: {}".format(sum_questions))

sum_questions = 0
questions = string.ascii_lowercase
for group in groups:
    persons = group.split("\n")
    all_answered = list(filter(lambda q: len(list(filter(lambda p: q in p, persons))) == len(persons), questions))
    print("Persons: {} answered: {}".format(persons, all_answered))
    sum_questions += len(list(all_answered))

print("Part2: {}".format(sum_questions))

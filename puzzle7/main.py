import sys
import re

bag_suffix_re = re.compile(r' bags?\.?$')

def remove_bag_suffix(data):
    return bag_suffix_re.sub("", data)

def extract_number(data):
    return (int(data[:data.index(" ")]), data[data.index(" ")+1:])

rules = {}

for line in sys.stdin.readlines():
    data = line.strip().split(" contain ")
    container = data[0][:-5]
    contained = map(extract_number, filter(lambda x: x != "no other", map(remove_bag_suffix, data[1].split(", "))))
    rules[container] = list(contained)

print("Rules: {}".format(rules))

def part1(rules):
    reversed_mapping = {}
    for (container, contained) in rules.items():
        for c in contained:
            reversed_mapping.setdefault(c[1], set()).add(container)

    print("Mapping: {}".format(reversed_mapping))

    bags_to_check_container = ["shiny gold"]

    seen_bags = set()
    while len(bags_to_check_container) > 0:
        bag = bags_to_check_container.pop()
        seen_bags.add(bag)
        containers = list([c for c in reversed_mapping.get(bag, []) if c not in seen_bags])
        bags_to_check_container += containers
        print("Containers for {} == {}".format(bag, containers))

    print("Part1: {} - {}".format(seen_bags, len(seen_bags)-1))

def part2(rules):
    def bags_inside(rules, bag):
        count = 0
        for c in rules[bag]:
            print("Checking bag: {} {}".format(bag, c))
            count += c[0] + c[0] * bags_inside(rules, c[1])
        return count

    print("Part2: {}".format(bags_inside(rules, "shiny gold")))

part1(rules)

part2(rules)

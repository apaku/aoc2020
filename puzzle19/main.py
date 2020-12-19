import sys
import re

def expand(values, rules):
    expanded = []
    print("Expanding: {}".format(values))
    for v in values:
        if v.isnumeric():
            v_int = int(v)
            expanded.append( "("+"".join(expand(rules[v_int], rules)) + ")")
        else:
            print("Adding {}".format(v))
            expanded.append(v)
    print("Expanded: {}".format(expanded))
    return expanded

def parse_rules(rules):
    def parse_values(values):
        parsed = []
        for v in values:
            if v[0] == "\"":
                parsed.append(v[1:-1])
            else:
                parsed.append(v)
        return parsed
    parsed_rules = {}
    for rule in rules:
        (num, value) = tuple(rule.split(": "))
        parsed_rules[int(num)] = parse_values(value.split(" "))
    print("parsed rules: {}".format(parsed_rules))
    return expand(parsed_rules[0], parsed_rules)

(rules, messages) = tuple(sys.stdin.read().split("\n\n"))

expanded = parse_rules(rules.split("\n"))

rx = re.compile("".join(expanded))
print("RX: {}".format("".join(expanded)))
matching_msg = list(filter(lambda msg: rx.fullmatch(msg) is not None, messages.split("\n")))
print("Part1: {}".format(len(matching_msg)))

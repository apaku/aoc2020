import sys
import math

def parse_rules(io):
    def generate_rule_fn(logic):
        def validate(num):
            for rng in logic:
                if rng[0] <= num <= rng[1]:
                    return True
            return False
        return validate
    rules = {}
    while True:
        line = io.readline()
        if line.strip() == "":
            break
        rule = line.split(": ")
        logic = list(map(lambda x: (int(x[:x.index("-")]), int(x[x.index("-")+1:])), rule[1].split(" or ")))
        rules[rule[0]] = generate_rule_fn(logic)
    return rules

def parse_ticket(line):
    return list(map(lambda x: int(x), line.split(",")))

def parse_my_ticket(io):
    line = io.readline()
    if line.strip() != "your ticket:":
        raise Exception("Invalid data: {}".format(line.strip()))
    line = io.readline()
    return parse_ticket(line.strip())

def parse_nearby_tickets(io):
    line = io.readline()
    if line.strip() != "nearby tickets:":
        raise Exception("Invalid data: {}".format(line.strip()))
    tickets = []
    for line in io.readlines():
        tickets.append(parse_ticket(line.strip()))
    return tickets

def is_valid_for_any(num, rules):
    for (key,fn) in rules.items():
        if fn(num):
            return True
    return False

rules = parse_rules(sys.stdin)
myticket = parse_my_ticket(sys.stdin)
sys.stdin.readline()
nearby_tickets = parse_nearby_tickets(sys.stdin)

valid_tickets = []
invalid_ticket_numbers = []
for ticket in nearby_tickets:
    is_ticket_valid = True
    for num in ticket:
        if not is_valid_for_any(num, rules):
            invalid_ticket_numbers.append(num)
            is_ticket_valid = False
    if is_ticket_valid:
        valid_tickets.append(ticket)

print("Part1: {}".format(sum(invalid_ticket_numbers)))

valid_tickets.append(myticket)

print("Tickets for Part2: {} {}".format(valid_tickets, len(valid_tickets)))


def is_valid_for_all_tickets(rule_fn, ticket_num, tickets):
    for ticket in tickets:
        if not rule_fn(ticket[ticket_num]):
            return False
    return True

rule_positions = {}
for i in range(len(myticket)):
    for rule in rules.keys():
        if is_valid_for_all_tickets(rules[rule], i, valid_tickets):
            rule_positions.setdefault(rule, []).append(i)

while True:
    rule_positions_to_clean = list(map(lambda p: p[0], filter(lambda p: len(p) == 1, rule_positions.values())))
    for rule in filter(lambda r: len(rule_positions[r]) > 1, rule_positions):
        print("Cleaning rule {}/{} from {}".format(rule, rule_positions[rule], rule_positions_to_clean))
        rule_positions[rule] = list(filter(lambda p: p not in rule_positions_to_clean, rule_positions[rule]))

    if len(list(filter(lambda r: len(rule_positions[r]) > 1, rule_positions))) == 0:
        break
print("rule_positions: {}".format(list(sorted(map(lambda x: (x[1][0], x[0]), rule_positions.items())))))

departure_fields = list(map(lambda r: myticket[r[1][0]], filter(lambda r: r[0].startswith("departure"), rule_positions.items())))
print("Departure_fields: {}".format(departure_fields))
print("Part2: {}".format(math.prod(departure_fields)))

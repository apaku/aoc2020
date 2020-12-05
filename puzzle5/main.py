import sys
from itertools import combinations

def calculate_row(rowinfo):
    row = list(range(128))
    for c in rowinfo:
        if c == 'F':
            row = row[:len(row) // 2]
        else:
            row = row[len(row) // 2:]
    return row[0]

def calculate_col(colinfo):
    col = list(range(8))
    for c in colinfo:
        if c == 'L':
            col = col[:len(col) // 2]
        else:
            col = col[len(col) // 2:]
    return col[0]

def seatids(boarding_passes):
    for boarding_pass in boarding_passes:
        row = calculate_row(boarding_pass[:7])
        col = calculate_col(boarding_pass[7:])
        seatid = row *8+col
        print("{} -> {} * 8 + {} = {}".format(boarding_pass, row, col, seatid))
        yield seatid


allseatids = list(seatids([line.strip() for line in sys.stdin.readlines()]))
print("Part1: {}".format(max(allseatids)))

all_two_apart = list(filter(lambda x: abs(x[0]-x[1]) == 2, combinations(allseatids, 2)))
valid_seat_ids = list(set([item for sublist in all_two_apart for item in sublist]))
missing_id = list(filter(lambda x: x not in valid_seat_ids, range(40,981)))
print("Part2: {} {} {} {}".format(valid_seat_ids, max(valid_seat_ids), min(valid_seat_ids), missing_id))


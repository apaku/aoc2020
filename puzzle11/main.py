import sys
from itertools import product
original_empty_seats = set()

x = y = 0
limits = (x,y)
for c in sys.stdin.read():
    if c == 'L':
        original_empty_seats.add((x,y))
    if c == "\n":
        limits = (x, limits[1])
        x = 0
        y += 1
    else:
        x += 1

limits = (limits[0], y)
print("limits: {}".format(limits))
def count_surrounding_occupied_seats(seat, occupied_seats, empty_seats):
    surrounding_seats = [(seat[0]+i, seat[1]+j) for i in [-1,0,1] for j in [-1,0,1] if not (i==0 and j==0)]
    occupied_surrounding_seats = list(filter(lambda s: s in occupied_seats, surrounding_seats))
    return len(occupied_surrounding_seats)

def count_visible_occupied_seats(seat, occupied_seats, empty_seats):
    def next_seat(seat, direction):
        def out_of_bounds(new_seat):
            return new_seat[0] < 0 or new_seat[0] >= limits[0] or new_seat[1] < 0 or new_seat[1] >= limits[1]
        new_seat = (seat[0]+direction[0], seat[1]+direction[1])
        while not out_of_bounds(new_seat) and new_seat not in occupied_seats and new_seat not in empty_seats:
            new_seat = (new_seat[0]+direction[0], new_seat[1]+direction[1])
        return True if new_seat in occupied_seats else False

    directions = list(filter(lambda x: x != (0,0), product((-1,0,1),(-1,0,1))))
    occupied_seat_count = 0
    for direction in directions:
        is_occupied = next_seat(seat, direction)
        if is_occupied == True:
            occupied_seat_count += 1
    return occupied_seat_count

def simulate(start_empty_seats, count_fn, occupation_limit):
    occupied_seats = set()
    empty_seats = set(start_empty_seats)
    last_occupied_seats = None
    while last_occupied_seats != occupied_seats:
        print("--------- Next Iteration --------")
        new_empty_seats = set()
        new_occupied_seats = set()
        for s in empty_seats:
            if count_fn(s, occupied_seats, empty_seats) == 0:
                new_occupied_seats.add(s)
            else:
                new_empty_seats.add(s)
        for s in occupied_seats:
            if count_fn(s, occupied_seats, empty_seats) >= occupation_limit:
                new_empty_seats.add(s)
            else:
                new_occupied_seats.add(s)
        last_occupied_seats = occupied_seats
        empty_seats = new_empty_seats
        occupied_seats = new_occupied_seats
    return len(occupied_seats)

print("Part1: {}".format(simulate(original_empty_seats, count_surrounding_occupied_seats, 4)))
print("Part2: {}".format(simulate(original_empty_seats, count_visible_occupied_seats, 5)))

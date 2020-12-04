import sys
import re

color_re = re.compile(r'^#[0-9a-f]{6}$')
four_digit_re = re.compile(r'^\d{4}$')
digits_re = re.compile(r'^\d+$')
nine_digit_re = re.compile(r'^\d{9}$')
split_re = re.compile(r'[ ]+')
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
field_validators = {
        'byr': lambda x: four_digit_re.match(x) is not None and 1920 <= int(x) <= 2002,
        'iyr': lambda x: four_digit_re.match(x) is not None and 2010 <= int(x) <= 2020,
        'eyr': lambda x: four_digit_re.match(x) is not None and 2020 <= int(x) <= 2030,
        'hgt': lambda x: digits_re.match(x[:-2]) is not None and (is_valid_cm(x) or is_valid_in(x)),
        'hcl': lambda x: color_re.match(x) is not None,
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: nine_digit_re.match(x) is not None,
        'cid': lambda x: True
    }
def is_valid_cm(x):
    return x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193

def is_valid_in(x):
    return x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76

def fields_exist(passport):
    for field in required_fields:
        if not field in passport:
            return False
    return True

def isvalid(passport):
    if not fields_exist(passport):
        return False
    simple_passport = passport.replace('\n', ' ').strip()
    for field in re.split(' +', simple_passport):
        if not field_validators[field[:3]](field[4:].strip()):
            print("Field '{}' for passport: '{}' invalid".format(field, simple_passport))
            return False
    return True

data = list(sys.stdin.read().split("\n\n"))

print("Part1: valid passports: {}".format(len(list(filter(fields_exist, data)))))

print("Part2: valid passports: {}".format(len(list(filter(isvalid, data)))))

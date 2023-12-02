import re

# filename = 'example_2.txt'
filename = 'input.txt'

with open(filename, 'r') as fp:
    lines = fp.read().splitlines()


def getnum(line):
    # big hack but ok -- lookaheads are technically zero width so they do not overlap
    pt = re.compile(
        r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
    )

    line = pt.findall(line)

    lookup = {
        'one':   '1',
        'two':   '2',
        'three': '3',
        'four':  '4',
        'five':  '5',
        'six':   '6',
        'seven': '7',
        'eight': '8',
        'nine':  '9'
    }

    line = [ (lookup[g] if g in lookup else g) for g in line ]
    line = line[0] + line[-1]

    return int(line)

lines = [getnum(l) for l in lines]

print(sum(lines))
# print(lines)

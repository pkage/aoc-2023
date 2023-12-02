# filename = 'example_1.txt'
filename = 'input.txt'

with open(filename, 'r') as fp:
    lines = fp.read().splitlines()


def getnum(line):
    # hack but ok
    line = ''.join([c for c in line if c in '0123456789'])
    line = line[0] + line[-1]
    return int(line)

lines = [getnum(l) for l in lines]

print(sum(lines))

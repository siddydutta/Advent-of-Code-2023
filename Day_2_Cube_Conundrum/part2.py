from collections import defaultdict
from functools import reduce
from operator import mul


def get_power(string: str) -> int:
    max_counts = defaultdict(int)
    string.strip()
    _, sets = list(map(str.strip, string.split(':')))
    for set in sets.split(';'):
        for cube in list(map(str.strip, set.split(','))):
            count, color = list(map(str.strip, cube.split(' ')))
            max_counts[color] = max(max_counts[color], int(count))
    return reduce(mul, max_counts.values())


file = open('input.txt')
total_sum = 0
for line in file.readlines():
    total_sum += get_power(line)
print(total_sum)
file.close()

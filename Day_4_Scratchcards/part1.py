file = open('input.txt')
data = file.readlines()
file.close()

total_points = 0
for line in data:
    line = line.strip()
    card, numbers = list(map(str.strip, line.split(':')))
    winners, have = list(map(str.strip, numbers.split('|')))
    winners = set(map(int, winners.split()))
    have = set(map(int, have.split()))
    common = have.intersection(winners)
    points = 0
    if common:
        points = 1
        common.pop()
        for _ in range(len(common)):
            points *= 2
    total_points += points

print(total_points)

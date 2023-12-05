MAX_COUNT = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def is_valid_game(string: str) -> int:
    string.strip()
    game, sets = list(map(str.strip, string.split(':')))
    for set in sets.split(';'):
        for cube in list(map(str.strip, set.split(','))):
            count, color = list(map(str.strip, cube.split(' ')))
            if int(count) > MAX_COUNT[color]:
                return 0
    return int(game.split(' ')[1])


file = open('input.txt')
total_sum = 0
for line in file.readlines():
    total_sum += is_valid_game(line)
print(total_sum)
file.close()

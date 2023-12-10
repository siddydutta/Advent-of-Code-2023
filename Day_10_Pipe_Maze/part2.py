from itertools import product

# parse input data
file = open('input.txt')
data = file.read()
file.close()
data = data.strip().split('\n')
data = list(map(list, data))

# find start
m, n = len(data), len(data[0])
i, j = None, None
for row, col in product(range(m), range(n)):
    if data[row][col] == 'S':
        i, j = row, col
        break

# direction mapping
d = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((0, -1), (-1, 0)),
    '7': ((0, -1), (1, 0)),
    'F': ((1, 0), (0, 1)),
}

# breadth first search
queue = [(i, j)]
count = -1
visited = {(i, j): 0}
while queue:
    temp = []
    count += 1
    for row, col in queue:
        visited[(row, col)] = count
        if data[row][col] == 'S':
            if 0 <= row < m and 0 <= col-1 < n and data[row][col-1] in {'-', 'L', 'F'}:
                temp.append((row, col-1))
            if 0 <= row < m and 0 <= col+1 < n and data[row][col+1] in {'-', 'J', '7'}:
                temp.append((row, col+1))
            if 0 <= row-1 < m and 0 <= col < n and data[row-1][col] in {'|', 'F', '7'}:
                temp.append((row-1, col))
            if 0 <= row+1 < m and 0 <= col < n and data[row+1][col] in {'|', 'J', 'L'}:
                temp.append((row+1, col))
        elif data[row][col] in d:
            for dx, dy in d[data[row][col]]:
                if 0 <= row+dx < m and 0 <= col+dy < n and (row+dx, col+dy) not in visited:
                    temp.append((row+dx, col+dy))
    queue = temp

# count included tiles based on row (so far) parity
verticals = {'|', 'J', 'L', 'S'}  # inclusion of S depends on input
tiles = 0
for row, col in product(range(m), range(n)):
    if (row, col) not in visited:
      count = 0
      for idx in range(col):
        # exclude tiles not in loop
        if (row, idx) in visited and data[row][idx] in verticals:
          count += 1
      tiles += count % 2

print(tiles)

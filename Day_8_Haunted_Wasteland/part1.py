file = open('input.txt')
data = file.read()
file.close()

data = data.strip().split('\n')
moves = data[0]
maps = data[2:]

graph = dict()
for node in data[2:]:
    graph[node[0:3]] = (node[7:10], node[12:15])

node = 'AAA'
count = 0
idx = 0
while node != 'ZZZ':
    if moves[idx] == 'L':
        node = graph.get(node)[0]
    elif moves[idx] == 'R':
        node = graph.get(node)[1]
    idx = (idx + 1) % len(moves)
    count += 1

print(count)

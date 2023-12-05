file = open('input.txt')
data = file.readlines()
file.close()

counts = [1] * len(data)
for i, line in enumerate(data, start=0):
    card, numbers = list(map(str.strip, line.split(':')))
    winners, have = list(map(str.strip, numbers.split('|')))
    winners = set(map(int, winners.split()))
    have = set(map(int, have.split()))
    common = have.intersection(winners)
    for n in range(len(common)):
        counts[i+n] += counts[i-1]
print(sum(counts))

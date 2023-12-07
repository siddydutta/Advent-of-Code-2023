from collections import Counter
from functools import cmp_to_key


file = open('input.txt')
data = file.read()
file.close()

# high card, one pair, two pair, three of a kind, full house, four of a kind, five of a kind
kinds = [[], [], [], [], [], [], []]
for line in data.strip().split('\n'):
    hand, score = line.split()
    freq = Counter(hand).most_common(2)
    k, k2 = freq[0][1], freq[1][1] if len(freq) > 1 else None
    if k == 5:
        # five of a kind
        kinds[6].append((hand, score))
    elif k == 4:
        # four of a kind
        kinds[5].append((hand, score))
    elif k == 3:
        if k2 == 2:
            # full house
            kinds[4].append((hand, score))
        else:
            # three of a kind
            kinds[3].append((hand, score))
    elif k == 2:
        if k2 == 2:
            # two pair
            kinds[2].append((hand, score))
        else:
            # one pair
            kinds[1].append((hand, score))
    else:
        # high card
        kinds[0].append((hand, score))


order = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
def compare(element1, element2):
    for ch1, ch2 in zip(element1[0], element2[0]):
        if ch1 != ch2:
            return 1 if order.get(ch1) > order.get(ch2) else -1
    return 0

i = 1
winnings = 0
for kind in kinds:
    kind.sort(key=cmp_to_key(compare), reverse=True)
    for hand, score in kind:
        winnings += i * int(score)
        i += 1

print(winnings)

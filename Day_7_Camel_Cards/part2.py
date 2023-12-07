from collections import Counter
from functools import cmp_to_key


file = open('input.txt')
data = file.read()
file.close()


# high card, one pair, two pair, three of a kind, full house, four of a kind, five of a kind
kinds = [[], [], [], [], [], [], []]
for line in data.strip().split('\n'):
    hand, score = line.split()
    freq = Counter(hand)
    j = freq.pop('J', 0)
    k1 = freq.most_common(2)[0][1] if freq else None
    k2 = freq.most_common(2)[1][1] if len(freq) > 1 else None
    if j == 5:
        # five of a kind
        kinds[6].append((hand, score))
    elif k1 == 5:
        # five of a kind
        kinds[6].append((hand, score))
    elif k1 == 4:
        if j == 1:
            # five of a kind
            kinds[6].append((hand, score))
        else:
            # four of a kind
            kinds[5].append((hand, score))
    elif k1 == 3:
        if j == 2:
            # five of a kind
            kinds[6].append((hand, score))
        elif j == 1:
            # four of a kind
            kinds[5].append((hand, score))
        elif k2 == 2:
            # full house
            kinds[4].append((hand, score))
        else:
            # three of a kind
            kinds[3].append((hand, score))
    elif k1 == 2:
        if j == 3:
            # five of a kind
            kinds[6].append((hand, score))
        elif j == 2:
            # four of a kind
            kinds[5].append((hand, score))
        elif j == 1:
            if k2 == 2:
                # full house
                kinds[4].append((hand, score))
            else:
                # three of a kind
                kinds[3].append((hand, score))
        elif k2 == 2:
            # two pair
            kinds[2].append((hand, score))
        else:
            # one pair
            kinds[1].append((hand, score))
    else:
        if j == 4:
            # five of a kind
            kinds[6].append((hand, score))
        elif j == 3:
            # four of a kind
            kinds[5].append((hand, score))
        elif j == 2:
            # three of a kind
            kinds[3].append((hand, score))
        elif j == 1:
            # one pair
            kinds[1].append((hand, score))
        else:
            # high card
            kinds[0].append((hand, score))

order = {'A': 1, 'K': 2, 'Q': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12, 'J': 13}
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

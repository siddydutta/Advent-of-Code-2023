from typing import Optional


class TrieNode:
    def __init__(self):
        self.children = {}
        self.digit = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, number: str, digit: int) -> None:
        node = self.root
        for ch in number:
            node = node.children.setdefault(ch, TrieNode())
        node.digit = digit

    def find(self, number: str) -> Optional[int]:
        node = self.root
        for ch in number:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node.digit


trie = Trie()
numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
for digit, number in enumerate(numbers, start=1):
    trie.add(number, digit)


def get_number(string: str) -> int:
    all_digits = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if substring.isdigit():
                all_digits += substring
                break
            digit = trie.find(substring)
            if digit is not None:
                all_digits += str(digit)
                break
    return int(all_digits[0] + all_digits[-1])


file = open('input.txt')

total_sum = 0
for line in file.readlines():
    total_sum += get_number(line.strip())

print(total_sum)

file.close()

file = open('input.txt')

total_sum = 0
for line in file.readlines():
    number = ''
    for ch in line.strip():
        if ch.isdigit():
            number += ch
            break
    for ch in reversed(line.strip()):
        if ch.isdigit():
            number += ch
            break
    total_sum += int(number)

print(total_sum)

file.close()

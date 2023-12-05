DELTA = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

file = open('input.txt')
data = file.read()
file.close()

data = data.strip()
schematic = list(map(list, (map(str.strip, data.split('\n')))))

part_number_indices = []
for n_row, row in enumerate(schematic):
    current_number = []
    current_indices = []
    for n_col, ch in enumerate(row):
        if ch.isdigit():
            current_number.append(ch)
            current_indices.append((n_row, n_col))
        else:
            if current_number:
                part_number = int(''.join(current_number))
                part_number_indices.append((part_number, current_indices))
            current_number = []
            current_indices = []
    # for numbers at the end of the row
    if current_number:
        part_number = int(''.join(current_number))
        part_number_indices.append((part_number, current_indices))

part_numbers_sum = 0
for part_number, indices in part_number_indices:
    added = False
    for n_row, n_col in indices:
        for d_row, d_col in DELTA:
            row = n_row + d_row
            col = n_col + d_col
            if 0 <= row < len(schematic) and 0 <= col < len(schematic[0]):
                if not schematic[row][col].isdigit() and schematic[row][col] != '.':
                    part_numbers_sum += part_number
                    added = True
                    break
        if added:
            break

print(part_numbers_sum)

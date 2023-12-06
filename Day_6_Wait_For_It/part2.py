from tqdm import tqdm

file = open('input.txt')
data = file.read()
file.close()

time = int(''.join(list(map(str, data.split('\n')[0].split()[1:]))))
distance = int(''.join(list(map(str, data.split('\n')[1].split()[1:]))))

options = 0
for i in tqdm(range(0, time+1)):
    d = i * (time - i)
    if d > distance:
        options += 1
print(options)

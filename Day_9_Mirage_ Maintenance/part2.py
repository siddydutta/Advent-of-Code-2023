file = open('input.txt')
data = file.read()
file.close()

data = data.strip().split('\n')
data = list(map(str.split, data))
data = [list(map(int, d)) for d in data]

def extrapolate(nums):
    if not any(nums):
        return 0
    return nums[-1] + extrapolate([n2-n1 for n1, n2 in zip(nums[:-1], nums[1:])])

print(sum(extrapolate(d[::-1]) for d in data))

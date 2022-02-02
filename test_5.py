l,r = [int(i) for i in input().split()]


def checker(number):
    if len(set(str(number))) == 1:
        return 1
    else: return 0

sum = 0

for i in range(l,r+1):
    sum += checker(i)

print(sum)

from itertools import permutations

myList = [int(num) for num in input().split(' ')]

zeroPerms = []

for perm in permutations(myList, r=3):
    if sum(perm) == 0:
        for smallPerm in permutations(perm, r=3):
            if smallPerm in zeroPerms:
                break
        else:
            zeroPerms.append(perm)

print(zeroPerms)
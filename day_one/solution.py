file = open("./input.txt")

llist: list[int] = []
rlist: list[int] = []
distance: list[int] = []

for line in file.readlines():
    if not len(line) >= 2:
        continue

    nums = line.split("   ")
    llist.append(int(nums[0]))
    rlist.append(int(nums[1]))

file.close()

if len(rlist) != len(llist):
    raise ValueError("lists must be of the same size")

llist.sort()
rlist.sort()

for _ in range(len(rlist)): # 1000
    ml = min(llist)
    mr = min(rlist)

    distance.append(abs(ml - mr))
    llist.pop(llist.index(ml))
    rlist.pop(rlist.index(mr))


print(sum(distance))

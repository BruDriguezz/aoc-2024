import timeit

def compute_distance():
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

    for _ in range(len(rlist)):  # Assuming ~1000 iterations
        ml = min(llist)
        mr = min(rlist)

        distance.append(abs(ml - mr))
        llist.pop(llist.index(ml))
        rlist.pop(rlist.index(mr))

    return sum(distance)

execution_time = timeit.timeit("compute_distance()", setup="from __main__ import compute_distance", number=1000)
print(f"Average execution time over 1000 runs: {execution_time / 1000:.6f} seconds")

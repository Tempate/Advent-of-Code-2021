with open("input.txt") as input:
    numbers = list(map(int, input.read().splitlines()))


def increasing_values(vector):
    increasing = 0

    for m, n in zip(vector[:-1], vector[1:]):
        increasing += int(n > m)

    return increasing


groups = []

for m, n, p in zip(numbers[:-2], numbers[1:-1], numbers[2:]):
    groups.append(m + n + p)


print("Part 1:", increasing_values(numbers))
print("Part 2:", increasing_values(groups))
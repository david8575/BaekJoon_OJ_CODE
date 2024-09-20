from itertools import combinations

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

for case_dwarf in combinations(dwarfs, 7):
    if sum(case_dwarf) == 100:
        case_dwarf = list(case_dwarf)
        case_dwarf.sort()
        for dwarf in case_dwarf:
            print(dwarf)
        break
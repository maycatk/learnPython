from random import choice
cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])
for i in cave_numbers:
    passage_to =choice(cave_numbers)
    caves[i].append(passage_to)
print caves

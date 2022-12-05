inputFile = "input.txt"  # Not full path

result = []
with open(inputFile, 'r') as fp:
    for i in fp.readlines():
        tmp = i.split()
        try:
            result.append(str(tmp[0].replace("\n", "")))
        except ValueError:
            pass

def priority_count(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

# Part One
count = 0
for line in result:
    ruck = list(line)
    ruckSplit = int(len(ruck) / 2)
    ruckCompartment = ruck[:ruckSplit], ruck[ruckSplit:]

    for i in ruckCompartment[0]:
        if i in ruckCompartment[1]:
            count += priority_count(i)
            break
print("Part 1: " + str(count))

# Part Two
count2 = 0
resultGroups = [result[i:i+3] for i in range(0, len(result), 3)]

for sublist in resultGroups:
    for item in sublist[0]:
        if item in sublist[1] and item in sublist[2]:
            count2 += priority_count(item)
            break
print("Part 2: " + str(count2))

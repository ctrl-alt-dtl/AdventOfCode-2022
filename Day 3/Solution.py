inputFile = "input.txt"  # Not full path

result = []
with open(inputFile, 'r') as fp:
    for i in fp.readlines():
        tmp = i.split()
        try:
            result.append(str(tmp[0].replace("\n", "")))
        except ValueError:
            pass

# print(result)
count = 0


def priority_count(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


for line in result:
    ruck = list(line)
    ruckSplit = int(len(ruck) / 2)
    ruckCompartment = ruck[:ruckSplit], ruck[ruckSplit:]

    for i in ruckCompartment[0]:
        if i in ruckCompartment[1]:
            count += priority_count(i)
            break
print("Count: " + str(count))

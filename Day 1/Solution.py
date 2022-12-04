from itertools import groupby

inputFile = open("input.txt", 'r') # not full path
data = inputFile.read()
inputFile.close()

dataInList = data.split('\n')

result = []
for i in dataInList:
    try:
        e = int(i)
        result.append(e)
    except ValueError:
        result.append('')  # Re-add the '' so we can break up into subgroup lists

newResult = [list(sub) for element, sub in groupby(result, key=bool) if element]
# Sum all subgroups
sumList = [sum(l) for l in newResult]

# Part 1 Top Amount
print("Part 1: " + str(sum(sorted(sumList, reverse=True)[:1])))
# Part 2 Top Three Added
print("Part 2: " + str(sum(sorted(sumList, reverse=True)[:3])))

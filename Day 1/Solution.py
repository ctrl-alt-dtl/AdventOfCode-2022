from itertools import groupby

inputFile = open("input.txt", 'r') #not full path

data = inputFile.read()

dataInList = data.split('\n')
inputFile.close()

result = []
for i in dataInList:
    try:
        e = int(i)
        result.append(e)
    except:
        result.append('')

newResult = [list(sub) for element, sub in groupby(result, key=bool) if element]

sumList = [sum(l) for l in newResult]

print("Part 1: " + str(sum(sorted(sumList, reverse=True)[:1])))

print("Part 2: " + str(sum(sorted(sumList, reverse=True)[:3])))
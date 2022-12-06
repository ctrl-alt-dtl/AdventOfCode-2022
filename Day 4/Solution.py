inputFile = open("input.txt", 'r')  # not full path
data = inputFile.read()
inputFile.close()

dataInList = data.split()
count = 0

for x in dataInList:
    a = x.split(',')
    section1 = a[0].split('-')
    section2 = a[1].split('-')

    if (int(section1[0]) <= int(section2[0]) and int(section1[1]) >= int(section2[1])) or \
            (int(section2[0]) <= int(section1[0]) and int(section2[1]) >= int(section1[1])):
        count += 1

print("Part 1: " + str(count))

inputFile = open("input.txt", 'r')  # not full path
data = inputFile.read().split()
inputFile.close()

count = 0
assignment = 0

for x in data:
    pair = x.split(',')
    section1 = list(map(int, pair[0].split('-')))
    section2 = list(map(int, pair[1].split('-')))

    # Part One
    if (section1[0] <= section2[0] and section1[1] >= section2[1]) or \
            (section2[0] <= section1[0] and section2[1] >= section1[1]):
        count += 1

    # Part Two
    if max(section1[0], section2[0]) <= min(section1[1], section2[1]):
        assignment += 1

print("Part 1: " + str(count))
print("Part 2: " + str(assignment))

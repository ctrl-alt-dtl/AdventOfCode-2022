inputFile = open("input.txt", 'r')
data = inputFile.read()
inputFile.close()

# Part 1
for i in range(4, len(data)):
    if len(set(data[i-4:i])) == 4:
        break

print("Part 1: " + str(i))

# Part 2
for i in range(14, len(data)):
    if len(set(data[i-14:i])) == 14:
        break

print("Part 2: " + str(i))

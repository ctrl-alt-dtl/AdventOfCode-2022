inputFile = open("input2.txt", 'r')
rawData = inputFile.read().split("\n")
inputFile.close()

print(rawData)
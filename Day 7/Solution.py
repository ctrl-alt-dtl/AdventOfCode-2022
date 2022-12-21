from collections import defaultdict
inputFile = open("input2.txt", 'r')
rawData = inputFile.read().split("\n")
inputFile.close()

data = []
for x in rawData:
    data.append(x.split(" "))

directoryDict = root = {}

paths = []

for line in data:
    if line[0] == '$':
        if line[1] == 'cd':
            if line[0] == "dir":
                if "dir" not in directoryDict:
                    directoryDict["dir"] = [line[1]]
                else:
                    directoryDict["dir"].append(line[1])

    if line[0] != "$" and line[0] != "dir":
        # print(line)
        if "fileSize" not in directoryDict:
            directoryDict["fileSize"] = ([line[0]])
        else:
            directoryDict["fileSize"].append((line[0]))
        if "fileName" not in directoryDict:
            directoryDict["fileName"] = [line[1]]
        directoryDict["fileName"].append(line[1])
    print(line)

print(directoryDict)


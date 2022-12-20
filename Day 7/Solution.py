import pathlib
inputFile = open("input2.txt", 'r')
rawData = inputFile.read().split("\n")
inputFile.close()

data = []
for x in rawData:
    data.append(x.split(" "))

directoryDict = {}

for line in data:
    #print(line)
    if line[0] == "dir":
        if "dir" not in directoryDict:
            directoryDict["dir"] = []
        directoryDict["dir"].append(line[1])

    if line[0] != '$' and line[0] != "dir":
        #print(line)
        if "fileSize" not in directoryDict:
            directoryDict["fileSize"] = []
        directoryDict["fileSize"].append(int(line[0]))
        if "fileName" not in directoryDict:
            directoryDict["fileName"] = []
        directoryDict["fileName"].append(line[1])


print(directoryDict)
inputFile = open("input2.txt", 'r')
rawData = inputFile.read().split("\n")
inputFile.close()

data = []
for x in rawData:
    data.append(x.split(" "))

directoryDict = {}

for line in data:
    # print(line)
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                if "root" not in directoryDict:
                    directoryDict["root"] = [line[2]]
                else:
                    directoryDict["root"].append(line[1])

    else:
        if line[0] == "dir":
            if "dir" not in directoryDict:
                directoryDict["dir"] = [line[1]]
            else:
                directoryDict["dir"].append(line[1])

        else:
            if line[0] != "$" and line[0] != "dir":
                # print(line)
                if "size" not in directoryDict:
                    directoryDict["size"] = ([line[0]])
                else:
                    directoryDict["size"].append((line[0]))
                if "name" not in directoryDict:
                    directoryDict["name"] = [line[1]]
                directoryDict["name"].append(line[1])

print(directoryDict)


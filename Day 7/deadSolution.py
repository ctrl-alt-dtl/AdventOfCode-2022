inputFile = open("input2.txt", 'r')
rawData = inputFile.read().split("\n")
inputFile.close()

data = []
for x in rawData:
    data.append(x.split(" "))

class DirectoryPath:
    def __init__(self, index, parent=None, size=0):
        self.index = index
        self.parent = parent
        self.content = {}
        self.size = size
        self.lessSize = size

root = DirectoryPath(0)
index = 1
nodeDictonary = {}
current = root

# Map the directory
for line in data:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current = current.parent
            else:
                directoryName = line[2]
                if directoryName == "/":
                    current = root
                else:
                    current = current.content[directoryName]

    # Breaking down directory and fileName & fileSizes
    else:
        if line[0] == "dir":
            directoryName = line[1]
            print("Dir: " + directoryName)
            nodeDictonary[index] = DirectoryPath(index, parent=current)
            current.content[directoryName] = nodeDictonary[index]
            index += 1
        else:
            if line[0] != '':
                fileSize = int(line[0])
                fileName = line[1]
                print(f"\tName: {fileName : <10} Size: {str(fileSize) : >}")
                nodeDictonary[index] = DirectoryPath(index, parent=current, size=fileSize)
                current.content[fileName] = nodeDictonary[index]
                index += 1


# Part 1
totalSizeOfDirs = 0

# TODO: Walk and sum

print("Part 1: " + str(totalSizeOfDirs))

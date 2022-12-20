inputFile = open("input2.txt", 'r')
rawData = inputFile.read().split("\n")
inputFile.close()

data = []
for x in rawData:
    data.append(x.split(" "))

class Node:
    def __init__(self, index, parent=None, size=0):
        self.index = index
        self.parent = parent
        self.content = {}
        self.size = size
        self.lessSize = size

root = Node(0)
index = 1
nodeDictonary = {}
current = root

# Walk the directory
for line in data:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current = root
            else:
                directoryName = line[2]
                if directoryName == "/":
                    current = root
                else:
                    current = current.content[directoryName]



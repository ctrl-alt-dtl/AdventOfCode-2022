inputFile = open("input2.txt", 'r')
data = inputFile.read().split("\n")
inputFile.close()

rep = []
for x in data:
    rep.append(x.split(" "))

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
for line in rep:
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



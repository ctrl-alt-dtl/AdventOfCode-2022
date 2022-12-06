inputFile = "input2.txt"  # Not full path

result = []
with open(inputFile, 'r') as fp:
    for i in fp.readlines():
        tmp = i.split()
        try:
            result.append(str(tmp[0]))
        except ValueError:
            pass

print(result)

crossAssignment = 0
pair = [[result[i]] for i in range(len(result)-1)]
print(pair)
for x in pair:
    for i in x:
        section = i.split(',')
        print(section)








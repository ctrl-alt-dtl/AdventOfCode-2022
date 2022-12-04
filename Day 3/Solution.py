inputFile = "input.txt" #Not full path

result = []
with open(inputFile, 'r') as fp:
    for i in fp.readlines():
        tmp = i.split(' ')
        try:
            result.append(str(tmp[0].replace("\n", "")))
        except ValueError:
            pass

print(result)
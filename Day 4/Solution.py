inputFile = "input2.txt"  # Not full path

with open(inputFile, 'r') as fp:
    result = fp.read().splitlines()

print(result)

out = []
for i in result:
    out.extend(list(i.split(',')))

print(out)








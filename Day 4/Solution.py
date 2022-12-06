inputFile = "input2.txt"  # Not full path

with open(inputFile, 'r') as fp:
    result = fp.read().splitlines()

# print(result)

count = 0

for x in range(len(result)-1):
    a = result[x].split(',')
    # print(a[0], a[1])

    section1 = a[0].split('-')
    section2 = a[1].split('-')

    if section1[0] >= section2[0] and section1[1] <= section2[1] or \
            section2[0] >= section1[0] and section2[1] <= section1[1]:
        print(section1[0], section1[1])
        print(section2[0], section2[1])
        print("")
        count += 1

print(count)





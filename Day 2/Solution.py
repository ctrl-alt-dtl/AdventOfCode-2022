inputFile = "input.txt" #Not full path

# Trying a different way to read and split input file
result = []
with open(inputFile, 'r') as fp:
    for i in fp.readlines():
        tmp = i.split(' ')
        try:
            result.append((str(tmp[0]), str(tmp[1].replace("\n", ""))))
        except ValueError:
            pass
# print(result)

# A - Rock = 1, B - Paper = 2, C - Scissors = 3
# X - Rock = 1, Y - Paper = 2, Z - Scissors = 3
# 0 = Lost, 3 = Draw, 6 = Won

finalScore = 0
x = 0

while x < len(result):
    # Win + 6
    if result[x][0] == 'A' and result[x][1] == 'Y': # 2
        finalScore += 8
    if result[x][0] == 'B' and result[x][1] == 'Z': # 3
        finalScore += 9
    if result[x][0] == 'C' and result[x][1] == 'X': # 1
        finalScore += 7

    # Lose + 0
    if result[x][0] == 'A' and result[x][1] == 'Z': # 3
        finalScore += 3
    if result[x][0] == 'B' and result[x][1] == 'X': # 1
        finalScore += 1
    if result[x][0] == 'C' and result[x][1] == 'Y': # 2
        finalScore += 2

    # Draw + 3
    if result[x][0] == 'A' and result[x][1] == 'X': # 1
        finalScore += 4
    if result[x][0] == 'B' and result[x][1] == 'Y': # 2
        finalScore += 5
    if result[x][0] == 'C' and result[x][1] == 'Z': # 3
        finalScore += 6

    x += 1

    # print(result[x][0], result[x][1])

# Part 1 Score
print("Part 1: " + str(finalScore))

# Part 2 Score
print("Part 2: " + str(finalScore))

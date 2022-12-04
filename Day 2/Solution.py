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

# A - Rock = 1, B - Paper = 2, C - Scissors = 3
# X - Rock = 1, Y - Paper = 2, Z - Scissors = 3
# 0 = Lost, 3 = Draw, 6 = Won

finalScore = 0
x = 0

while x < len(result):
    # Win + 6
    if result[x][0] == 'A' and result[x][1] == 'Y':  # 2
        finalScore += 8
    if result[x][0] == 'B' and result[x][1] == 'Z':  # 3
        finalScore += 9
    if result[x][0] == 'C' and result[x][1] == 'X':  # 1
        finalScore += 7

    # Lose + 0
    if result[x][0] == 'A' and result[x][1] == 'Z':  # 3
        finalScore += 3
    if result[x][0] == 'B' and result[x][1] == 'X':  # 1
        finalScore += 1
    if result[x][0] == 'C' and result[x][1] == 'Y':  # 2
        finalScore += 2

    # Draw + 3
    if result[x][0] == 'A' and result[x][1] == 'X':  # 1
        finalScore += 4
    if result[x][0] == 'B' and result[x][1] == 'Y':  # 2
        finalScore += 5
    if result[x][0] == 'C' and result[x][1] == 'Z':  # 3
        finalScore += 6

    x += 1
    # print(result[x][0], result[x][1]) # DEBUG

# Part 1 Score
print("Part 1: " + str(finalScore))

# Part 2
# A - Rock = 1, B - Paper = 2, C - Scissors = 3
# X - Lose = 0, Y - Draw = 3, Z - Win = 6

i = 0
finalScore2 = 0
while i < len(result):
    # Win + 6
    if result[i][0] == 'A' and result[i][1] == 'Z':  # R < P + W = 8
        finalScore2 += 8
    if result[i][0] == 'B' and result[i][1] == 'Z':  # P < S + W = 9
        finalScore2 += 9
    if result[i][0] == 'C' and result[i][1] == 'Z':  # S < R + W = 7
        finalScore2 += 7

    # Lose + 0
    if result[i][0] == 'A' and result[i][1] == 'X':  # R > S = 3
        finalScore2 += 3
    if result[i][0] == 'B' and result[i][1] == 'X':  # P > R = 1
        finalScore2 += 1
    if result[i][0] == 'C' and result[i][1] == 'X':  # S > P = 2
        finalScore2 += 2

    # Draw + 3
    if result[i][0] == 'A' and result[i][1] == 'Y':  # R + R + D = 4
        finalScore2 += 4
    if result[i][0] == 'B' and result[i][1] == 'Y':  # P + P + D = 5
        finalScore2 += 5
    if result[i][0] == 'C' and result[i][1] == 'Y':  # S + S + D = 6
        finalScore2 += 6

    i += 1

# Part 2 Score
print("Part 2: " + str(finalScore2))

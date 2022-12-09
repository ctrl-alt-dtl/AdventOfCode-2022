import copy

# Because I am lazy and do not want to write code to parse this multi-2d list
cargo_crates = [
    ['H', 'C', 'R'],
    ['B', 'J', 'H', 'L', 'S', 'F'],
    ['R', 'M', 'D', 'H', 'J', 'T', 'Q'],
    ['S', 'G', 'R', 'H', 'Z', 'B', 'J'],
    ['R', 'P', 'F', 'Z', 'T', 'D', 'C', 'B'],
    ['T', 'H', 'C', 'G'],
    ['S', 'N', 'V', 'Z', 'B', 'P', 'W', 'L'],
    ['R', 'J', 'Q', 'G', 'C'],
    ['L', 'D', 'T', 'R', 'H', 'P', 'F', 'S']
]
test_crates = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]
# Making a deep copy of the list for Part 2, because reasons...
cargo_crates2 = copy.deepcopy(cargo_crates)

# Part 1
moves = []  # final list for moves
with open("input.txt", 'r') as fp:
    for i in fp.readlines():
        tmp = i.split()
        all_moves = []  # parsing all moves in each odd index of each read line
        for w in range(1, len(tmp), 2):
            try:
                all_moves.append(int(tmp[w]))
            except ValueError:
                pass
        moves.append(all_moves)

for num, start, finish in moves:
    for i in range(num):
        x = cargo_crates[start - 1].pop()
        cargo_crates[finish - 1].append(x)

print("Part 1: " + "".join([a[-1] for a in cargo_crates]))

# Part 2 - This hurt my head.....
for num, start, finish in moves:
    multi_stack = cargo_crates2[start - 1][-num:]
    cargo_crates2[start - 1] = cargo_crates2[start - 1][:-num]
    cargo_crates2[finish - 1] += multi_stack

print("Part 2: " + "".join([a[-1] for a in cargo_crates2]))

cups = [1, 0, 0]
moves = {'A': [0, 1], 'B': [1, 2], 'C': [0, 2]}

moves_string = input()

for move in moves_string:
    index_a, index_b = moves[move]
    cups[index_a], cups[index_b] = cups[index_b], cups[index_a]

print(cups.index(1) + 1)
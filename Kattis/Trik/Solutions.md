# Solutions

## Python 3

## Brute Force

```python
cups = [1, 0, 0]
moves = {'A': [0, 1], 'B': [1, 2], 'C': [0, 2]}

moves_string = input()

for move in moves_string:
    index_a, index_b = moves[move]
    cups[index_a], cups[index_b] = cups[index_b], cups[index_a]

print(cups.index(1) + 1)
```

If we consider the cups to be a list of `0` and `1` where `0` signifies an empty cup and `1` signifies the position of the ball, then each "move" is essentially a swapping of indexes. Move `A` means swap the first and second indexes, move `B` swaps the second and third indexes and move `C` swaps and first and the third indexes.

In this approach we create a dictionary from the move "name" and to the list of indexes it swaps. Then we can simply iterate over the string of moves and swap indexes accordingly. When we are done performing all moves we can find the index of `1` in the `cups` list and print it (remembering to add `1`).

## Possible improvements

After a small analysis of this problem it is apparent that performing the same move an even number of times returns the state of the `cups` to its original state (for example, the state of `cups` after performing the moves `AA` is congruent to its initial state). In fact, this is true regardless of the parity of the number of times the same move is performed in modulo 2 (for example, `A` is the same as `AAA`).

We can take advantage of this by normalizing the moves input string before performing any move.

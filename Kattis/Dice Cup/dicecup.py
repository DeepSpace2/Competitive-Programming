from collections import Counter
from itertools import product

dice_a, dice_b = map(int, input().split())
counts = Counter(map(sum, product(range(1, dice_a + 1), range(1, dice_b + 1))))
top_sums = [str(k) for k, v in counts.items() if v == max(counts.values())]
print('\n'.join(top_sums))
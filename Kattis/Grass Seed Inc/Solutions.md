# Solutions

## Python 3

```python
from functools import reduce

cost_per_one_sqr_mtr = float(input())
number_of_lawns = int(input())
lawns = [(tuple(map(float, input().split()))) for _ in range(number_of_lawns)]
print(reduce(lambda total, lawn: total + lawn[0] * lawn[1] * cost_per_one_sqr_mtr, lawns, 0))
```
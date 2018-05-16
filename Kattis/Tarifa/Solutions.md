# Solutions

## Python 3

```python

from functools import reduce

mb_per_month, num_of_months = (int(input()) for _ in range(2))
usages = (int(input()) for _ in range(num_of_months))
print(reduce(lambda x, y: x + mb_per_month - y, usages, mb_per_month))
```
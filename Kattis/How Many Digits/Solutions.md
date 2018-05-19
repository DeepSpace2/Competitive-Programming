# Solutions

One may take the naive approach while attempting to solve this problem (calculating `n!` then checking its length). However, given the range of the possible inputs `[1, 10000]` it will be quickly apparent that this approach can't be used. Instead, we can use [Kamenetsky's formula](http://oeis.org/A034886) to guesstimate the number of digits in `n!`.

## Python 3

```python
from math import e, log10, pi

while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n == 0:
        print(1)
    else:    
        print(int(n * log10(n / e) + log10(2 * pi * n) / 2) + 1)
```
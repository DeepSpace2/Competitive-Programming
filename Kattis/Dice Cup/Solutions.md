# Solutions

## Python 3

```python
from collections import Counter
from itertools import product

dice_a, dice_b = map(int, input().split())
counts = Counter(map(sum, product(range(1, dice_a + 1), range(1, dice_b + 1))))
top_sums = [str(k) for k, v in counts.items() if v == max(counts.values())]
print('\n'.join(top_sums))
```

Using 2 powerful built-in modules in Python (`collections` and `itertools`) this otherwise tedious task becomes more manageable.

*For sake of simplicity 3-faced dice is used for the explanation*

`itertools.product` returns the cartesian product of 2 (or more) iterables with no repetitions:

```python
>>> list(product((1, 2, 3), (1, 2, 3)))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
```

Then, by applying `sum` to it, we get the list of sums of each combination:

```python
>>> list(map(sum, [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]))
[2, 3, 4, 3, 4, 5, 4, 5, 6]
```

By passing the list of sums to `Counter` we are getting back a dictionary with `<sum>:<count>` pairs:

```python
>>> Counter([2, 3, 4, 3, 4, 5, 4, 5, 6])
Counter({4: 3, 3: 2, 5: 2, 2: 1, 6: 1})
```

Now, we could have used the `most_common` method, but we don't necessarily know how many sums are most common, so unfortunately we have to iterate over the dictionary and pick the sums whose values are equal to the most frequent one.

```python
>>> counter = Counter([2, 3, 4, 3, 4, 5, 4, 5, 6])
>>> [k for k, v in counter.items() if v == max(counter.values())]
[4]
```

The only thing left for us to do is to generate the output in the correct format.

```python
>>> counter = Counter([2, 3, 4, 3, 4, 5, 4, 5, 6])
>>> '\n'.join([str(k) for k, v in counter.items() if v == max(counter.values())])
'4'
```
# Python 3

## Brute Force

```python
min_range, max_range, required_sum = (int(input()) for _ in range(3))

valid_numbers = [num for num in range(min_range, max_range + 1)
                 if sum(map(int, str(num))) == required_sum]

print(valid_numbers[0])
print(valid_numbers[-1])
```

We create the list `valid_numbers` which contains all the numbers between `min_range` and `max_range` whose sum of digits is `required_sum` (as calculated by `sum(map(int, str(num)))`).

Since we iterate over the range `[min_range, max_range]` the list `valid_numbers` is guaranteed to be sorted so we don't need to use `min(valid_numbers)` and `max(valid_numbers)` (which will needlessly iterate over `valid_numbers` twice). We can instead output the first and last numbers directly.
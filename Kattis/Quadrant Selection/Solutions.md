# Solutions

## Python 3

```python
x, y = map(int, (input() for _ in range(2)))
if x > 0:
    print(1 if y > 0 else 4)
else:
    print(2 if y > 0 else 3)
```

The input here is a bit more tricky because it is provided as 2 different lines. In order to read it in a single line of code we read the input in a generator and then use `map` to convert both inputs to integers.

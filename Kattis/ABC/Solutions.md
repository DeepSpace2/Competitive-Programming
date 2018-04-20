# Python 3

```python
nums = map(str, sorted(map(int, input().split())))
order = input()
d = dict((k, v) for k, v in zip(sorted(order), nums))
print(' '.join(d[ch] for ch in order))
```

A generic solution that accepts any number of inputs. It uses a dictionary that associates each number to its precedence.
# Python 3

```python
print('\n'.join('{} Abracadabra'.format(n) for n in range(1, int(input()) + 1)))
```

A single-line solution that may look complex at first sight but really isn't. Working from bottom to top:

------------

```python
int(input()) + 1
```

Reading the input we were given, converting to an integer and adding 1.

------------

```python
for n in range(1, int(input()) + 1)
```

Using the aforementioned input to build a range from `1` to the integer we were provided.

------------

```python
'{} Abracadabra'.format(n) for n in range(1, int(input()) + 1)
```

This creates a generator object whose elements are strings of the form

```
'1 Abracadabra', '2 Abracadabra', ... 'N Abracadabra'
```

------------

```python
'\n'.join('{} Abracadabra'.format(n) for n in range(1, int(input()) + 1))
```

`'\n'.join` joins all the strings in the aforementioned generator with `'\n'` (new-line character) in between to a single string which is then printed with `print`. This provide the required output to this problem.
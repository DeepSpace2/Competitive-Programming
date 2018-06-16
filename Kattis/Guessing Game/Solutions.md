# Solutions

## Python 3

```python
lower_bound, upper_bound = 1, 10
while True:
    guess = int(input())
    if guess == 0:
        break
    response = input()
    if response == 'right on':
        print('Stan may be honest') if lower_bound <= guess <= upper_bound else print('Stan is dishonest')
        lower_bound, upper_bound = 1, 10
    elif response == 'too low':
        lower_bound = max(lower_bound, guess + 1)
    elif response == 'too high':
        upper_bound = min(upper_bound, guess - 1)
```
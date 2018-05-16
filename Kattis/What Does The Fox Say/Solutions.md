# Solutions

## Python 3

```python
cases = int(input())
for _ in range(cases):
    recording = input().split()
    data = input()
    while data != 'what does the fox say?':
        identified_sound = data.split()[-1]
        recording = [sound for sound in recording if sound != identified_sound]
        data = input()
    print(' '.join(recording))
```

Except for the fancy context and input, this question is essentially about removing the correct strings from a list.
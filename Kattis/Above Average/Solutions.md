# Python 3

```python
test_cases = int(input())
for _ in range(test_cases):
    num_of_students, *grades = map(int, input().split())
    avg = sum(grades) / num_of_students
    print('{:.3f}%'.format(sum(1 for grade in grades if grade > avg) / num_of_students * 100))
```
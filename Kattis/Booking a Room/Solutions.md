# Solutions

## Python 3

```python
total_rooms, booked_rooms = map(int, input().split())
if total_rooms == booked_rooms:
    print('too late')
else:
    booked_rooms_nums = {int(input()) for _ in range(booked_rooms)}
    for temp_room in range(1, total_rooms + 1):
        if temp_room not in booked_rooms_nums:
            print(temp_room)
            break
```
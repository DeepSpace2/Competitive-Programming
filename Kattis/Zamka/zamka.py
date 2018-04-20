min_range, max_range, required_sum = (int(input()) for _ in range(3))

valid_numbers = [n for n in range(min_range, max_range + 1)
                 if sum(map(int, str(n))) == required_sum]

print(valid_numbers[0])
print(valid_numbers[-1])
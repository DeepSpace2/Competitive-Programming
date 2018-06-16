input()
li = list(map(int, input().split()))
output = [li[0]]
output.extend(n for n in li if n > output[-1])
print(len(output))
print(' '.join(map(str, output)))
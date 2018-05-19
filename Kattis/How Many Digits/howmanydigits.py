from math import e, log10, pi

while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n == 0:
        print(1)
    else:    
        print(int(n * log10(n / e) + log10(2 * pi * n) / 2) + 1)
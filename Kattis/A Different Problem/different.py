while True:
    try:
        line = input()
    except EOFError:
        break
    a, b = map(int, line.split())
    print(abs(a - b))
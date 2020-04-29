import random as r
while True:
    n = r.randint(1, 100)
    print(n)
    if n == 50:
        break

    if n % 3 != 0:
        continue

    print(n)
    
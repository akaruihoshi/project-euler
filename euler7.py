a = int(input("Prime ke berapa? "))
x = 4
y = 2
prm = [2, 3]

while len(prm) < a:
    is_prime = True
    # untuk nyari tau apakah dia prime apa ga
    x1 = x ** 0.5
    if x1 % 1 > 0:
        x1 = int(x1) + 1
    while y <= x1 and is_prime:
        z = x / y
        if z % 1 == 0:
            is_prime = False
        y = y + 1
    if is_prime:
        prm.append(int(x))
    y = 2
    x = x + 1

print(prm[a-1])

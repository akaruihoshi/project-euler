a = int(input("Batas atas? "))
x = 5
y = 2
prm = [2, 3]
prr = 5
is_prime = True

# while prm[(len(prm))-1] <= a and x <= a:
while x <= a:
    # untuk nyari tau apakah dia prime apa ga
    # print(f"x {x}")
    x1 = x ** 0.5
    if x1 % 1 > 0:
        x1 = int(x1) + 1
    # while y < len(prm) and is_prime and y <= x1:
    while is_prime and y <= x1:
        # print(prm[y])
        # z = x / prm[y]
        # print(x, y, prr)
        z = x / y
        if z % 1 == 0:
            is_prime = False
            break
        y = y + 1
    if is_prime:
        prr = prr + x
        # prm.append(int(x))
        # print(x)
        # print("PRIME LOH!!!!!")
        # print(prm[0:a])
    is_prime = True
    y = 2
    x = x + 2


# print(prm[0:len(prm)])
print(prr)

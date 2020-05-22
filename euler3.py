a = 600851475143
x = 2
y = 2

while x <= a:
    is_prime = True
    # untuk nyari tau apakah dia prime apa ga
    if x > 3:
        x1 = x ** 0.5
        if x1 % 1 > 0:
            x1 = int(x1) + 1
        while y <= x1 and is_prime:
            z = x / y
            if z % 1 == 0:
                is_prime = False
            y = y + 1
    y = 2
    # untuk tau apakah bisa dibagi sama angka tersebut
    while is_prime:
        # print(a)
        if a % x == 0:
            a = a / x
        else:
            is_prime = False
    x = x + 1

print(x-1)

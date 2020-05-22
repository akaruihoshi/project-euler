n = int(input("Meh? "))
a = b = c = 1
z = 1
is_break = False

while a <= n // 2:
    while b <= a:
        while c <= b and a + b + c <= n:
            # print(f"a {a}, b {b}, c {c}")
            z = a + b + c
            # print(z)
            if z == n:
                if (c*c)+(b*b) == (a*a):
                    # print(f"{c*c} + {b*b} = {a*a}")
                    # print("break")
                    is_break = True
                break
            c = c + 1
        if is_break:
            break
        b = b + 1
        c = 1
    if is_break:
        break
    a = a + 1
    b = 1
    c = 1

ans = a*b*c

print(ans)

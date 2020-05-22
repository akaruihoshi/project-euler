col = int(input("Kolom? "))
row = int(input("Baris? "))
dig = int(input("Digit? "))

x = 0
y = 0
a = []

# while y < row:
#     a.append([])
#     while x < col:
#         z = int(input(""))
#         a[y].append(z)
#         x = x + 1
#     y = y + 1
#     x = 0

while y < row:
    a.append([])
    s = input(f"Angka di line {y+1} = ")
    a[y] = [int(i) for i in s.split()]
    # while x < col:
    #     z = int(input(""))
    #     a[y].append(z)
    #     x = x + 1
    y = y + 1
    x = 0

# vertical
x = y = z = yy = 0
sm = 1
ans = 1
while x < col:
    while y < row:
        if y < row - dig + 1:
            while z < dig:
                # print(x, yy, f"value {a[yy][x]}")
                sm = sm * a[yy][x]
                # print(f"sum {sm}")
                z = z + 1
                yy = yy + 1
            y = y + 1
            yy = y
            z = 0
        if ans < sm:
            ans = sm
        # print(f"ans {ans}")
        sm = 1
        if y >= row - dig + 1:
            break
    y = z = yy = 0
    x = x + 1

# horizontal
x = y = z = xx = 0
sm = 1
while y < row:
    while x < col:
        if x < col - dig + 1:
            while z < dig:
                # print(xx, y, f"value {a[y][xx]}")
                sm = sm * a[y][xx]
                # print(f"sum {sm}")
                z = z + 1
                xx = xx + 1
            x = x + 1
            xx = x
            z = 0
        if ans < sm:
            ans = sm
        # print(f"ans {ans}")
        sm = 1
        if x >= col - dig + 1:
            break
    x = z = xx = 0
    y = y + 1

# diagonal forward
x = y = z = 0
sm = 1
while x < col:
    while y < row:
        if x < col - dig + 1 and y < row - dig + 1:
            while z < dig:
                yy = y + z
                xx = x + z
                # print(xx, yy, z, f"value {a[yy][xx]}")
                sm = sm * a[yy][xx]
                # print(f"sum {sm}")
                z = z + 1
            y = y + 1
            z = 0
        if ans < sm:
            ans = sm
        # print(f"ans {ans}")
        sm = 1
        if x >= col - dig + 1 or y >= row - dig + 1:
            break
    y = z = 0
    x = x + 1

# diagonal backward
x = 0
y = row
z = 0
sm = 1
while x < col:
    while y > 1:
        if x < col - dig + 1 and y >= dig:
            while z < dig:
                yy = y - z - 1
                xx = x + z
                # print(xx, yy, z, f"value {a[yy][xx]}")
                sm = sm * a[yy][xx]
                # print(f"sum {sm}")
                z = z + 1
            y = y - 1
            z = 0
        if ans < sm:
            ans = sm
        # print(f"ans {ans}")
        sm = 1
        if x >= col - dig + 1 or y < dig:
            break
    y = row
    z = 0
    x = x + 1

y = 0
while y < row:
    print(a[y][0:col])
    y = y + 1
print(ans)

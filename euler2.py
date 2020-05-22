f1 = 0
f2 = 1
total = 0

x = f1 + f2

while x < 4000000:
    if x % 2 == 0:
        total = total + x
    f1 = f2
    f2 = x
    x = f1 + f2

print(f"Jumlahnya: {total}")

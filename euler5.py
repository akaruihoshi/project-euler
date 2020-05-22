a = int(input("Batas atasnya "))
x = z = 4
mult = [1, 2, 3]
y = x - 2
ind = 2

# untuk masukin data ke array
while x <= a:
    while y >= 1:
        # kalau pembaginya hasilnya 1 berarti ga perlu ditambah
        # kalau hasil sampe akhir sisanya 1 otomatis ke break jadi ga nambah array
        if z / mult[y] == 1:
            break
        # kalau pembaginya lebih dari 1 dan mod nya 0 / bukan pecahan artinya bisa dibagi
        elif z / mult[y] > 1 and z % mult[y] == 0:
            # hasil pembagiannya disimpen
            z = z / mult[y]
        # kalau sampe akhir masih ada sisa z dimasukin ke array
        if y == 1:
            mult.append(int(z))
            ind = ind + 1
        y = y - 1
    x = x + 1
    y = ind
    z = x

# untuk mengkalikan semua angka di dalam array
s = 1
t = ind
while t >= 0:
    s = s * mult[t]
    t = t - 1

# print(mult[0:ind])
print(s)

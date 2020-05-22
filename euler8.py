numbr = int(input("Silahkan masukan digitnya! "))
digit = int(input("Berapa digit bersebelahan? "))
lennb = len(str(numbr))
listd = []
y = lennb

while len(listd) <= lennb:
    x = numbr % (10**y) // (10**(y-1))
    listd.append(x)
    y = y-1

i = 1
j = lennb
k = 1
ans = 1
while j >= digit:
    while k <= digit:
        # print(f"j-k {j-k}")
        # print(f"listd[j-k] {listd[j-k]}")
        i = i * listd[j-k]
        # print(f"i {i}")
        k = k + 1
    if i > ans:
        ans = i
    # print(f"ans {ans}")
    i = 1
    j = j - 1
    k = 1

# print(listd[0:lennb])
print(ans)

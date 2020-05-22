number = int(input("Angkanya berapa? "))
x = 1
y = 0

while x < number:
    if x % 3 == 0 or x % 5 == 0:
        y = y + x
    x = x + 1

print(f"Jumlahnya: {y}")

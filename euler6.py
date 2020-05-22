a = int(input("Batas atasnya "))
x = 1
sm = 0
sq = 0

while x <= a:
    sm = sm + (x * x)
    x = x + 1
# print(sm)

x = 1
while x <= a:
    sq = sq + x
    x = x + 1
sqr = sq * sq
# print(sqr)

diff = sqr - sm
print(diff)

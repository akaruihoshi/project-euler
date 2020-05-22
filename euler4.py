x = 999
y = 999
number = x * y
numberlen = len(str(number))
is_palindrome = False
z = 0
pal = 0

while number > 10000 and is_palindrome == False:
    while x > 100 and is_palindrome == False:
        while y > 100 and is_palindrome == False:
            is_palindrome = True
            while numberlen > 0 and is_palindrome:
                #print(f"angkanya sekarang {number} dari {x} x {y}")
                aa = number % (10**(numberlen)) // (10**(numberlen-1))
                zz = number % (10**(z+1)) // (10**z)
                if aa != zz:
                    is_palindrome = False
                z = z + 1
                numberlen = numberlen - 1
                if numberlen == 0:
                    if number > pal:
                        pal = number
                        xx = x
                        yy = y
                    else:
                        pal = pal
            y = y - 1
            number = x * y
            numberlen = len(str(number))
            z = 0
            is_palindrome = False
        y = 999
        x = x - 1
    is_palindrome = True

print(f"Angkanya adalah {pal} berdasarkan perkalian {xx} x {yy}")

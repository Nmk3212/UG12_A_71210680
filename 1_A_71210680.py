deret = input("Masukkan deret angka : ")
spl = deret.split(",")
con = len(spl)

if(int(spl[0]) % 2 == 0):
    x = spl[0]
    jum = int(x)
else:
    x = int(spl[0]) * -1
    jum = int(x)

print("Total :", x, end="")

for y in spl[1:con]:
    if ( y != spl[0]):
        if (int(y) % 2 == 1):
            y = int(y) * -1
            jum = jum + int(y)
            print("",y, end="")
        elif (int(y) % 2 == 0):
            jum = jum + int(y)
            if (y == spl[0]):
                print(y, end="")
            else:
                print(" +", y, end="")

print()
print("Hasil perhitungan diatas ialah",jum)
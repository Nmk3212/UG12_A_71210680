nam = []
kurs = []
rep = True

while (rep):
    nama = input("Masukkan nama : ")
    if (nama == "STOP"):
        break
    kursi = int(input("Masukkan nomor kursi "+nama+" : "))
    if (kursi in kurs):
        print("Mohon maaf kursi tersebut telah terisi!")
    if (kursi not in kurs):
        nam.append(nama)
        kurs.append(kursi)

print()
print("List kursi yang telah terisi : ")

for x in range(0, len(kurs), 1):
    print("Kursi nomor", kurs[x], "telah diisi oleh", nam[x])
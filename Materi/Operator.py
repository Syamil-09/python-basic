x = 80
y = 100
print("x:", x)
print("y:", y)
# operator penugasan += (y = y+5)
y += 5
y += 5
print("y:", y)

# operator penugasan -= (y = y-10)
y -= 10
y -= 10
print("y:", y)

# input (menerima inputan dari user)
kelasBudi = input("Kamu kelas mana Budi ?")
print("Budi dari kelas", kelasBudi)

# if - elif - else (kondisional)
# operator pembandingan == (sama dengan nilai)
if (kelasBudi == "10 B"):
    print("Wah kamu kenal Fudhoil dong")
elif(kelasBudi == "10 C"):
    print("Wah wali kelas kamu Pak Andi ya")
else:
    print("Ya sudah lah...")

# operator pembandingan != (tidak sama dengan nilai)
jenisKelaminBudi = "Laki-Laki"
if (jenisKelaminBudi != "Laki-Laki"):
    print("Budi Wedok")
else:
    print("Budi Lanang")

# operator pembanding > (Lebih Besar) dan < (Lebih Kecil)
nilaiBudi = 90 # Lolos (true)
naialAsep = 80
if (nilaiBudi > naialAsep):
    print("Budi di beliin HP kesukaannya sama bapak nya", nilaiBudi)
else:
    print("Budi di marahin bapak nya", nilaiBudi)

nilaiKedisiplinanBudi = 60 # gak Lolos (False)
if (nilaiBudi > 70 and nilaiKedisiplinanBudi > 70):
    print("Selamat Budi Lanjut ke Semester 2")
else:
    print("Kamu Harus Remedial Budi!")
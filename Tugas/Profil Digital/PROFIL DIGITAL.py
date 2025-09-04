print("-----> CHALLENGE DIGITAL PROFILE <-----")

name = input("Nama :")
umur = input("Umur :")
kelas = input("Kelas :")
hobi = input("Hobi :")
cita = input("Cita-cita :")
waktu = input("Lebih Suka Belajar Pagi atau Malam :")
kelahiran = input("Tahun Kelahiran :")

print("1. Wibu")
print("2. Gamer")
print("3. K-Popers")
print("4. Anak Konten")
print("5. Anak Nongki")
tipeDigitalKamu = int(input("Masukan tipe gaya digital kamu :"))
if (tipeDigitalKamu == 1):
    wibuu = input("Siapa waifu atau husbando kamu ?")
    komentar1 = print("Ihhh bau bawang")

if (tipeDigitalKamu == 2):
    game = input("Apa game favorit kamu ?")
    komentar2 = print("Pasti seharian main game terus")

if (tipeDigitalKamu == 3):
    kpop = input("Siapa bias mu ?")
    komentar3 = print("Ihhh pasti suka nya opa-opa")

elif (tipeDigitalKamu == 4):
    konten = input("Platform favorit kamu?Tiktok?Youtube?")
    komentar4 = print("Followers nya pati dikit,upsss")

elif (tipeDigitalKamu == 5):
    nongki = input("Nongkrong paling sering dimana ?")
    komentar5 = print("Boleh juga tuh tempatnya")

bau = input("Apakah teman disebelah kamu bau Ya/Tidak ?")

if (bau == "Ya"):
    komentarYa = print("Busettt hidung aku udah gk kuat nih nahan nya ")

elif (bau == "Tidak"):
    komentarTidak = print("Behhh hoki seumur hidup tuh ")
print(" ")
print(" ")

print("=== PROFIL DIGITAL KAMU ===")
print("Nama :", name)
print("Umur :", umur)
print("Kelas :", kelas)
print("Hobi :", hobi)
print("Cita-cita :", cita)
print("Belajar paling enak pas :", waktu)
print("Tahun kelahiraan :", kelahiran)
print(" ")


print("== TIPE DIGITAL ==")

if (tipeDigitalKamu == 1):
    print("Tipe : Wibu")
    print("Waifu/Husbando favorit :", wibuu)
    print("Komentar :", komentar1)

if (tipeDigitalKamu == 2):
    print("Tipe : Gamer")
    print("Game favorit :", game)
    print("Komentar :", komentar2)

if (tipeDigitalKamu == 3):
    print("Tipe : K-Popers")
    print("Bias favorit :", kpop)
    print("Komentar :", komentar3)

elif (tipeDigitalKamu == 4):
    print("Tipe : Anak Konten")
    print("Platfrom favorit :", konten)
    print("Komentar :", komentar4)

elif (tipeDigitalKamu == 5):
    print("Tipe : Anak Nongki")
    print("Tempat favorit :", nongki)
    print("Komentar :", komentar5)
print(" ")


print("= FUN CHEK =")

if (bau == "Ya"):
    print("Temen sebelah bau :", bau)
    print(komentarYa)

elif (bau == "Tidak"):
    print("Temen sebelah bau :", bau)
    print(komentarTidak)
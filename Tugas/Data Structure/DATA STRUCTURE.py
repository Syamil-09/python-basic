print("-----| CHALLENGE DATA STRUCTURE |-----")
print(" ")

print("Tantangan 1 : Jadwal Piket Harian 🕌")
print(" ")

print("---> Jadwal piket hari ini :")
piket_hari_ini = ["Dihyah", "Evandra", "Fadhil"]
for name in piket_hari_ini:
    print("-", name)
print(" ")

print(" Tantangan 2 : Rukun Iman dan Rukun Islam ✨")
print(" ")

print("---> Rukun Islam :")
rukun_islam = ("Syahadat", "Shalat", "Zakat", "Puasa", "Haji") 
for islam in range(len(rukun_islam)):
    print(f"{islam + 1}. {rukun_islam[islam]}")
print(" ")

print("---> Rukun Iman :")
rukun_iman = (
    "Iman Kepada Allah SWT",
    "Iman Kepada Malaikat",
    "Iman Kepada Kitab",
    "Iman Kepada Rosul",
    "Iman Kepada Hari Akhir",
    "Iman Kepada Qodo dan Qodar"
) 
for iman in range(len(rukun_iman)):
    print(f"{iman + 1}. {rukun_iman[iman]}")
print(" ")

print("Tantangan 3 : Kitab-Kitab Pelajaran 📚")
print(" ")

print("---> Kitab-kitab yang dipelajari :")
kitab_dipelajari = {"Kitab Tajwid", "Kitab Fiqih", "Kitab Aqidah"}
for kitab in kitab_dipelajari:
    print("-", kitab)
print(" ")

print("Tantangan 4 : Biodata Santri 🎓")
print(" ")

print("---> Biodata Santri :")
biodata = {
    "Nama": "Farhat Syamil Pangestu",
    "Kelas": "X - B",
    "Hafalan Juz": 30,           
 }
for key, value in biodata.items():
    print(f"{key} : {value}")














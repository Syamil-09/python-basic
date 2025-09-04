print("                                           MATERI 8 - FUNCTION DASAR")
print(" ")

# Struktur fungsi dasar tanda parameter
def halo_dunia():
    print("Hello World")
    print("Halo Dunia")

# Cara akses function, sertakan nama dan () -nya
halo_dunia() 
print(" ")

# Fungsi dengan perameter (variabel di fungsi)
def sapa_sapa_gan(nama):
    print("Hello", nama, "Welcome in Indonesia")
sapa_sapa_gan("Farhat")
sapa_sapa_gan("Syamil")
sapa_sapa_gan("Pangestu")
print(" ")

# Kalau manual begini
print("Hello Farhat welcome in indonesia")
print("Hello Syamil welcome in indonesia")
print("Hello pangestu welcome in indonesia")
print("")

# Fungsi dengan banyak parameter
def rumus_luas_segitiga(alas, tinggi):
    print("Alas :", alas)
    print("Tinggi :", tinggi)
    rumusan_segitiga = 1/2 * (alas * tinggi)
    print("Hasil :", rumusan_segitiga)
rumus_luas_segitiga(14, 8)
rumus_luas_segitiga(12, 16)
print("")

def rumus_luas_tabung(phi, jari_jari, tinggi):
    print("r (Jari-jari) :", jari_jari)
    print("Tinggi        :", tinggi)
    print("π (Phi)       :", phi)
    rumusan_tabung = 2 * phi * jari_jari * (jari_jari * tinggi)
    print("Hasil         :", rumusan_tabung)
rumus_luas_tabung(22/7, 21, 12)
rumus_luas_tabung(3.14, 7, 13)
print("")

# Filter teman toxic
def filter_teman_toxic(nama, sifat):
    # Ciri-ciri toxic
    sifat_toxic = [
     "Julid",
     "Pamer",
     "Ngatain",
     "Baperan",
     "Manipulatif",
     "Drama",
     "Sombong"
    ]
    # Deteksi kata toxic dari parameter sifat di atas
    if any(kata in sifat for kata in sifat_toxic):
         print(nama, "Itu temen TOXIC, kabooooor....")
    else:
        print(nama, "Temen baek tuhhh,MANTAPPPPP...")

filter_teman_toxic("Syamil", "Rajin Disiplin Baik hati Pintar Cerdas")
filter_teman_toxic("Asep", "Pintar Sombong Pamer Ngatain")
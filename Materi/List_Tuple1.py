print("                                           MATERI 6 - PYTHON DATA STRUCTURE")
print(" ")
# List -> [] -> berurutan, berubah, duplikat
daftar_belanjaan = [
    "Es Teh Desa", # index 0
    "Olive Chicken", # index 1
    "Gorengan", # index 2
]
print("Daftar Belanjaan :", daftar_belanjaan)
print(daftar_belanjaan[0]) # akses ke index 0

# apped() menambah item ke akhir list
daftar_belanjaan.append("Gabin")

# insert() menambah item ke spesifik index (bisa di awal,tenggah,akhir.Tergantung nomer index yg kita inginkan)
daftar_belanjaan.insert(0, "Naspad Kawan Lamo")
print("Daftar Belanjaan Sekarang :", daftar_belanjaan)

# remove() menghapus item berdasarkan valeu (Namanya)
daftar_belanjaan.remove("Olive Chicken")
print("Daftar Belanjaan Akhir :", daftar_belanjaan)

# [no_index:no_urut_item]
print("Potong list :", daftar_belanjaan[1:3])

# menggabungkan list +
jajanan_bilal = ["Basreng", "Macaroni"]
jajanan_dzaki = ["Pisang Kembung", "Pentol"]
jajanan_syamil = ["Roti Bakar", "Siomai"]
gabungan_jajanan = jajanan_dzaki + jajanan_bilal + jajanan_syamil
print("Gabungan Jajanan :", gabungan_jajanan)
print("Bilal nambah :", jajanan_bilal * 3)
print("Syamil nambah :", jajanan_syamil * 2)
print(" ")


# Tuple -> () -> berurutan, TIDAK bisa diubah
ttl = ("DKI Jakatra", 18, "Mei", 2009)
print("TTL Syamil :", ttl)
print("Tanggal Lahir :", ttl[1])

# unpacking tuple ke variable baru
# harus berurutan sesuai value nya
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print("Tempat Lahir :", tempat_lahir)
print("Tahun Lahir :", thn_lahir)

# list multi dimensi
daftar_minuman = [
["Kopi", "Ronde", "Susu Jahe"], # baris 0
["Jus Apel", "Jus Stowberi", "Jus Alpukat", "Jus Mangga"], # baris 1
["es Doger", "Es Cendol", "Es Jeruk"], # baris 2
]
print(daftar_minuman)
print("Minuman Hangat Favorit Syamil :", daftar_minuman[0][1]) # Masukkan baris nya terlebih dahulu lalu index nya
print("Jus Favoris Syamil :", daftar_minuman[1][1]) 
print("Es Favorit Syamil :", daftar_minuman[2][1])
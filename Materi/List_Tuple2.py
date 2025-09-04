kumpulan_angka = [1, 2.5, 3, 4, 5]
print(kumpulan_angka)
campuran = ("Syamil", 15, False)
for i in campuran:
    print(1)

#               LIST
# Bisa diubah dan menggunakan []
# Len -> untuk menghitung panjang data
data_nama = ["Dihyah", "Evandra", "Fadil", "Fudhoi"]
print(len(data_nama))

# Insert -> untuk menambahkan data sesuai keinginan kita
data_nama.insert(0, "Syamil")
print(data_nama)

# Append -> untuk menambahkan data di akhir (hanya bisa satu data saja)
data_nama.append("Hanif Cawas")
print(data_nama)

# Remove -> untuk menghapus data sesuai yg kita inginkan
data_nama.remove("Evandra")
print(data_nama)

# Pop -> untuk menghapus data terakhir
data_nama.pop()
print(data_nama)

# Extend -> untuk menambahkan data di akhir (harus lebih dari satu)
data_baru = ["Harist", "Dzaki"]
data_nama.extend(data_baru)
print(data_nama)

#                TUPLE
# Tidak bisa diubah dan menggunakan ()
my_tuple = ("Syamil", "Hanif", "Dihyah")
# my_tuple.append("Evandra") -> jika ditulis seperti ini akan error, karena tuple tdk bisa diubah/dimanipulasi
print(" ")
print(" ")
print("              Tugas Dari Bang Daffa")
print(" ")
print(" ")
peserta = int(input("Masukan Jumlah Peserta :"))
list = []

for i in range(0, peserta):
     nama = input("Masukkan Nama :")
     list.append(nama)

print(list)
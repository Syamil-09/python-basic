print("                                                  MATERI 9 - PYTHON 3 FUNCTION")
print(" ")

print("-------> DEF <-------")
# Fungsi biasa dengan "def"
def hello_world(name):
    print("Hello Mr.",name)
    print(f"How are you doing {name} ?") # f {formatting string}
hello_world("Farhat")
hello_world("Syamil")
hello_world("Pangestu")
print(" ")

print("-------> LAMBDA <-------")
# Fungsi anonim dengan "lambada"
greeting = lambda name: print(f"Hello, {name} with lambada")
greeting("Syamil")
greeting("Dihyah")
greeting("Hanif")
print(" ")

print("===== KONVERSI TIPE DATA =====")
# "" artinya string walaupun isi nya angka
nilai_string = "100" # Tipe datanya string
nilai_integer = int(nilai_string) # int(ubah jadi integer)
kalikan_dua_salah = nilai_string * 2
kalikan_dua_bener = nilai_integer * 2
print(kalikan_dua_salah, kalikan_dua_bener)
print(" ")

# map() untuk mentransformasi data
# map([fungi_perubahan_data], [sumber_data])
nilai_mentah = [79, 94, 86, 100, 75, 68, 98]
nilai_kali_seratus = map(lambda nilai: nilai * 100, nilai_mentah)
# Konversi map object menjadi list
list_nilai_kali_dua = list(nilai_kali_seratus)
print(f"Nilai mentah : {nilai_mentah}")
print(f"Nilai x 100 : {nilai_kali_seratus}")
print(" ")

# sorted () mengurutkan data
daftar_siswa = [
    {"Nama": "Syamil", "Angka": 18},
    {"Nama": "Dzaky", "Angka": 77},
    {"Nama": "Hanif", "Angka": 26},
    {"Nama": "Abdul Ubuntu", "Angka": 5},
]
                             # for loop -> mengeluarkan isi list
print("Daftar Angka Asli =")
for siswa in daftar_siswa:
    print(siswa)
print("--------------- PEMBATAS --------------- ")
daftar_angka_tersusun = sorted(daftar_siswa, key=lambda siswa: siswa["Angka"]) # Menyusun dari yg nilai-nya terkecil
print("Daftar Tersusun =")                                                     # hingga yg nilai-nya terbesar.  
for siswa in daftar_angka_tersusun:
    print(siswa)
print(" ")

# sorting list 
daftar_nama_kelas_b = ["Hanif", "Wildan", "Syamil", "Ziyad", "Royyan", "Abdul", "Azmi"]
daftar_nama_terurut = sorted(daftar_nama_kelas_b) # A ke Z (Kecil - Besar)
daftar_nama_terbalik = sorted(daftar_nama_kelas_b, reverse=True) # Z ke A (Besar - Kecil)
for nama in daftar_nama_terurut:
    print(nama)
print("---------- PEMBATAS ----------")
for nama in daftar_nama_terbalik:
    print(nama)
print("")

print("|||||||  FILTER  |||||||")
# filter() menyaring data
transaksi = [18000, 27000, 11000, 7500, 34000]
transaksi_besar = filter(lambda angka: angka >= 15000, transaksi)
list_transaksi_besar = list(transaksi_besar)
print("Data Transaksi :", transaksi)
print("Transaksi di atas 15rb :", list_transaksi_besar)





























































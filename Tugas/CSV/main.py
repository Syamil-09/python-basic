import csv

# Baca Semua Data Dari CSV
with open("keuangan.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

print("\n")

# 1. Menampilkan Semua Data
print("📌 Semua Data :")
print("-" * 50)
print("  Tanggal  | Katerangan | Kategori | Jumlah")
print("-" * 50)
for row in data:
    print(f"{row['Tanggal']} | {row['Keterangan']} | {row["Kategori"]} | Rp.{row["Jumlah"]}")
    # Boleh Menggunakan '' Atau "" Di -> Tanggal,Keterangan,Kategori,Jumlah.
    # Tetapi Di Bahasa Progaman Lain Biasanya Harus Dengan ''
print("-" * 50)
print(" ")

# 2.  Menghitung Semua Pengeluaran
total = sum(int(row['Jumlah']) for row in data)
print(f"💰 Total Pengelaran : Rp.{total}")
print(" ")

# 3. Mnghitung Total Per Kategori
kategori_total = {}
for  row in data:
    kategori = row["Kategori"]
    jumlah = int(row["Jumlah"])
    if kategori not in kategori_total:
        kategori_total[kategori] = 0
    kategori_total[kategori] += jumlah

print("📊 Pengeluaran Per Kategori :")
for kategori,jumlah in kategori_total.items():
    print(f"- {kategori} : Rp.{jumlah}")













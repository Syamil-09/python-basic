print("                                         MATERI 5 - PYTHON BEGINNER")
print("MEMBAHAS TENTANG LOOPING")
# for loop (index di mulai dari 0 sampai seterusnya)
# di balik layar range (0,1,2,3,4)
for angka in range(0, 5):
    print("Hallo Syamil Ke-", angka)
    print("SEMANGAT!!!")
# di bawah ini tidak masuk blok kode for karena diluar scope nya
print("-- SELESAI --")

# for loop pada string/text
wiffiJoglo = "hsijoglo"
for huruf in wiffiJoglo:
    print(huruf, "-->")

rentangNomor = range(0, 11)
for no in rentangNomor:
    print("*" * no)
print("--- SELESAI LAGI ---")

# while loop (selalu di jalankan sampai kondisi terpenuhi)
num = 1
while (num < 6):
    print("Jalan Terus:", num)
    num += 1
print("--------")
num = 6
while (num > 1):
    print("Jalan Terus:", num)
    num -= 1
# tekan ctrl+c kalau looping terus berjalan untuk mematikn proses
print("-- SELESAI LAGI DONG --")

# contoh flowchart cek umur
print("-- MULAI --")
cekUmur = int(input("Berapa umur anda?"))
# seluruh input() dari user 
# 
if (cekUmur > 18):
    print("Boleh bikin SIM C")
elif (cekUmur > 15):
    print("Sebentar lagi Ya Deck!!!")
else:
    print("Masih Bocil FF gk Boleh!!!")

print("-- SELESAI --")

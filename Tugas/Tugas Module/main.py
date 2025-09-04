import doa_harian
import hitung_uang
import rangking

doa_harian.doa_tidur()
doa_harian.doa_bangun()
doa_harian.doa_makan()


jajan = [50000, 30000, 15000, 70000, 10000]
print(hitung_uang.tambah_bonus(jajan))
uang_lebih = hitung_uang.filter_boros(jajan)
print(uang_lebih)


nilai = [75, 90, 60, 88, 100, 55]
print(rangking.ururtan_nilai(nilai))
print(rangking.tinggi(nilai))
print(rangking.rendah(nilai))



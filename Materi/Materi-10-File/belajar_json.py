import json
print("------- READ JSON FILE -------")
file_json_path = r"\Users\HNLaptop\Desktop\PYHTON\Materi-10-File\rukun_islam.json"
# With ... as -> agar file otomatis ter close
with open(file_json_path, 'r') as file_rukun_islam:
    # baca data dengan fungsi load() dari module json
    data_json = json.load(file_rukun_islam)
    print(f"Judul : {data_json['judul']}")
    print(f"Jumlah Rukun : {data_json['jumlah']}")
    print(f"Jumlah Sholat Sunnah : {data_json['sholat_sunnah']}")
    print(f"Status Kawin : {data_json['status_kawin']}")
    print(f"Status Jomblo : {data_json['status_jomblo']}")
    print(f"Info Halaman : {data_json['info']['halaman']}")
    print(f"Info Rating : {data_json['info']['rating']}")
    print(f"Info Riwayat Versi 1 : {data_json['info']['riwayat']['versi1']}")
    print(f"Info Riwayat Versi 2 : {data_json['info']['riwayat']['versi2']}")
    print(f" : {data_json['status_jomblo']}")
    
    for item in data_json['rukun']:
        print(f"-> {item}")

# akses manual array of object dengan key index
print(f"Surah ke-1 : {data_json['surah'][0]['nama']}")

# buat garis dengan dikalikan angka
print("-" * 50)
print("| No | Nama Surah | Jumlah Ayat | Lokasi Turun |")
print("-" * 50)
# tampilkan ke bentuk table garis sederhana
# keys: no, ayat, nama, turun
for item_surah in data_json['surah']:
    print(f"| {item_surah['no']} | {item_surah['ayat']} | {item_surah['nama']} | {item_surah['turun']} |")

print("--- PROSES BACA FILE JSON SELESAI ---")

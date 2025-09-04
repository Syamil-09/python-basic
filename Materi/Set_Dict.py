print("                                        MATERI 7 - PYTHON DATA STRUCTURE")
print(" ")
                 ###   Set -> {} -> tidak berurutan, berubah, tidak duplikat   ###
game_hanif = {"ff", "pou", "ff"}         
game_syamil = {"mlbb", "coc", "ff"}
print("Hanif Game :", game_hanif)
print("Syamil Game :", game_syamil)

# .add() -> menambahkan item baru
game_syamil.add("pubg")
game_syamil.add("mlbb") # tidak akan bertambah 
game_hanif.add("efootball")
game_syamil.add("class royal")

# .remove() -> menghapus item
game_hanif.remove("pou")
game_syamil.remove("coc")

# len() -> menghitung jumah item
print("Hanif ada", len(game_hanif),"games :", game_hanif)
print("Syamil ada", len(game_syamil),"games :", game_syamil)

# .union() -> menggabungkan 2 set berbeda
game_berdua = game_hanif.union(game_syamil)
total_game = len(game_berdua)
print("Semua game ada", total_game,"game :", game_berdua)

# intersection() -> mencari item yang kembar/sama
game_kembar = game_hanif.intersection(game_syamil)
total_kembar = len(game_kembar)
print("Game yang kembar ada", total_kembar,"game :", game_kembar)

# difference() -> mencari item yang berdeda
game_beda = game_syamil.difference(game_hanif) # jika -> game_beda = game_hanif.difference(game_syamil)
total_beda = len(game_beda)                    # maka yang beda hanya game "ff" saja
print("Game yang beda ada", total_beda,"game :", game_beda)


                 ###   Dict (dictionary) -> {key:value} / {kunci:isinya}   ###
# berurutan berdasarkan key, berubah
# key tidak boleh duplikat
koleksi_anime = {
    "re_zero": "subaru",
    "wind_breaker": "sakura",
    "onePiece": "usop",
    "onePiece": "luffy",   # jika ada key yg sama dlm satu struktur maka komputer akan pilih yg terakhir
    "waifu": {
        "re_zero": "rem-chan",   # tidak masalah key sama kalau struktur beda
        "demon_slayer": "nezuko",
    }
}
print("Koleksi Anime :", koleksi_anime)
print("MC One Piece :", koleksi_anime["onePiece"])
print("Waifu Re Zero :", koleksi_anime["waifu"]["re_zero"])

# menambah / mengubah data dict
koleksi_anime["naruto"] = "sasuke"
koleksi_anime["onePice"] = "zoro"
koleksi_anime["waifu"]["re_zero"] = "rem kanan"
print("Koleksi Anime Sekarang :", koleksi_anime)
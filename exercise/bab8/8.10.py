def kirim_pesan(daftar_pesan, pesan_terkirim): 
    """Menampilkan setiap pesan dan memindahkannya ke daftar terkirim."""
    while daftar_pesan: 
        pesan_sekarang = daftar_pesan.pop(0) 
        print(pesan_sekarang) 
        pesan_terkirim.append(pesan_sekarang) 
 
daftar_teks = ["Halo!", "Apa kabar?", "Sampai jumpa besok."] 
pesan_terkirim = [] 
 
kirim_pesan(daftar_teks, pesan_terkirim) 
 
print("\nDaftar pesan asli:", daftar_teks) 
print("Daftar pesan terkirim:", pesan_terkirim)
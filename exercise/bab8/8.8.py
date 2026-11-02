def buat_album(artis, judul, jumlah_lagu=None): 
    # Mengembalikan dictionary informasi album musik.
    album = { 'artis': artis, 'judul': judul } 
    if jumlah_lagu is not None: 
        album['jumlah_lagu'] = jumlah_lagu 
    return album 
 
while True: 
    print("\nMasukkan informasi album (ketik 'tidak ada' untuk keluar).") 
 
    artis = input("Nama artis: ") 
    if artis.lower() == 'tidak ada': 
        break 
 
    judul = input("Judul album: ") 
    if judul.lower() == 'tidak ada': 
        break 
 
    print(buat_album(artis, judul))
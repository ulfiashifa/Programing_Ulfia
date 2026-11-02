def buat_album(artis, judul, jumlah_lagu=None):
    """Mengembalikan dictionary yang menjelaskan album musik."""
    album = {'artis': artis, 'judul': judul}

    if jumlah_lagu is not None:
        album['jumlah_lagu'] = jumlah_lagu
    return album


print(buat_album("Queen", "A Night at the Opera"))
print(buat_album("Adele", "21"))
print(buat_album("Coldplay", "Parachutes", jumlah_lagu=10))
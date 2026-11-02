pengguna_saat_ini = ['Admin', 'Zee', 'Halwa', 'Raina', 'Vinka'] 
pengguna_baru = ['Nabilah', 'Halwa', 'Tasa', 'Vania', 'Zee'] 
 
pengguna_saat_ini_kecil = [pengguna.lower() for pengguna in pengguna_saat_ini] 
 
for nama_baru in pengguna_baru: 
    if nama_baru.lower() in pengguna_saat_ini_kecil: 
        print(f"{nama_baru}: kamu harus memasukkan nama pengguna baru.") 
    else: 
        print(f"{nama_baru}: nama pengguna ini tersedia.") 
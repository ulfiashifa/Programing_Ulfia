daftar_pengguna = ['admin', 'zee', 'halwa', 'raina', 'vinka'] 
 
for nama_pengguna in daftar_pengguna: 
    if nama_pengguna == 'admin': 
        print("Halo admin, apakah kamu ingin melihat laporan status?") 
    else: 
        print(f"Halo {nama_pengguna}, terima kasih sudah masuk kembali.")
def buat_profil(nama_depan, nama_belakang, **informasi_pengguna): 
    """Membuat dictionary yang berisi informasi pengguna."""
    informasi_pengguna['nama depan'] = nama_depan 
    informasi_pengguna['nama belakang'] = nama_belakang 
    return informasi_pengguna 
 
profil_saya = buat_profil( 'Ulfia', 'Shifa', 
                          lokasi='Salatiga',
                          bidang='teknik', 
                          hobi='berlari' )  
print(profil_saya) 
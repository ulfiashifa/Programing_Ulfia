orang_1 = { 
    'nama_depan': 'Edelyn', 
    'nama_belakang': 'Ayesha', 
    'usia': 19, 
    'kota': 'Maluku', 
} 
 
orang_2 = { 
    'nama_depan': 'Alyssa', 
    'nama_belakang': 'Wulandari', 
    'usia': 18, 
    'kota': 'Batam', 
} 
 
orang_3 = { 
    'nama_depan': 'Niky', 
    'nama_belakang': 'Saputra', 
    'usia': 27, 
    'kota': 'Jakarta', 
} 
 
daftar_orang = [orang_1, orang_2, orang_3] 
 
for orang in daftar_orang: 
    print( 
        f"{orang['nama_depan']} {orang['nama_belakang']}, " 
        f"berusia {orang['usia']} tahun, tinggal di {orang['kota']}." 
    ) 
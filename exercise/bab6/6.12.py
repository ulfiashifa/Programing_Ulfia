orang_1 = { 
    'nama_depan': 'Niky', 
    'nama_belakang': 'Saputra', 
    'usia': 27, 
    'kota': 'Jakarta', 
    'hobi': 'menyanyi', 
} 
 
orang_2 = { 
    'nama_depan': 'Alyssa', 
    'nama_belakang': 'Wulandari', 
    'usia': 18, 
    'kota': 'Batam', 
    'hobi': 'menonton film', 
} 
 
daftar_orang = [orang_1, orang_2] 
 
for orang in daftar_orang: 
    nama_lengkap = f"{orang['nama_depan']} {orang['nama_belakang']}" 
 
    print(f"\n{nama_lengkap}") 
    print(f"    Usia:  {orang['usia']}") 
    print(f"    Kota:  {orang['kota']}") 
    print(f"    Hobi:  {orang['hobi']}") 
tempat_favorit = { 
    'edelyn': ['Bali', 'Bromo'], 
    'alyssa': ['Yogyakarta', 'Lombok', 'Raja Ampat'], 
    'niky': ['Bandung'], 
} 
 
for nama, daftar_tempat in tempat_favorit.items(): 
    print(f"\nTempat favorit {nama.title()} adalah:") 
 
    for tempat in daftar_tempat: 
        print(f"    {tempat}")
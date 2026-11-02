angka_favorit = { 
    'edelyn': [7, 11], 
    'garnish': [14], 
    'Alyssa': [3, 8, 21], 
    'Niky': [21, 5], 
    'Mario': [9, 1], 
} 
 
for nama, daftar_angka in angka_favorit.items(): 
    print(f"\nAngka favorit {nama.title()} adalah:") 
 
    for angka in daftar_angka: 
        print(f"    {angka}") 
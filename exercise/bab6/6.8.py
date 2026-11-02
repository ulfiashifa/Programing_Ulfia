hewan_1 = {'jenis hewan': 'kucing', 'pemilik': 'Edelyn'} 
hewan_2 = {'jenis hewan': 'anjing', 'pemilik': 'Niky'} 
hewan_3 = {'jenis hewan': 'burung', 'pemilik': 'Alyssa'} 
 
daftar_hewan = [hewan_1, hewan_2, hewan_3] 
 
for hewan in daftar_hewan: 
    print("Hewan peliharaan:") 
    for kunci, nilai in hewan.items(): 
        print(f"    {kunci}: {nilai}") 
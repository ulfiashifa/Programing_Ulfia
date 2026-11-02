sungai = { 
    'kapuas': 'indonesia', 
    'mississippi': 'amerika serikat', 
    'amazon': 'brasil', 
} 
 
for nama_sungai, negara in sungai.items(): 
    print(f"Sungai {nama_sungai.title()} mengalir melalui {negara.title()}.") 
 
print("\nNama sungai dalam kamus:") 
for nama_sungai in sungai.keys(): 
    print(nama_sungai.title()) 
 
print("\nNama negara dalam kamus:") 
for negara in sungai.values(): 
    print(negara.title()) 
kota = { 
    'surakarta': { 
        'negara': 'indonesia', 
        'populasi': 520000, 
        'fakta': 'negara yang sedang mengalami nilai mata uang yang rendah.', 
    }, 
    'tokyo': { 
        'negara': 'jepang', 
        'populasi': 14000000, 
        'fakta': 'salah satu kawasan metropolitan terbesar di dunia.', 
    }, 
    'paris': { 
        'negara': 'prancis', 
        'populasi': 2100000, 
        'fakta': 'merupakan lokasi Menara Eiffel.', 
    }, 
} 
 
for nama_kota, informasi in kota.items(): 
    print(f"\n{nama_kota.title()}:") 
    print(f"    Negara: {informasi['negara'].title()}") 
    print(f"    Populasi: {informasi['populasi']:,}") 
    print(f"    Fakta: {informasi['fakta']}")
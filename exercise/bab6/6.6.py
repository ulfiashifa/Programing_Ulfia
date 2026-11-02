bahasa_favorit = {
    'fathir': 'python',
    'rakha': 'c',
    'edelyn': 'rust',
    'sheila': 'python',
}

daftar_orang = ['fathir', 'rakha', 'edelyn', 'sheila', 'ivan']

for nama in daftar_orang:
    if nama in bahasa_favorit:
        print(f"Terima kasih sudah mengisi survei, {nama.title()}!")
    else:
        print(f"{nama.title()}, silakan isi survei!")
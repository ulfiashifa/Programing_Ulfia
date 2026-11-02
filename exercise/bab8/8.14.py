def buat_mobil(pabrikan, model, **opsi): 
    """Mengembalikan dictionary yang menjelaskan mobil."""
    mobil = { 'pabrikan': pabrikan, 'model': model } 
    mobil.update(opsi) 
    return mobil 
 
mobil_saya = buat_mobil( 'subaru', 'outback', warna='biru', paket_derek=True ) 
 
print(mobil_saya)
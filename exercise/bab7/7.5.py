prompt = "\nBerapa usia Anda? (masukkan 'selesai' untuk keluar): " 
 
while True: 
    usia = input(prompt) 
 
    if usia == 'selesai': 
        break 
 
    usia = int(usia) 
 
    if usia < 3: 
        print("Tiket Anda gratis.") 
    elif usia <= 12: 
        print("Harga tiket Anda Rp10.000.") 
    else: 
        print("Harga tiket Anda Rp15.000.")
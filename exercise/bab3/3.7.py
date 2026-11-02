tamu = ["Dilla", "Nadia", "Amel"] 
print(f"Selamat pagi, {tamu[0]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 
print(f"Selamat pagi, {tamu[1]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 
print(f"Selamat pagi, {tamu[2]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 

# Satu tamu tidak bisa hadir 
print(f"\n{tamu[2]} tidak bisa datang untuk makan malam.")

# Ganti dengan tamu baru 
tamu[2] = "Najwa" 
print("\nDaftar undangan terbaru:") 
print(f"Selamat pagi, {tamu[0]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 
print(f"Selamat pagi, {tamu[1]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 
print(f"Selamat pagi, {tamu[2]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 

# Mendapatkan meja kosong lagi 
print("\nTernyata aku mendapatkan meja kosong lagi, aku ingin mengajak lebih banyak teman.") 
# Menambahkan tamu baru 
tamu.insert(0, "Kayla")       
tamu.insert(2, "Sabina")     
tamu.append("Khansa")        

# Menampilkan semua undangan terbaru 
print("\nDaftar undangan makan malam:") 
print(f"Selamat pagi, {tamu[0]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 
print(f"Selamat pagi, {tamu[1]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 
print(f"Selamat pagi, {tamu[2]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 
print(f"Selamat pagi, {tamu[3]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 
print(f"Selamat pagi, {tamu[4]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 
print(f"Selamat pagi, {tamu[5]}! Aku ingin mengajak kalian makan malam hari ini, di cafe pojok jalan itu.") 

# Meja baru tidak datang tepat waktu 
print("\nMaaf, meja baruku tidak akan datang tepat waktu. Aku hanya bisa mengundang dua orang.") 
# Mengatur urutan agar Nadia dan Dilla tetap diundang 
tamu = ["Kayla", "Sabina", "Najwa", "Khansa", "Nadia", "Dilla"] 

# Hapus tamu satu per satu dengan pop() sampai tersisa dua 
removed = tamu.pop() 
print(f"Maaf {removed}, aku tidak bisa mengundangmu untuk makan malam.") 
removed = tamu.pop() 
print(f"Maaf {removed}, aku tidak bisa mengundangmu untuk makan malam.") 
removed = tamu.pop() 
print(f"Maaf {removed}, aku tidak bisa mengundangmu untuk makan malam.") 
removed = tamu.pop() 
print(f"Maaf {removed}, aku tidak bisa mengundangmu untuk makan malam.") 

# Dua tamu yang tersisa tetap diundang 
print(f"\nHai, {tamu[0]}! Kamu tetap diundang untuk makan malam.") 
print(f"Hai, {tamu[1]}! Kamu tetap diundang untuk makan malam.") 
# Kosongkan list menggunakan del 
del tamu[0] 
del tamu[0] 
# Tampilkan list kosong 
print(tamu) 
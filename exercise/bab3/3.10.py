gunung = ["Rinjani", "Semeru", "Merapi"] 

# Mengakses elemen lewat indeks 
print(gunung[0]) 
print(gunung[-1]) 

# Mengubah elemen 
gunung[1] = "Bromo" 

# append(): tambah di akhir 
gunung.append("Kerinci") 

# insert(): sisipkan di posisi tertentu 
gunung.insert(1, "Merbabu")
 
# len(): jumlah elemen 
print(f"Jumlah gunung: {len(gunung)}")
 
# sorted(): urut sementara 
print(sorted(gunung)) 
print(sorted(gunung, reverse=True)) 
print(gunung) 

# reverse(): balik urutan permanen 
gunung.reverse() 
print(gunung) 

# sort(): urut permanen 
gunung.sort() 
print(gunung) 
gunung.sort(reverse=True) 
print(gunung) 

# pop(): hapus elemen terakhir dan simpan nilainya 
gunung_terakhir = gunung.pop() 
print(f"Dihapus: {gunung_terakhir}")
 
# pop(indeks): hapus elemen di posisi tertentu 
gunung_kedua = gunung.pop(1) 
print(f"Dihapus: {gunung_kedua}") 

# remove(): hapus berdasarkan nilai 
gunung.remove("Rinjani") 

# del: hapus berdasarkan indeks 
del gunung[0] 
print(gunung)
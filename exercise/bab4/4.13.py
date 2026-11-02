# Membuat menu makanan 
makanan = ("nasi", "ayam goreng", "mi", "sup", "salad") 
# Menampilkan menu makanan 
for menu in makanan: 
    print(menu) 
 
# Mencoba mengubah item (akan error jika dijalankan) 
# makanan[0] = "roti" 
 
# Mengganti menu dengan membuat tuple baru 
makanan = ("nasi", "ikan bakar", "mi", "sup", "buah") 
 
print("\nMenu yang telah diperbarui:") 
for menu in makanan: 
    print(menu)
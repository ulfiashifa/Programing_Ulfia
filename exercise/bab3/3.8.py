tempat = ["Jepang", "Korea Selatan", "Swiss", "New Zealand", "Arab Saudi"] 
# 1. Urutan asli 
print("Urutan asli:") 
print(tempat) 

# 2. diurutkan berdasarkan abjad, daftar asli tidak berubah 
print("\ndiurutkan berdasarkan abjad:") 
print(sorted(tempat)) 

# 3. Buktikan daftar asli masih sama 
print("\nDaftar asli masih sama:") 
print(tempat) 

# 4. diurutkan berdasarkan abjad terbalik, daftar asli tidak berubah 
print("\ndiurutkan berdasarkan abjad terbalik:") 
print(sorted(tempat, reverse=True))
 
# 5. Buktikan lagi daftar asli masih sama 
print("\nDaftar asli masih sama:") 
print(tempat) 

# 6. Urutan terbalik untuk mengubah daftar asli 
tempat.reverse() 
print("\nSetelah urutan terbalik: ") 
print(tempat) 

# 7. urutan terbalik lagi, kembali ke urutan awal 
tempat.reverse() 
print("\nSetelah urutan terbalik kedua:") 
print(tempat)
 
# 8. diurutkan berdasarkan abjad, mengubah daftar asli 
tempat.sort() 
print("\nSetelah diurutkan:") 
print(tempat) 

# 9. diurutkan berdasarkan abjad terbalik, mengubah daftar asli 
tempat.sort(reverse=True) 
print("\nSetelah diurutkan berdasarkan abjad terbalik:") 
print(tempat)
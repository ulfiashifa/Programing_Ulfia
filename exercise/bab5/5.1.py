# Kesetaraan dan ketidaksetaraan string 
mobil = 'subaru' 
 
print("Apakah mobil == 'subaru'? Saya memprediksi Benar.") 
print(mobil == 'subaru') 
 
print("\nApakah mobil == 'audi'? Saya memprediksi Salah.") 
print(mobil == 'audi') 
 
print("\nApakah mobil != 'audi'? Saya memprediksi Benar.") 
print(mobil != 'audi') 
 
print("\nApakah mobil != 'subaru'? Saya memprediksi Salah.") 
print(mobil != 'subaru') 
 
# Metode lower() 
print("\nApakah mobil== 'subaru'? Saya memprediksi Benar.") 
print(mobil.lower() == 'subaru') 
 
nama = 'Subaru' 
 
print("\nApakah nama == 'subaru'? Saya memprediksi Salah.") 
print(nama == 'subaru') 
 
print("\nApakah nama == 'subaru'? Saya memprediksi Benar.") 
print(nama.lower() == 'subaru') 
 
# Pengujian numerik 
usia = 20 
 
print("\nApakah usia == 20? Saya memprediksi Benar.") 
print(usia == 20) 

print("\nApakah usia != 20? Saya memprediksi Salah.") 
print(usia != 20) 

print("\nApakah usia > 18? Saya memprediksi Benar.") 
print(usia > 18) 

print("\nApakah usia < 18? Saya memprediksi Salah.") 
print(usia < 18) 

print("\nApakah usia >= 20? Saya memprediksi Benar.") 
print(usia >= 20) 

print("\nApakah usia <= 19? Saya memprediksi Salah.") 
print(usia <= 19) 

# Penggunaan and dan or 
print("\nApakah usia > 18 dan usia < 30? Saya memprediksi Benar.") 
print(usia > 18 and usia < 30) 

print("\nApakah usia > 25 dan usia < 30? Saya memprediksi Salah.") 
print(usia > 25 and usia < 30) 

print("\nApakah usia < 18 atau usia == 20? Saya memprediksi Benar.") 
print(usia < 18 or usia == 20) 

print("\nApakah usia < 18 atau usia > 30? Saya memprediksi Salah.") 
print(usia < 18 or usia > 30) 

# Penggunaan in dan not in 
daftar_mobil = ['subaru', 'audi', 'toyota'] 
print("\nApakah 'audi' ada dalam daftar mobil? Saya memprediksi Benar.") 
print('audi' in daftar_mobil) 

print("\nApakah 'bmw' ada dalam daftar mobil? Saya memprediksi Salah.") 
print('bmw' in daftar_mobil) 

print("\nApakah 'bmw' tidak ada dalam daftar mobil? Saya memprediksi Benar.") 
print('bmw' not in daftar_mobil) 

print("\nApakah 'audi' tidak ada dalam daftar mobil? Saya memprediksi Salah.") 
print('audi' not in daftar_mobil) 
bilangan_kubik = [] 
for nomor in range(1, 11): 
    bilangan_kubik.append(nomor ** 3) 
    
for kubik in bilangan_kubik: 
    print(kubik) 
bilangan_kubik = [nomor ** 3 for nomor in range(1, 11)] 

print("Tiga angka pertama dalam daftar adalah:") 
print(bilangan_kubik[:3]) 

print("Tiga angka dari bagian tengah daftar adalah:") 
print(bilangan_kubik[3:6]) 

print("Tiga angka terakhir dalam daftar adalah:") 
print(bilangan_kubik[-3:]) 
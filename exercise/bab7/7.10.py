jawaban = {} 
 
survei_aktif = True 
 
while survei_aktif: 
    nama = input("\nSiapa nama Anda? ") 
    tempat = input( "Jika bisa mengunjungi satu tempat di dunia, " "ke mana Anda ingin pergi? " ) 
 
    jawaban[nama] = tempat 
 
    ulangi = input("Apakah ada orang lain yang ingin menjawab? (ya/tidak) ") 
 
    if ulangi.lower() == 'tidak': 
        survei_aktif = False 
 
print("\n--- Hasil Survei ---") 
for nama, tempat in jawaban.items(): 
    print(f"{nama.title()} ingin mengunjungi {tempat.title()}.")
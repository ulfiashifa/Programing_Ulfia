#while 
prompt = "\nMasukkan topping pizza (atau 'selesai' untuk mengakhiri): " 
 
topping = "" 
while topping != 'selesai': 
    topping = input(prompt) 
    if topping != 'selesai': 
        print(f"Saya akan menambahkan {topping} ke pizza Anda.") 
 
#var aktif  
prompt = "\nMasukkan topping pizza (atau 'selesai' untuk mengakhiri): " 
 
aktif = True 
while aktif: 
    topping = input(prompt) 
 
    if topping == 'selesai': 
        aktif = False 
    else: 
        print(f"Saya akan menambahkan {topping} ke pizza Anda.") 
        
#break 
prompt = "\nMasukkan topping pizza (atau 'selesai' untuk mengakhiri): " 
 
while True: 
    topping = input(prompt) 
    if topping == 'selesai': 
        break 
 
    print(f"Saya akan menambahkan {topping} ke pizza Anda.")
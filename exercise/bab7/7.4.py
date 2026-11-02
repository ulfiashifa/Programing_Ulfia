prompt = "\nMasukkan topping pizza (atau 'selesai' untuk mengakhiri): " 
 
topping = "" 
while topping != 'selesai': 
    topping = input(prompt) 
 
    if topping != 'selesai': 
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")
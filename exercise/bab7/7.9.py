pesanan_sandwich = [ 
    'pastrami', 'tuna', 'pastrami', 'ham', 
    'sayuran', 'pastrami', 'ayam' 
] 
sandwich_selesai = [] 
 
print("Maaf, toko sandwich kehabisan pastrami.") 
 
while 'pastrami' in pesanan_sandwich: 
    pesanan_sandwich.remove('pastrami') 
 
while pesanan_sandwich: 
    sandwich_sekarang = pesanan_sandwich.pop() 
    print(f"Saya telah membuat sandwich {sandwich_sekarang}.") 
    sandwich_selesai.append(sandwich_sekarang) 
 
print("\nSemua sandwich yang telah dibuat:") 
for sandwich in sandwich_selesai: 
    print(sandwich)
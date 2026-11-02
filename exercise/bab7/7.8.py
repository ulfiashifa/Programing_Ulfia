pesanan_sandwich = ['tuna', 'ham', 'sayuran', 'ayam'] 
sandwich_selesai = [] 
 
while pesanan_sandwich: 
    sandwich_sekarang = pesanan_sandwich.pop() 
    print(f"Saya telah membuat sandwich {sandwich_sekarang}.") 
    sandwich_selesai.append(sandwich_sekarang) 
 
print("\nSemua sandwich yang telah dibuat:") 
for sandwich in sandwich_selesai: 
    print(sandwich) 
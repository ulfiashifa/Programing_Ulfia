def buat_sandwich(*isian): 
    """Menampilkan daftar isian sandwich yang dipesan."""
    print("\nMembuat sandwich dengan isian:") 
 
    for bahan in isian: 
        print(f"    - {bahan}") 
 
buat_sandwich("ham") 
buat_sandwich("tuna", "selada") 
buat_sandwich("ayam", "keju", "tomat", "bawang") 
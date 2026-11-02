from random import choice

kumpulan = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

tiket_pemenang = []
while len(tiket_pemenang) < 4:
    terambil = choice(kumpulan)
    if terambil not in tiket_pemenang:
        tiket_pemenang.append(terambil)

print("Tiket yang cocok dengan 4 angka atau huruf ini memenangkan hadiah:")
print(tiket_pemenang)
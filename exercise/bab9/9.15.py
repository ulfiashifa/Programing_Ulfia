from random import choice

kumpulan = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
tiket_saya = [3, 'b', 8, 'e']


def tarik_tiket(kumpulan):
    """Kembalikan 4 item acak yang berbeda dari kumpulan."""
    tiket = []
    while len(tiket) < 4:
        terambil = choice(kumpulan)
        if terambil not in tiket:
            tiket.append(terambil)
    return tiket


percobaan = 0
while True:
    percobaan += 1
    tiket_pemenang = tarik_tiket(kumpulan)
    if set(tiket_pemenang) == set(tiket_saya):
        break

print(f"Butuh {percobaan} percobaan untuk menang.")
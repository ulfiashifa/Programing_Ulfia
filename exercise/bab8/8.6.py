def kota_negara(kota, negara): 
    """Mengembalikan teks berisi nama kota dan negara."""
    return f"{kota.title()}, {negara.title()}" 
 
print(kota_negara("bangkok", "vietnam")) 
print(kota_negara("salatiga", "indonesia")) 
print(kota_negara("tokyo", "jepang"))
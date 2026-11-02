class Mobil:
    """Model sederhana sebuah mobil."""

    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun


class Baterai:
    """Model sederhana baterai mobil listrik."""

    def __init__(self, ukuran_baterai=40):
        self.ukuran_baterai = ukuran_baterai

    def dapatkan_jarak(self):
        if self.ukuran_baterai == 40:
            jarak_km = 150
        elif self.ukuran_baterai == 65:
            jarak_km = 225
        else:
            jarak_km = 0
        print(f"Mobil ini bisa menempuh sekitar {jarak_km} km "
              f"dengan baterai penuh.")

    def tingkatkan_baterai(self):
        if self.ukuran_baterai != 65:
            self.ukuran_baterai = 65


class MobilListrik(Mobil):
    """Mobil yang berjalan dengan baterai."""

    def __init__(self, merek, model, tahun):
        super().__init__(merek, model, tahun)
        self.baterai = Baterai()


mobil_saya = MobilListrik("nissan", "leaf", 2024)

mobil_saya.baterai.dapatkan_jarak()
mobil_saya.baterai.tingkatkan_baterai()
mobil_saya.baterai.dapatkan_jarak()
class Restoran:
    """Model sederhana sebuah restoran."""

    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.jumlah_dilayani = 0

    def deskripsikan_restoran(self):
        print(f"{self.nama_restoran} menyajikan masakan {self.jenis_masakan}.")

    def buka_restoran(self):
        print(f"{self.nama_restoran} sedang buka!")

    def atur_jumlah_dilayani(self, jumlah):
        self.jumlah_dilayani = jumlah

    def tambah_jumlah_dilayani(self, jumlah):
        self.jumlah_dilayani += jumlah


restoran = Restoran("McDonalds", "Fastfood")

print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")

restoran.jumlah_dilayani = 20
print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")

restoran.atur_jumlah_dilayani(35)
print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")

restoran.tambah_jumlah_dilayani(120)
print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")
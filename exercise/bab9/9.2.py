class Restoran:
    """Model sederhana sebuah restoran."""

    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"{self.nama_restoran} menyajikan masakan {self.jenis_masakan}.")

    def buka_restoran(self):
        print(f"{self.nama_restoran} sedang buka!")


restoran_1 = Restoran("Warung Solo", "Jawa")
restoran_2 = Restoran("Sushi Tei", "Jepang")
restoran_3 = Restoran("Luigi's", "Italia")

restoran_1.deskripsikan_restoran()
restoran_2.deskripsikan_restoran()
restoran_3.deskripsikan_restoran()
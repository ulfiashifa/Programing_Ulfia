class Restoran:
    """Model sederhana sebuah restoran."""

    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"{self.nama_restoran} menyajikan masakan dengan jenis {self.jenis_masakan}.")

    def buka_restoran(self):
        print(f"{self.nama_restoran} sedang buka!")


restoran = Restoran("McDonald's", "Fast Food")

print(restoran.nama_restoran)
print(restoran.jenis_masakan)

restoran.deskripsikan_restoran()
restoran.buka_restoran()
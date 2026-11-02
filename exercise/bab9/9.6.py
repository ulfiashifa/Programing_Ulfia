class Restoran:
    """Model sederhana sebuah restoran."""

    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"{self.nama_restoran} menyajikan {self.jenis_masakan}.")


class KiosEsKrim(Restoran):
    """Jenis restoran khusus yang menjual es krim."""

    def __init__(self, nama_restoran, jenis_masakan="es krim"):
        super().__init__(nama_restoran, jenis_masakan)
        self.daftar_rasa = ["vanila", "cokelat", "stroberi"]

    def tampilkan_rasa(self):
        print("Kami punya rasa berikut:")
        for rasa in self.daftar_rasa:
            print(f"    - {rasa}")


kios = KiosEsKrim("Es Krim Tianlala")
kios.deskripsikan_restoran()
kios.tampilkan_rasa()
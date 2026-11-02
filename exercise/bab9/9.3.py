class Pengguna:
    """Model sederhana profil pengguna."""

    def __init__(self, nama_depan, nama_belakang, umur, kota):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.kota = kota

    def deskripsikan_pengguna(self):
        print(f"{self.nama_depan} {self.nama_belakang}, "
              f"berumur {self.umur} tahun, dari {self.kota}.")

    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan}! Selamat datang kembali.")


pengguna_1 = Pengguna("Edelyyn", "Laos", 19, "Maluku Utara")
pengguna_2 = Pengguna("Alyssa", "Wulandari", 19, "Batam")
pengguna_3 = Pengguna("Niky", "Saputra", 27, "Jakarta")

for pengguna in (pengguna_1, pengguna_2, pengguna_3):
    pengguna.deskripsikan_pengguna()
    pengguna.sapa_pengguna()
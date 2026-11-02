class Pengguna:
    """Model sederhana profil pengguna."""

    def __init__(self, nama_depan, nama_belakang, umur, kota):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.kota = kota
        self.percobaan_login = 0

    def deskripsikan_pengguna(self):
        print(f"{self.nama_depan} {self.nama_belakang}, "
              f"berumur {self.umur} tahun, dari {self.kota}.")

    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan}! Selamat datang kembali.")

    def tambah_percobaan_login(self):
        self.percobaan_login += 1

    def reset_percobaan_login(self):
        self.percobaan_login = 0


pengguna = Pengguna("Ulfia", "Shifa", 18, "Salatiga")

pengguna.tambah_percobaan_login()
pengguna.tambah_percobaan_login()
pengguna.tambah_percobaan_login()
print(pengguna.percobaan_login)

pengguna.reset_percobaan_login()
print(pengguna.percobaan_login)
from modul_9_12 import Pengguna


class HakAkses:
    """Hak akses seorang administrator."""

    def __init__(self):
        self.hak_akses = ["boleh menambah postingan",
                          "boleh menghapus postingan",
                          "boleh memblokir pengguna"]

    def tampilkan_hak_akses(self):
        print("Hak akses administrator:")
        for hak in self.hak_akses:
            print(f"    - {hak}")


class Admin(Pengguna):
    """Pengguna dengan hak akses administrator."""

    def __init__(self, nama_depan, nama_belakang):
        super().__init__(nama_depan, nama_belakang)
        self.hak_akses = HakAkses()
# 1. import nama_modul
import modul_8_16
print(modul_8_16.kota_negara("santiago", "chile"))

# 2. from nama_modul import nama_fungsi
from modul_8_16 import kota_negara
print(kota_negara("tokyo", "japan"))

# 3. from nama_modul import nama_fungsi as alias
from modul_8_16 import kota_negara as kn
print(kn("paris", "france"))

# 4. import nama_modul as alias
import modul_8_16 as mm
print(mm.kota_negara("surakarta", "indonesia"))

# 5. from nama_modul import *
from modul_8_16 import *
print(kota_negara("cairo", "egypt"))
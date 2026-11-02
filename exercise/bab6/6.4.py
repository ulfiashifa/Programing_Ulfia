glosarium = { 
    'variabel': 'nama yang digunakan untuk menyimpan suatu nilai.', 
    'string': 'kumpulan karakter yang ditulis di dalam tanda kutip.', 
    'list': 'kumpulan elemen yang memiliki urutan.', 
    'perulangan': 'kode yang menjalankan kembali sekumpulan perintah.', 
    'tuple': 'kumpulan elemen yang tidak dapat diubah secara langsung.', 
    'dictionary': 'kumpulan pasangan kunci dan nilai.', 
    'komentar': 'catatan dalam kode yang diabaikan oleh Python.', 
    'indeks': 'posisi suatu elemen dalam sebuah list.', 
    'boolean': 'tipe nilai yang hanya memiliki nilai True atau False.', 
    'irisan': 'bagian tertentu dari sebuah list.', 
} 
 
for istilah, arti in glosarium.items(): 
    print(f"{istilah.title()}:\n    {arti}\n") 
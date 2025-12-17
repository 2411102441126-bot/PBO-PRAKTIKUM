class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status_pinjam = False  

    def tampilkan_info(self):
        status = "Dipinjam" if self.status_pinjam else "Tersedia"
        print(f"Judul       : {self.judul}")
        print(f"Penulis     : {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Status      : {status}")
        print("-" * 40)

    def pinjam_buku(self):
        if not self.status_pinjam:
            self.status_pinjam = True
            print(f"Buku '{self.judul}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.judul}' sedang tidak tersedia.")

    def kembalikan_buku(self):
        if self.status_pinjam:
            self.status_pinjam = False
            print(f"Buku '{self.judul}' telah dikembalikan.")
        else:
            print(f"Buku '{self.judul}' memang belum dipinjam.")


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' berhasil ditambahkan ke perpustakaan.")

    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku di perpustakaan.")
        else:
            print("\n=== Daftar Buku di Perpustakaan ===")
            for buku in self.daftar_buku:
                buku.tampilkan_info()


# ----------------- Contoh Penggunaan -----------------

# Buat perpustakaan
perpus = Perpustakaan()

# Tambah buku
buku1 = Buku("Pemrograman Python", "Guido van Rossum", 2010)
buku2 = Buku("Algoritma dan Struktur Data", "Donald Knuth", 2005)
buku3 = Buku("Kecerdasan Buatan", "John McCarthy", 2018)

perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.tambah_buku(buku3)

# Tampilkan semua buku
perpus.tampilkan_semua_buku()

# Pinjam buku
buku1.pinjam_buku()
buku1.pinjam_buku()  # coba pinjam lagi

# Kembalikan buku
buku1.kembalikan_buku()
buku1.kembalikan_buku()  # coba kembalikan lagi

# Tampilkan ulang daftar buku
perpus.tampilkan_semua_buku()

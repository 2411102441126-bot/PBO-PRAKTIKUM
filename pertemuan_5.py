# PARENT CLASS
class Bentuk:
    def gambar(self):
        raise NotImplementedError("Subclass harus mengimplementasikan method ini!")

 # CHILD CLASS 1   
class Persegi(Bentuk):
    def gambar(self):
        print("Menggambar Persegi: [][][][]")

# CHILD CLASS 2
class Lingkaran(Bentuk):
    def gambar(self):
        print("Menggambar Lingkaran oooooo")

# --- Bagian Utama Proram ---
daftar_bentuk = [Persegi(), Lingkaran(), Persegi(), Lingkaran()]

print("--- Memanggil method yang sama pada objek yang berbeda ---")
for bentuk in daftar_bentuk:
    bentuk.gambar()

# CHILD CLASS 3
class Segitiga(Bentuk):
    def gambar(self):
        print("Menggambar Segitiga: /\\")

# CLASS YANG TIDAK BERHUBUNGAN (untuk Duck Typing)
class Teks:
    def gambar(self):
        print("Menulis Teks: 'Hello, Polmorphism!'")

def render_objek(objek_untuk_digambar):
    print("Mencoba me-render objek...")
    objek_untuk_digambar.gambar()

persegi = Persegi()
lingkaran = Lingkaran()
segitiga = Segitiga()
teks_biasa = Teks()

print("\n--- Menggunakan fungsi polimorfik ---")
render_objek(persegi)
render_objek(lingkaran)
render_objek(segitiga)

print("\n--- Demonstrasi Duck Typing ---")
render_objek(teks_biasa)


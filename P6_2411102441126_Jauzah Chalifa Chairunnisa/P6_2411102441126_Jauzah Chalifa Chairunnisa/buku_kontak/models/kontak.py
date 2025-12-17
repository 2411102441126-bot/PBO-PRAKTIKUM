# File: buku_kontak/models/kontak.py

class Kontak:
    """
    Class Kontak untuk merepresentasikan data kontak (nama dan nomor telepon).
    """
    
    # 2. b. Constructor __init__ menerima nama dan nomor_telepon
    def __init__(self, nama, nomor_telepon):
        # 2. c. Semua atribut harus bersifat privat (menggunakan konvensi __)
        self.__nama = nama
        self.__nomor_telepon = nomor_telepon
    
    # --- Getter dan Setter (Optional, sebagai latihan tambahan) ---
    
    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    # Getter untuk nomor_telepon
    def get_nomor_telepon(self):
        return self.__nomor_telepon

    # Setter untuk nomor_telepon
    def set_nomor_telepon(self, nomor_baru):
        self.__nomor_telepon = nomor_baru

    # 2. d. Buat method tampilkan_info()
    def tampilkan_info(self):
        print("--- Info Kontak ---")
        print(f"Nama: {self.__nama}")
        print(f"No. Telp: {self.__nomor_telepon}")
        print("-------------------")
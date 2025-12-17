

from models.kontak import Kontak

if __name__ == "__main__":
    
    daftar_kontak = []
    
    print("APLIKASI BUKU KONTAK SEDERHANA")
    print("==============================\n")
    
    kontak1 = Kontak("Jule", "087835025118")
    kontak2 = Kontak("Icha ", "085651982833")
    kontak3 = Kontak("Diah ", "081347046499")
    
    # Masukkan ketiga objek tersebut ke dalam daftar_kontak
    daftar_kontak.append(kontak1)
    daftar_kontak.append(kontak2)
    daftar_kontak.append(kontak3)
    
    print(f"Total {len(daftar_kontak)} kontak telah ditambahkan.\n")
    

    
    for kontak in daftar_kontak:
        kontak.tampilkan_info()

    print("--- Update Kontak 1 ---")
    kontak1.set_nama("Budi Santoso (Baru)")
    kontak1.set_nomor_telepon("08111222333")
    kontak1.tampilkan_info()
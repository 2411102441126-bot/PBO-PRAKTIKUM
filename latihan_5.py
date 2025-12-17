from abc import ABC, abstractmethod

# Parent Class abstrak
class Notifikasi(ABC):
    @abstractmethod
    def kirim(self, pesan):
        raise NotImplementedError("Method ini harus dioverride oleh subclass")

# Child Class: Email
class Email(Notifikasi):
    def kirim(self, pesan):
        print(f"[EMAIL] Mengirim: '{pesan}'")

# Child Class: SMS
class SMS(Notifikasi):
    def kirim(self, pesan):
        print(f"[SMS] Mengirim: '{pesan}'")

# Child Class: Push Notification
class PushNotif(Notifikasi):
    def kirim(self, pesan):
        print(f"[PUSH] Mengirim: '{pesan}'")

# Bagian utama program
if __name__ == "__main__":
    daftar_notifikasi = [Email(), SMS(), PushNotif()]
    for notif in daftar_notifikasi:
        notif.kirim("Diskon Spesial! Hanya untuk Anda!")


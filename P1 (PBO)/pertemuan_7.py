import os
from datetime import datetime

class FileAnalyzer:
    def __init__(self, file_path):
        self.__file_path = file_path

        if os.path.exists(file_path):
            self.__file_ada = True
            self.__file_size = os.path.getsize(file_path)
        else:
            self.__file_ada = False
            print(f"Error: File '{file_path}' tidak ditemukan.")

    def get_file_size(self, unit="bytes"):
        if not self.__file_ada:
            return None
        if unit.lower() == "kb":
            return self.__file_size / 1024
        return self.__file_size

    def get_modification_time(self):
        if not self.__file_ada:
            return None
        mod_time = os.path.getmtime(self.__file_path)
        waktu_terformat = datetime.fromtimestamp(mod_time)
        return waktu_terformat.strftime("%d %B %Y, %H:%M:%S")

    def analyze(self):
        print("\n=== Hasil Analisis File ===")
        print(f"Nama File : {self.__file_path}")

        if not self.__file_ada:
            print("Status    : File tidak ditemukan. Analisis dibatalkan.")
            return

        ukuran_kb = self.get_file_size("KB")
        waktu_modifikasi = self.get_modification_time()

        print("Status    : File ditemukan")
        print(f"Ukuran    : {ukuran_kb:.2f} KB")
        print(f"Terakhir diubah : {waktu_modifikasi}")
        print("============================\n")

analyzer1 = FileAnalyzer("dokumen.txt")
analyzer1.analyze()

analyzer2 = FileAnalyzer("file_khayalan.txt")
analyzer2.analyze()

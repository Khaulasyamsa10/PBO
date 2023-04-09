class Komputer:
  
    def __init__(self, merk, procesor, ukuran_layar):
        self.__merk = merk
        self.__procesor = procesor
        self.__ukuran_layar = ukuran_layar

    def menghidupkan(self):
        print(f"Saya menghidupkan komputer {self.__merk} dengan procesor {self.__procesor} dengan ukuran {self.__ukuran_layar}")

    def mematikan(self):
        print(f"Saya mematikan komputer {self.__merk} dengan procesor {self.__procesor} dengan ukuran {self.__ukuran_layar}")

# Method Getter
    def get_merk(self):
        return self.__merk

    def get_procesor(self):
        return self.__procesor

    def get_ukuran_layar(self):
        return self.__ukuran_layar

# Method Setter
    def set_merk(self, merk):
        self.__merk = merk

    def set_procesor(self, procesor):
        self.__procesor = procesor

    def set_ukuran_layar(self, ukuran_layar):
        self.__ukuran_layar = ukuran_layar

# Objek baru
komputer_4 = Komputer("HP", "Intel", "sedang")

# Mengakses variabel private menggunakan method getter
print("Merk:", komputer_4.get_merk())  
print("Procesor:", komputer_4.get_procesor())  
print("Ukuran Layar:", komputer_4.get_ukuran_layar())  

# Mengubah nilai variabel private menggunakan method setter
komputer_4.set_merk("Dell")
komputer_4.set_procesor("AMD")
komputer_4.set_ukuran_layar("besar")

# Mengakses nilai variabel private yang telah diubah menggunakan method getter
print("Merk (setelah diubah):", komputer_4.get_merk())  
print("Procesor (setelah diubah):", komputer_4.get_procesor())  
print("Ukuran Layar (setelah diubah):", komputer_4.get_ukuran_layar())  

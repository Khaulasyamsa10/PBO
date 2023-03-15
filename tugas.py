class komputer:
  
    def __init__(self, merk, procesor, ukuran_layar):
        self.merk = merk
        self.procesor = procesor
        self.ukuran_layar = ukuran_layar

    def menghidupkan (self):
        print(f"saya menghidupkan komputer {self.merk} dengan procesor {self.procesor} dengan ukuran {self.ukuran_layar} ")

    def mematikan (self):
        print(f"saya mematikan komputer {self.merk} dengan procesor {self.procesor} dengan ukuran {self.ukuran_layar} ")

komputer_1 = komputer("Lenovo", "Intel", "mini")
komputer_2 = komputer("Asus", "AMD", "super komputer")
komputer_3 = komputer("Acer", "Apple", "Komputer main frame")

komputer_1.menghidupkan()
komputer_2.mematikan()
komputer_3.menghidupkan()
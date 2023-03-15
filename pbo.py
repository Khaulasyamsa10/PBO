class Mahasiswa():
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan
    def get_info(self):
        print(f" Nama        : {self.nama} ")
        print(f" Umur        : {self.umur} ")
        print(f" Jurusan     : {self.jurusan} ")

    def set_nama(self, nama_baru):
        self.nama = nama_baru

    def set_umur(self, umur_baru):
        self.umur = umur_baru

mahasiswa1 = Mahasiswa("syamsa", 19, "Pendidikan Teknik Informatika")
mahasiswa2 = Mahasiswa("chanyeol", 18, "Pendidikan Teknik Informatika")

    
mahasiswa1.set_nama("syamsa")
mahasiswa1.set_umur("19")
mahasiswa1.get_info()
print()
mahasiswa2.set_nama("chanyeol")
mahasiswa2.set_umur("18")
mahasiswa2.get_info()
print()
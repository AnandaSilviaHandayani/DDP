class manusia:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def cetak(self):
        print("nama saya adalah", self.fname, self.lname)
        
class staff (manusia):
    def bekerja (self):
        print("saya pekerja keras")
        
class pelajar(manusia):
    def __init__(self, fname, lname, prodi, angkatan):
        super().__init__(fname, lname)
        self.prodi = prodi
        self.angkatan = angkatan
        
    def cetak(self):
        super().cetak()
        print("saya mahasiswa angkatan", self.angkatan, "prodi",self.prodi)
        
    def belajar(self):
        print("saya adalah pelajar")
#objek manusia
x = manusia ("nada", "indah")
x.cetak()

#objek staff
y = staff("dedi", "drajat")
y.cetak()
y.bekerja()

#objek pelajar
danu = pelajar("danu", "setiawan", "sistem informasi", 2023)
danu.cetak()
danu.belajar()
        
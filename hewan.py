class animal:
    def __init__(self, name, makanan, hidup, berkembangBiak ) -> None:
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
        
    def cetak(self):
        print("saya adalah", self.name)
        print("makanan saya", self.makanan)
        print("saya hidup di", self.hidup)
        print("dan berkembang biak dengan", self.berkembangBiak)
        

class badak(animal):
    def __init__(self, name, makanan, hidup, berkembangBiak, bergerak, bernafas):
        super().__init__(name, makanan, hidup, berkembangBiak)
        self.bergerak = bergerak
        self.bernafas = bernafas
        
    def print(self):
        print("saya adalah", self.name)
        print("makanan saya", self.makanan)
        print("saya hidup di", self.hidup)
        print("dan berkembang biak dengan", self.berkembangBiak)
        print("bergerak dengan cara", self.bergerak)
        print("bernafas menggunakan", self.bernafas)
        
class ikan(animal):
    def __init__(self, name, makanan, hidup, berkembangBiak, bergerak, bernafas):
        super().__init__(name, makanan, hidup, berkembangBiak)
        self.bergerak = bergerak
        self.bernafas = bernafas
        
    def print(self):
        print("saya adalah", self.name)
        print("makanan saya", self.makanan)
        print("saya hidup di", self.hidup)
        print("dan berkembang biak dengan", self.berkembangBiak)
        print("bergerak dengan cara", self.bergerak)
        print("bernafas menggunakan", self.bernafas)
        
class ular(animal):
    def __init__(self, name, makanan, hidup, berkembangBiak, bergerak, bernafas):
        super().__init__(name, makanan, hidup, berkembangBiak)
        self.bergerak = bergerak
        self.bernafas = bernafas
        
    def print(self):
        print("saya adalah", self.name)
        print("makanan saya", self.makanan)
        print("saya hidup di", self.hidup)
        print("dan berkembang biak dengan", self.berkembangBiak)
        print("bergerak dengan cara", self.bergerak)
        print("bernafas menggunakan", self.bernafas)
        
#objek animal
x = animal ("Badak", "tumbuhan", "daratan", "melahirkan")
x.cetak()


#objek badak
bdk = badak ("badak", "tumbuhan", "daratan", "melahirkan", "berjalan", "paru-paru")
bdk.print()

#objek ikan
ikn = ikan ("ikan", "daging", "air", "bertelur", "berenang", "insang")
ikn.print()

#objek ular
ulr = ular ("ular", "daging", "daratan", "bertelur", "melata", "kulit")
ulr.print()

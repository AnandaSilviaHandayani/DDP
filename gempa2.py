class Gempa :
    lokasi =''
    skala = 0
    
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    def dampak(self, skala):
        if self.skala < 2:
            print('Gempa tidak berasa')
        elif 2 <= self.skala <= 4:
            print('Gempa berdambak banguan retak')
        elif 4 <= self.skala <= 6:
            print('Gempa berdampak roboh')
        elif self.skala > 6:
            print('Gempa besar berdampak tsunami')
            
        print('Lokasi Gempa:', self.lokasi)
        print('skala gempa:', self.skala)
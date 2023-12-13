from gempa2 import *

gempa1 = Gempa('Banten',1.2)
gempa2 = Gempa('Palu',6.1)
gempa3 = Gempa('Cianjur',5.6)
gempa4 = Gempa('Jayapura',3.3)
gempa5 = Gempa('Garut',4.0)

print('===Gempa Bumi Info===')
print()
gempa1.dampak(1.2)
gempa2.dampak(6.1)
gempa3.dampak(5.6)
gempa4.dampak(3.3)
gempa5.dampak(4.0)

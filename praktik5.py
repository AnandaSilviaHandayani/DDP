# NO1
kendaraan = ["motor","beat",250,"hitam",2]
print(kendaraan)

kendaraan = ["motor","beat",250,"hitam",2]
kendaraan.append("22 juta")
print(kendaraan)
  
kendaraan = ["motor","beat",250,"hitam",2]
kendaraan.append("22 juta")
kendaraan.append("matic")  
print(kendaraan)         

kendaraan = ["motor","beat",250,"hitam",2]
kendaraan.append("22 juta")
kendaraan.append("matic")           
kendaraan.insert(2,"honda")
print(kendaraan)


# # NO2
print("""selamat datang kamu masuk di aplikasi penghitung luas bangun datar
 masukan pilihan :
 1. untuk menghitung luas persegi
 2. untuk menghitung luas lingkaran
 3. untuk menghitung luas segitiga
 """)
pilihan = int(input("masukan pilihan kamu"))

match pilihan :
     case 1 : 
         print("kamu memilih 1 untuk menghitung luas persegi") 
         sisi = int(input("masukan sisi?"))
         luasP= sisi * sisi
         print("luas persegi yang sisinya adalah",luasP)
          
     case 2 :
         print("kamu memilih 2 untuk menghitung luas lingkaran")
         R = int(input("masukan jari-jari"))
         luasL= 3.14 * R * R
         print("luas lingkarang yang jari-jarinya", R, "adalah", int(luasL))
         
     case 3 :
         print("kamu memilih 3 untuk menghitung luas segitiga")
         alas = int(input("masukan alas"))
         tinggi = int(input("masukan tinggi"))
         Lsegitiga= 0.5 * alas * tinggi
         print("luas segitiga yang adalah", int(Lsegitiga))
         
     case _: 
         print("kamu salah masukan pilihan")

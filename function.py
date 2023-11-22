print("")
print("=====No 1=====")
print("")
def profil(nama,alamat, gender, umur, hoby) :
    print("nama saya adalah", nama)
    print("alamat saya di", alamat)
    print("saya adalah seorang", gender)
    print("umur saya", umur)
    print("hoby saya adalah", hoby)
    
profil("ananda silvia", "Depok", "perempuan", "19 Tahun", "membaca")

print("")
print("=====No 2=====")
print("")
def cetaknilai (nilai) :
    if nilai <=60 :
        print("gagal")
    elif nilai >60 and nilai <=70 :
        print("baik")
    elif nilai >71 and nilai <=80 :
        print("sangat baik")
    elif nilai >81 and nilai <=100 :
        print("istimewa")
    else :
        print("nilai tidak ada")
        
cetaknilai(60)

print("")
print("=====No 3=====")
print("")
def bilganjil(ganjil) :
    for i in range(ganjil) :
        if(i %2 !=0):
            print(i, end=" ")
            
bilganjil(100)
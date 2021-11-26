#Membuat 2 buah fungsi untuk menghitung bilangan yang dipangkatkan dan menghitung nilai dari bilangan yang diakarkan.
#Mencetak menu program untuk menghitung bilangan yang dipangkatkan dan diakarkan
print("Menu Program yang tersedia")
#Mencetak fungsi 1 (PangkatAngka)
print("1. pangkatkan angka")
#Mencetak fungsi 2 (AkarDua)
print("2. akarkan bilangan")

#Memasukkan input pada Menu pilihan 
Menupilihan = float(input("Masukkan pilihan yang diinginkan :"))
#Menupilihan nomer 1 ("Pangkatkan Angka")
if Menupilihan == 1:
    #Mencetak "Masukkan angka yang ingin dipangkatkan"
    print("Masukkan angka yang ingin di Pangkatkan :")
    a1 = float(input("Angka :"))
    #Mencetak "Ingin memodifikasi pangkat ? (yes/no)"
    print ("Ingin memodifikasi pangkat ? (yes/no) ")
    a2 = str(input(":"))
    #Jika Menupilihan 1 bernilai "yes"
    if a2 == "yes":
        #np = Nilai Pangkat
        np = int(input("Masukkan nilai pangkat :"))
        #Rumus mencari pangkat
        Hasil = (a1 ** np)
        #Mencetak hasil dari pangkat
        print ("Hasil dari" ,a1 ,"^" ,np ,"=" ,Hasil)
    #Jika Menupilihan 1 bernilai "no"
    elif a2 == "no" :
        Hasil = (a1 ** 2)
        print ("Hasil dari" ,a1 ,"^2" ,"=" ,Hasil)
#Menupilihan nomer 2 ("Akarkan Bilangan")
elif Menupilihan == 2:
    #Mencetak "Masukkan angka yang ingin di akar"
    print("Masukkan angka yang ingin di akar")
    b1 = float(input("Angka :"))
    #Mencetak "Ingin memodifikasi akar ? (yes/no)"
    print ("Ingin memodifikasi akar ? (yes/no) ")
    b2 = str(input(":"))
    #Jika Menupilihan 2 bernilai "yes"
    if b2 == "yes":
        na = int(input("Masukkan nilai akar :"))
        #Rumus mencari akar pangkat
        Hasil = b1 ** (1.0/na)
        #Mencetak hasil dari akar pangkat
        print ("Hasil akar pangkat" ,na ,"dari" ,b1 ,"=" ,round(Hasil ,2))
    #Jika Menupilihan 2 bernilai "no"
    elif b2 == "no":
        Hasil = b1 ** (1.0/2)
        print ("Hasil akar pangkat 2" ,"dari" ,b1 ,"=" ,round(Hasil ,2))

        
        
    
        
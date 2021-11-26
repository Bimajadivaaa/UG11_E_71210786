#Membuat 3 buah fungsi yang memiliki kegunaan yang berbeda
print ("=======Program Manipulasi String=======")
#Mencetak Pilihan Menu
print ("Pilihan Menu :")
#Mencetak fungsi Hitung Kata
print ("1. Hitung kata")
#Mencetak fungsi Cek Kata
print ("2. cek kata")
#Mencetak fungsi Ubah Kata
print ("3. ubah kata")

menupilihan = input("Pilihan anda :")
kalimat = input("Masukkan sebuah kalimat/kata :")
kesimpulan = (kalimat.lower())
#Membuat menupilihan 1 
if menupilihan == "1":
    q1 = input("Masukkan kata yang ingin dihitung :")
    q2 = kesimpulan.count(q1)
    #Mencetak hasil hitung kata
    print("Terdapat sebanyak" ,q2 ,"kata" ,q1, "didalam string")
#Membuat menupilihan 2
elif menupilihan == "2":
    w1 = input("Masukkan kata yang ingin di cek : ")
    w2 = w1.upper()
    Hasilakhir = kesimpulan.replace(w1,w2)
#Jika tidak terdapat sebuah string
    if w2 not in Hasilakhir:
        #Mencetak "Jika kata tidak terdapat dalam string"
        print("Kata" ,w1 ,"tidak terdapat di dalam string")
        #Mencetak kata yang ingin di cek
        print (Hasilakhir, w1)
    else:
    #Mencetak "Jika kata terdapat dalam string"
        print("Kata" ,w1 ,"terdapat di dalam string")
        print("String diubah menjadi :")
        #Mencetak kata yang ingin di cek
        print(Hasilakhir)
#Membuat menupilihan 3
elif menupilihan == "3":
    e1 = input("Masukkan kata yang ingin diubah :")
    e2 = input("Masukkan kata pengganti :")
    print("Anda akan mengubah kata" ,e1 ,"menjadi" ,e2 ,"sebanyak 1x")
    gantikata = input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) :")
    #Jika ingin mengganti kata
    if gantikata == ("yes"):
        r1 = int(input("Masukkan jumlah total penggantian :"))
        #Mencetak string berhasil diubah
        print("String berhasil diubah menjadi :")
        r2 = kesimpulan.replace(e1 ,e2 ,r1)
        print(r2)
    #Jika tidak ingin mengganti kata
    elif gantikata == ("no"):
        t1 = 1
        print ("String berhasil diubah menjadi :")
        t2 = kesimpulan.replace(e1 ,e2 ,t1)
        print(t2)
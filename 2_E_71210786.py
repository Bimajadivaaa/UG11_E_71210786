#Membuat fungsi yang dapat mencetak huruf tengah pada sebuah kata.
##terdapat satu parameter yang ingin di cetak.
##Jika kalimat berisi 5 huruf maka akan di cetak 3 parameter.
##jika huruf yang berjumlah genap dan gajil pengambilan nilai tengah akan berbeda dan banyaknya huruf yang diambil juga dipengaruhi oleh banyaknya huruf pada kata tersebut.
#Membuat fungsi Huruf tengah.
## HT = Huruf Tengah
def HT_kalimat():
    #Fungsi len digunakan untuk mengetahui panjang kalimat
    N=len(kalimat)//2
    ##Operator % menandakan Sisa Bagi
    if (len(kalimat)%2==0) and ((len(kalimat)/2)%2==0):
        ##Fungsi return berguna untuk mengembalikan nilai
        return kalimat[(N)//2 : ((N)//2)*-1]
    elif (len(kalimat)%2==0) and ((len(kalimat)/2)%2!=0):
        return kalimat[((N)//2)+1 : (((N)//2)+1)*-1]
    else:
        return kalimat[(((N)+1)//2) : (((N)+1)//2)*-1]
#Menambahkan string
kalimat= str(input("Masukkan kata :"))
#Mencetak huruf tengah pada kata yang terdapat di sebuah kalimat
print("Huruf tengah pada kata" ,kalimat ,"adalah" ,HT_kalimat())
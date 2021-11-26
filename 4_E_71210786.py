#Membuat tiga operasi secara random
#Membuat Pertanyaan random 
import random
#OPERASI PENJUMLAHAN, PENGURANGAN, PEMBAGIAN, DAN PERKALIAN
operasi = ['+','-','/','*']
def LihatHasil(Opsi):
    hasil = 0
    hasilsalah = False
    SOAL = ""
    #Membuat OPSI 1
    if Opsi == "1":
        a1 = random.randint(20, 50)
        a2 = random.randint(20, 50)
        c  = random.choice(operasi)
        SOAL = f"{a1} {c} {a2}"
        print("Berapakah hasil dari ", a1, c, a2)
        if c== '-':
            jawaban = a1 - a2
        elif c == '+':
            jawaban = a1 + a2
        elif c == '/':
            jawaban = a1 / a2
        elif c == '*':
            jawaban = a1 * a2
    #Membuat OPSI 2
    elif Opsi == "2":
        a1 = random.randint(20, 70)
        a2 = random.randint(20, 70)
        a3 = random.randint(20, 70)
        c1 = random.choice(operasi)
        c2 = random.choice(operasi)
        SOAL = f"{a1} {c1} {a2} {c2} {a3}"
        print("Berapakah hasil dari ", a1, c1, a2, c2, a3)
        if c1 == '-':
            if c2 == '/':
                jawaban = a1 - a2 / a3
            elif c2 == '*':
                jawaban = a1 - a2 * a3
            elif c2 == '-':
                jawaban = a1 - a2 - a3
            elif c2 == '+':
                jawaban = a1 - a2 + a3
        elif c1 == '+':
            if c2 == '-':
                jawaban = a1 + a2 - a3
            elif c2 == '+':
                jawaban = a1 + a2 + a3
            elif c2 == '/':
                jawaban = a1 + a2 / a3
            elif c2 == '*':
                jawaban = a1 + a2 * a3
        elif c1 == '/':
            if c2 == '-':
                jawaban = a1 / a2 - a3
            elif c2 == '+':
                jawaban = a1 / a2 + a3
            elif c2 == '/':
                jawaban = a1 / a2 / a3
            elif c2 == '*':
                jawaban = a1 / a2 * a3
        elif c1 == '*':
            if c2 == '-':
                jawaban = a1 * a2 - a3
            elif c2 == '+':
                jawaban = a1 * a2 + a3
            elif c2 == '/':
                jawaban = a1 * a2 / a3
            elif c2 == '*':
                jawaban = a1 * a2 * a3
    #Membuat OPSI 3
    elif Opsi == "3":
        a1 = random.randint(20, 100)
        a2 = random.randint(20, 100)
        a3 = random.randint(20, 100)
        a4 = random.randint(20, 100)
        c1 = random.choice(operasi)
        c2 = random.choice(operasi)
        c3 = random.choice(operasi)
        stringsoal = f"{a1} {c1} {a2} {c2} {a3} {c3} {a4}"
        print("Berapakah hasil dari ", a1, c1, a2, c2, a3, c3, a4)
        if c1 == '-':
            if c2 == '-':
                if c2 == '-':
                    jawaban = a1 - a2 - a3 - a4
                elif c2 == '+':
                    jawaban = a1 - a2 - a3 + a4
                elif c2 == '/':
                    jawaban = a1 - a2 - a3 / a4
                elif c2 == '*':
                    jawaban = a1 - a2 - a3 * a4
            elif c2 == '+':
                if c2 == '-':
                    jawaban = a1 - a2 + a3 - a4
                elif c2 == '+':
                    jawaban = a1 - a2 + a3 + a4
                elif c2 == '/':
                    jawaban = a1 - a2 + a3 / a4
                elif c2 == '*':
                    jawaban = a1 - a2 + a3 * a4
            elif c2 == '/':
                if c2 == '-':
                    jawaban = a1 - a2 / a3 - a4
                elif c2 == '+':
                    jawaban = a1 - a2 / a3 + a4
                elif c2 == '/':
                    jawaban = a1 - a2 / a3 / a4
                elif c2 == '*':
                    jawaban = a1 - a2 / a3 * a4
            elif c2 == '*':
                if c2 == '-':
                    jawaban = a1 - a2 * a3 - a4
                elif c2 == '+':
                    jawaban = a1 - a2 * a3 + a4
                elif c2 == '/':
                    jawaban = a1 - a2 * a3 / a4
                elif c2 == '*':
                    jawaban = a1 - a2 * a3 * a4
        elif c1 == '+':
            if c2 == '-':
                if c2 == '-':
                    jawaban = a1 + a2 - a3 - a4
                elif c2 == '+':
                    jawaban = a1 + a2 - a3 + a4
                elif c2 == '/':
                    jawaban = a1 + a2 - a3 / a4
                elif c2 == '*':
                    jawaban = a1 + a2 - a3 * a4
            elif c2 == '+':
                if c2 == '-':
                    jawaban = a1 + a2 + a3 - a4
                elif c2 == '+':
                    jawaban = a1 + a2 + a3 + a4
                elif c2 == '/':
                    jawaban = a1 + a2 + a3 / a4
                elif c2 == '*':
                    jawaban = a1 + a2 + a3 * a4
            elif c2 == '/':
                if c2 == '-':
                    jawaban = a1 + a2 / a3 - a4
                elif c2 == '+':
                    jawaban = a1 + a2 / a3 + a4
                elif c2 == '/':
                    jawaban = a1 + a2 / a3 / a4
                elif c2 == '*':
                    jawaban = a1 + a2 / a3 * a4
            elif c2 == '*':
                if c2 == '-':
                    jawaban = a1 + a2 * a3 - a4
                elif c2 == '+':
                    jawaban = a1 + a2 * a3 + a4
                elif c2 == '/':
                    jawaban = a1 + a2 * a3 / a4
                elif c2 == '*':
                    jawaban = a1 + a2 * a3 * a4
        elif c1 == '+':
            if c2 == '-':
                if c2 == '-':
                    jawaban = a1 + a2 - a3 - a4
                elif c2 == '+':
                    jawaban = a1 + a2 - a3 + a4
                elif c2 == '/':
                    jawaban = a1 + a2 - a3 / a4
                elif c2 == '*':
                    jawaban = a1 + a2 - a3 * a4
            elif c2 == '+':
                if c2 == '-':
                    jawaban = a1 + a2 + a3 - a4
                elif c2 == '+':
                    jawaban = a1 + a2 + a3 + a4
                elif c2 == '/':
                    jawaban = a1 + a2 + a3 / a4
                elif c2 == '*':
                    jawaban = a1 + a2 + a3 * a4
            elif c2 == '/':
                if c2 == '-':
                    jawaban = a1 / a2 / a3 - a4
                elif c2 == '+':
                    jawaban = a1 / a2 / a3 + a4
                elif c2 == '/':
                    jawaban = a1 / a2 / a3 / a4
                elif c2 == '*':
                    jawaban = a1 / a2 / a3 * a4
            elif c2 == '*':
                if c2 == '-':
                    jawaban = a1 / a2 * a3 - a4
                elif c2 == '+':
                    jawaban = a1 / a2 * a3 + a4
                elif c2 == '/':
                    jawaban = a1 / a2 * a3 / a4
                elif c2 == '*':
                    jawaban = a1 / a2 * a3 * a4
        elif c1 == '*':
            if c2 == '-':
                if c2 == '-':
                    jawaban = a1 * a2 - a3 - a4
                elif c2 == '+':
                    jawaban = a1 * a2 - a3 + a4
                elif c2 == '/':
                    jawaban = a1 * a2 - a3 / a4
                elif c2 == '*':
                    jawaban = a1 * a2 - a3 * a4
            elif c2 == '+':
                if c2 == '-':
                    jawaban = a1 * a2 + a3 - a4
                elif c2 == '+':
                    jawaban = a1 * a2 + a3 + a4
                elif c2 == '/':
                    jawaban = a1 * a2 + a3 / a4
                elif c2 == '*':
                    jawaban = a1 * a2 + a3 * a4
            elif c2 == '/':
                if c2 == '-':
                    jawaban = a1 * a2 / a3 - a4
                elif c2 == '+':
                    jawaban = a1 * a2 / a3 + a4
                elif c2 == '/':
                    jawaban = a1 * a2 / a3 / a4
                elif c2 == '*':
                    jawaban = a1 * a2 / a3 * a4
            elif c2 == '*':
                if c2 == '-':
                    jawaban = a1 * a2 * a3 - a4
                elif c2 == '+':
                    jawaban = a1 * a2 * a3 + a4
                elif c2 == '/':
                    jawaban = a1 * a2 * a3 / a4
                elif c2 == '*':
                    jawaban = a1 * a2 * a3 * a4
    else:
        #Mencetak jika inputan salah
        print("inputan salah")
        hasilsalah= True
    if not hasilsalah:
        hasiljawab = float(input("Masukkan jawaban anda: "))
        if (jawaban == hasiljawab or hasiljawab == ("%.3f" % jawaban)):
            #Mencetak jawaban jika benar
            print("Jawaban anda benar !")
        else:
            #Mencetak jawaban jika salah
            print("Jawaban Anda Masih Salah")
            print("Hasil dari ",SOAL, " = %.3f" % jawaban)
#Mencetak Program test aritmatika dasar
print("======Program test aritmatika dasar======")
#Mencetak Pilihan level program
print("Pilihan level yang tersedia :")
#Terdapat 3 level dalam program yaitu Easy,Medium, dan Hard.
print("1. Easy")
print("2. Medium")
print("3. Hard")
#Memasukan tingkatan yang ingin dicoba
opsimenu=str(input("Masukkan tingkatan yang ingin anda coba :"))
#Melihat hasil 
LihatHasil(opsimenu)







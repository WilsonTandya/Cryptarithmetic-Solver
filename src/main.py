import time
import os

#Membaca file
nama_file = input("Masukkan nama file: ")
if os.name=='nt':
    file_path = os.path.join("..\\test", nama_file)
else:
    file_path = os.path.join("test", nama_file)
f = open(file_path, "r")

#Memulai perhitungan waktu
start = time.time()

#Membersihkan tanda + dan - dari file
A=f.read().replace("+","").replace("-","").split('\n')

#Menampilkan soal
print("Input dari file:")
for k in range(len(A)):
    if (k == len(A)-3):
        print(A[k],"+")
    elif (k == len(A)-2):
        print("------")
    else:
        print(A[k])
print("")

#Membuang blank pada soal
for kata in range (len(A)):
    A[kata]=A[kata].strip()

#Mencari seluruh kemunculan alfabet unik
unique_letters = []
for word in A:
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)

#Fungsi untuk membangkitkan permutasi dari panjang alfabet unik
def permutasi(length):
    elements = list('0123456789')
    if length == 0:
        return []
    elif length == 1:
        return [[ele] for ele in elements]
    output = []
    for p in permutasi(length-1):
        for ele in elements:
            if ele not in p:
                output.append(p + [ele])
    return output

#Fungsi mengubah kata ke angka dari susunan permutasi 
def kataToAngka(kata, unique_letters, p):
    for j in range (len(unique_letters)):
        kata = kata.replace(unique_letters[j], p[j])
    return kata

#Main
count=0
solusi=0
for p in permutasi(len(unique_letters)):
    B = A.copy()
    for i in range(len(B)):
        B[i]=kataToAngka(B[i], unique_letters, p)
    sum=0
    for j in range(len(B)-2):
        #iterasi dilewatkan saat muncul 0 sebagai digit pertama
        if (B[j][0]=="0"):
            continue
        else:
            count+=1
            sum+=(int(B[j]))
            if (sum == int(B[len(B)-1]) and B[len(B)-1][0]!="0"):
                solusi+=1
                #Menampilkan solusi ke-n
                print("Solusi ke -",solusi)
                for k in range(len(B)):
                    if (k == len(B)-3):
                        print(B[k],"+")
                    elif (k == len(B)-2):
                        print("------")
                    else:
                        print(B[k])
                print("")
                
#Pencatatan waktu selesai
end = time.time()
print("Program memiliki", solusi,"solusi")
print("Dibutuhkan", round(end-start, 3), "detik untuk mendapatkan solusi diatas")
print("Jumlah tes yang dilakukan untuk mendapatkan solusi:", count)



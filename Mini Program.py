#ID
#Program ini bertujuan untuk bermain tebak angka dimana permainan yang akan kalian lakukan
#adalah bermain dengan komputer/laptop kalian sendiri. Ada saat giliran Computer menebak
#juga ada giliran kalian menebak.
#Giliran Kalian Menebak, kalian akan menebak angka dari 1-15 yang telah komputer pilih secara random
#jika kalian salah sebanyak 3 kali kalian akan kalah pada giliran tersebut
#Giliran Komputer Menebak, Kalian akan menyiapkan angka yang kalian pilih dari 1-100 dalam hati, nanti komputer
#akan menebak angka kalian, apabila komputer salah menebak sebanyak 7 kali, Komputer akan kalah
#setiap kali salah satu pihak benar menebak maka poin akan ditambahkan, siapapun yang menang sebanyak 3 kali
#dikatakan sebagai pemenang game tersebut, dan jika pemenang sudah ditemukan program berhenti berjalan.

import random
import os


def membersihkan_layar(): #fungsi yang berguna untuk membersihkan layar terminal
    if os.name == 'nt':
        os.system('')
        print('\n')
    else:
        os.system('clear')
        print('\n')


def G_User():
    angka_komputer = random.randint(1,15)
    chance = 1
    while chance <= 3:
        tebakan = int(input("Masukan Tebakan 1-15 : "))
        if tebakan == angka_komputer:
            print("Selamat Anda Benar !!")
            poin["user"] += 1
            input("\nTekan Enter untuk melanjutkan")
            membersihkan_layar()
            break
        elif tebakan < angka_komputer:
            print("Salah!!! Angka Terlalu kecil")
            chance += 1
        elif tebakan > angka_komputer:
            print("Salah!!! Angka Terlalu Besar")
            chance += 1
    else:
        print("Anda Gagal Menebak, Lanjut pada Giliran selanjutnya")
        input("\nTekan Enter untuk melanjutkan")
        membersihkan_layar()


def G_Computer():
    print("Pilihlah Angka antara 1-100, Komputer akan menebaknya")
    b_bawah = 1
    b_atas = 100
    chance = 1
    while chance <= 7:
        tebakan = random.randint(b_bawah, b_atas)
        klu = input(
            f"Apakah Angka {tebakan} terlalu kecil(input = '<'), terlalu besar (input = '>') atau benar (input = 'b')")
        if klu == '<':
            chance += 1
            b_bawah = tebakan+1
        elif klu == '>':
            chance += 1
            b_atas = tebakan-1
        elif klu == 'b':
            print("Komputer Telah Menebak, Terimakasih sudah bermain secara jujur")
            poin["computer"] += 1
            input("\nTekan Enter untuk melanjutkan")
            membersihkan_layar()
            break
    else:
        print("Komputer Gagal Menebak, lanjut pada giliran selanjutnya")
        input("\nTekan Enter untuk melanjutkan")
        membersihkan_layar()


poin = {
    "user": 0,
    "computer": 0
}
while poin["user"] < 3 and poin["computer"] < 3:
    G_User()
    G_Computer()
    print(poin)
else:
    if poin["user"] >= 3:
        print("Selamat anda menang dalam game tebak angka")
    elif poin["computer"] >= 3:
        print("Komputer menang dalam game kali ini, coba lebih baik di kesempatan selanjutnya")
    input("tekan enter untuk keluar")
    membersihkan_layar()

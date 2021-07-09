import csv
import datetime
import random
import os

file_name = "VillaManagement.csv"
data_pengunjung = 'Data Pengunjung.csv'
hari_ini = datetime.date.today()
tanggal = ''
stay = 0
jenis_villa = ''
user_id = ''
pilihan = 0
stay = 0
user_id = ''

def halaman_utama():
    global pilihan
    print(
        "==========VILLA MANAGEMENT==========="
        "\n========= Mikli Oktrarianto ========="
        "\n========== Viqi Rafif S.P. =========="
        "\n" + "_" * 37,
        "\n[1]Pesan Villa"
        "\n[2]Informasi Villa"
        "\n[3]Informasi Ketersediaan"
        "\n[4]Catatan Pemesanan"
        "\n[0]Keluar"
    )
    pilihan = int(input("Masukan Pilihan --> "))
    if pilihan==1:
        info_villa()
        pemesanan()
    elif pilihan==2:
        info_villa()
    elif pilihan==3:
        info_kamar()
    elif pilihan==4:
        catatan_pemesanan()
    elif pilihan==0:
        exit()
    else:
        print("Input Salah")

def pemesanan():
    global tanggal
    global stay
    global jenis_villa
    global user_id
    info_kamar()
    tanggal = input('Masukan Tanggal Check-In : ')
    stay = int(input('Masukan Lama Hari Menginap (Max 5 hari) : '))
    jenis_villa = input("Masukan jenis Villa : ")
    if ("Villa Konohagakure" == jenis_villa):
        total_biaya = 2250000 * stay
        print("Jumlah Harga = Rp", total_biaya)
    elif ("Villa Kirigakure" == jenis_villa):
        total_biaya = 1500000 * stay
        print("Jumlah Harga = Rp", total_biaya)
    elif ("Villa Sunagakure" == jenis_villa):
        total_biaya = 1800000 * stay
        print("Jumlah Harga = Rp", total_biaya)
    user_id = str(random.randint(1000000, 9999999))
    print("Nomor ID Pemesanan anda adalah : ", user_id)
    input('Tekan Enter Untuk Melanjutkan ')
    payment()

def info_kamar():
    data_sementara = []
    print('='*77+
          f"\n|{'Tanggal': ^12}|{'Villa Konohagakure' : ^20}|"
          f"{'Villa Kirigakure' : ^20}|{'Villa Sunagakure' : ^20}|\n"+
          '='*77)
    with open (file_name, 'r') as data_pemesanan:
        data_villa = csv.DictReader(data_pemesanan)
        for info in data_villa:
            data_sementara.append(info)
    area = ['Tanggal', 'Villa Konohagakure', 'Villa Kirigakure', 'Villa Sunagakure']
    if data_sementara[0]['Tanggal'] == str(hari_ini):
        data_sementara.remove(data_sementara[0])
        update = dict()
        update['Tanggal'] = datetime.date.today() + datetime.timedelta(days=15)
        update['Villa Konohagakure'] = 'Available'
        update['Villa Kirigakure'] = 'Available'
        update['Villa Sunagakure'] = 'Available'
        data_sementara.append(update)
    with open(file_name, 'w', newline='') as update_info:
        update = csv.DictWriter(update_info, fieldnames=area)
        update.writeheader()
        update.writerows(data_sementara)

    for info in data_sementara:
        print(f"|{info['Tanggal'] : ^12}|{info['Villa Konohagakure'] : ^20}|"
              f"{info['Villa Kirigakure'] : ^20}|{info['Villa Sunagakure'] : ^20}|")
    if pilihan == 3:
        input("\n Tekan Enter Untuk Kembali ke halaman Utama")
        os.system('cls' if os.name == 'nt' else 'clear')
    return data_sementara

def booked():
    global stay
    data_sementara = list()
    with open(file_name, 'r') as data:
        baca = csv.DictReader(data)
        for info in baca:
            data_sementara.append(info)
    i = 0
    for info in data_sementara:
        if tanggal == info['Tanggal']:
            info[jenis_villa] = 'Booked'
            i = data_sementara.index(info)
            stay += data_sementara.index(info)
    for index in range(i, stay):
        data_sementara[index][jenis_villa] = 'Booked'
    with open(file_name, 'w', newline='') as villa:
        area = ['Tanggal', 'Villa Konohagakure', 'Villa Kirigakure', 'Villa Sunagakure']
        tulis_ulang = csv.DictWriter(villa, fieldnames=area)
        tulis_ulang.writeheader()
        tulis_ulang.writerows(data_sementara)
    info_kamar()
    input('Tekan Enter Untuk Melanjutkan --> ')

def info_villa():
    print(f"\n{'=======Villa Konohagakure=======':^70}")
    print(f"{'Harga Sewa / hari' : <20}: Rp 2.250.000",
          f"\n{'Luas Bangunan': <20}: 720m^2"
          f"\n{'Luas Tanah': <20}: 1000m^2"
          f"\n{'Jumlah Kamar Tidur' : <20}: 5 Kamar",
          f"\n{'Jumlah Kamar Mandi' : <20}: 3 Kamar Mandi",
          f"\n{'Ketarangan' : <20}: Full Furnished",
          f"\n{'Fasilitas' : <20}: Bath-Up, Kolam Renang, Taman, Air-Panas, Dapur, Balkon"
          )
    print(f"\n{'=======Villa Kirigakure=======':^70}")
    print(f"{'Harga Sewa / hari' : <20}: Rp 1.500.000",
          f"\n{'Luas Bangunan': <20}: 640m^2"
          f"\n{'Luas Tanah': <20}: 800m^2"
          f"\n{'Jumlah Kamar Tidur' : <20}: 4 Kamar",
          f"\n{'Jumlah Kamar Mandi' : <20}: 2 Kamar Mandi",
          f"\n{'Ketarangan' : <20}: Full Furnished",
          f"\n{'Fasilitas' : <20}: Kolam Renang, Air Panas Taman, Dapur, Balkon"
          )
    print(f"\n{'=======Villa Sunagakure=======': ^70}")
    print(f"{'Harga Sewa / hari' : <20}: Rp 1.800.000",
          f"\n{'Luas Bangunan': <20}: 640m^2"
          f"\n{'Luas Tanah': <20}: 800m^2"
          f"\n{'Jumlah Kamar Tidur' : <20}: 5 Kamar",
          f"\n{'Jumlah Kamar Mandi' : <20}: 3 Kamar Mandi",
          f"\n{'Ketarangan' : <20}: Full Furnished",
          f"\n{'Fasilitas' : <20}: Bath-Up, Kolam Renang, Air-Panas, Dapur, Balkon"
          )
    input("\nTekan Enter Untuk Melanjutkan ")
    if pilihan == 2:
        os.system('cls' if os.name == 'nt' else 'clear')

def payment():
    print("""
    ========Pilih Jenis Pembayaran==========
    [1] Transfer ATM
    [2] Tunai
    """)

    pengunjung_baru = dict()
    pilih = int(input("\nPilih Metode Pembayaran : "))
    kode_booking = str(random.randint(1000000, 9999999))
    pengunjung_baru['Nama'] = input('Masukkan Nama:')
    pengunjung_baru['NIK'] = input("Masukkan NIK: ")
    pengunjung_baru['Alamat'] = input("Masukkan Alamat Anda: ")
    pengunjung_baru['Email'] = input("Masukkan Email: ")
    pengunjung_baru['Check-in'] = tanggal
    pengunjung_baru['Inap'] = str(stay)+'hari'
    pengunjung_baru['Villa'] = jenis_villa
    pengunjung_baru['ID_Pembayaran'] = kode_booking
    area = ['Nama','NIK','Alamat','Email','Check-in','Inap','Villa','ID_Pembayaran']
    print(pengunjung_baru)
    with open(data_pengunjung, 'a', newline='') as pengunjung:
        data_baru = csv.DictWriter(pengunjung, fieldnames=area)
        data_baru.writerow(pengunjung_baru)

    if pilih == 1:
        cek_id = input('Masukkan Nomer ID Pemesanan : ')
        while True:  # cek id dapat dari mikli
            if user_id == cek_id:
                break
            cek_id = input('Masukkan Nomer ID Pemesanan : ')
        print("Silahkan Lakukan Transfer Ke Nomor Rekening Di Bawah")
        print("Nomor Rekening Sewa Villa-Naruto --> BCA 0042069111")
        input("Tekan Enter Untuk Melanjutkan ")
        nomor_rekening_pengguna = input('Masukan Nomor Rekening Anda sebagai Bukti Transfer : ')
        booked()
        print('Pemesanan berhasil dilakukan, Kami akan mengirimkan Kode Voucher ke alamat email anda')
        print('\nKode Voucher/ Kode Pembayaran anda adalah -->', kode_booking)

    if pilih == 2:
        cek_id = input('Masukkan Nomor ID Pemesanan : ')
        print(user_id)
        while True:  # cek id dapat dari mikli
            if user_id == cek_id:
                booked()
                print("Pemesananan berhasil dilakukan silahkan lakukan pembayaran dengan Nomor Pembayaran di bawah")
                print("Nomor Pembayaran/ID Pembayaran -->", kode_booking)
                break
            print('ID Salah!')
            cek_id = input('Masukan Nomor ID Pemesanan : ')
    input("Tekan Enter Untuk Kembali")
    os.system('cls' if os.name == 'nt' else 'clear')

def catatan_pemesanan():
    cek_id = input("Masukan Id Pembayaran : ")
    data_sementara = list()
    with open(data_pengunjung, 'r') as pengunjung:
        cek_info = csv.DictReader(pengunjung)
        for info in cek_info:
            data_sementara.append(info)
        for info in data_sementara:
            if info['ID_Pembayaran'] == cek_id:
                print(f"{'Nama': <15}: "+ info['Nama'],
                f"\n{'NIK': <15}: " + info['NIK'],
                f"\n{'Alamat': <15}: "+ info['Alamat'],
                f"\n{'Email': <15}: "+ info['Email'],
                f"\n{'Check-In': <15}: "+ info['Check-in'],
                f"\n{'Lama Inap': <15}: "+ info['Inap'],
                f"\n{'Jenis Villa': <15}: "+ info['Villa'],
                f"\n{'ID_Pembayaran': <15}: "+ info['ID_Pembayaran']
                )
                break
            elif len(data_sementara) == data_sementara.index(info)+1:
                print("Data Tidak Ditemukan")
    if pilihan == 4:
        input("Tekan Enter Untuk Kembali")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    while True:
        halaman_utama()



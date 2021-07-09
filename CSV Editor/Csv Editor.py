import csv #import module csv
import os #import module OS

pilih_menu = '' #menyimpan isi pilih_menu
indeks_terakhir = 1 #menyimpan data nomor indeks global
nama_file_jadi = '' #menympan nama file yang digunakan

def pilihan(): #fungsi bernama pilihan yang akan menentukan penggunaan fungsi sesuai input user
    if pilih_menu == '1':
        membuat_file()
    elif pilih_menu == '2':
        pemroses()
        membaca_file()
    elif pilih_menu == '3':
        menambah_data()
    elif pilih_menu == '4':
        pemroses()
        data_baru()
    elif pilih_menu == '5':
        pemroses()
        hapus_data()
    elif pilih_menu == '6':
        pemroses()
        hapus_file()
    elif pilih_menu == '0':
        exit()
    else:
        print("Input Salah!")
        kembali()

def membersihkan_layar(): #fungsi yang berguna untuk membersihkan layar terminal
    if os.name == 'nt':
        os.system('')
        print('\n')
    else:
        os.system('clear')
        print('\n')

def kembali(): #Menu yang membiarkan user melihat datanya sebelum kembali ke layar awal
    input("\nTekan Enter Untuk Kembali")

def menampilkan_data_pembelian(): #Menampilkan isi direktori dari folder data pembelian pada user
    dir = os.listdir('data pembelian')
    print('data pembelian :')
    for i in dir:
        print('    ',i)

def pemroses(): #mengolah data yang dimasukan oleh user untuk menjadi variabel global
    global nama_file_jadi
    global indeks_terakhir
    menampilkan_data_pembelian()
    nama_file_mentah = input("Masukan Nama File : ")
    nama_file_jadi = '{}.csv'.format(nama_file_mentah)
    file_yang_dibuka = open("data pembelian/{}".format(nama_file_jadi), 'r')
    pembaca = csv.reader(file_yang_dibuka)
    indeks_terakhir = len(list(pembaca))
    file_yang_dibuka.close()
    print("Data Tidak Ditemukan")

def membaca_file(): #Fungsi untuk menampilkan isi file csv yang dipilih oleh user
    global nama_file_jadi
    if pilih_menu == '2':
        membersihkan_layar()
    nama_file = nama_file_jadi
    print(f"{'Nomor' : <5}{'Tanggal' : ^10}{'Nama Barang' : ^15}"
          f"{'Harga' : ^10}{'Jumlah' : ^10}{'Total' : >10}")
    with open('data pembelian/{}'.format(nama_file), 'r') as nama_file:
        baca = csv.DictReader(nama_file)
        for item in baca:
            print(f"{item['Nomor'] : <5}{item['Tanggal'] : ^10}{item['Nama Barang'] : ^15}"
                  f"{item['Harga'] : ^10}{item['Jumlah'] : ^10}{item['Total'] : >10}")
    if pilih_menu == '2':
        print("\nData Sedang Ditampilkan")
        kembali()

def masukan_data(data = dict()): #Fungsi yang akan menerima input dari user untuk ditampung kedalam dictionaries data
    data["Tanggal"] = input("Masukan Tanggal : ")
    data["Nama Barang"] = input("Masukan Nama Barang : ")
    data["Harga"] = int(input("Masukan Harga Barang : "))
    data["Jumlah"] = int(input("Masukan Jumlah Barang : "))
    total = data.get("Jumlah") * data.get("Harga")
    data["Total"] = total
    return data

def menambah_data(): #Fungsi yang berguna untuk memasukan data pembelian baru pada file csv sesuai input user
    while True:
        pemroses()
        global nama_file_jadi
        global indeks_terakhir
        membersihkan_layar()
        membaca_file()
        nama_file = nama_file_jadi
        with open('data pembelian/{}'.format(nama_file), 'a', newline='') as nama_file:
            area = ['Nomor', 'Tanggal', "Nama Barang", "Harga", "Jumlah", "Total"]
            tambah_data = csv.DictWriter(nama_file, fieldnames=area)
            nomor_index = masukan_data()
            nomor_index["Nomor"] = str(indeks_terakhir)
            tambah_data.writerow(nomor_index)
        print("\nData Pembelian telah ditambahkan kedalam File")
        keluar = input("Apakah ada yang ingin ditambahkan lagi? [y]/[t] : ")
        while keluar != 'y' and keluar != 't':
            keluar = input("Apakah ada yang ingin ditambahkan lagi? [y]/[t] : ")
        if keluar == 'y':
            nama_file.close()
            continue
        elif keluar == 't':
            break
        kembali()

def membuat_file(): #Fungsi untuk user membuat file csv baru sesuai dengan nama yang user inginkan
    membersihkan_layar()
    nama_file_mentah = input("Masukan Nama File Baru : ")
    nama_file = "{}.csv".format(nama_file_mentah)
    with open('data pembelian/{}'.format(nama_file), 'a', newline='') as nama_file:
        area = ['Nomor', 'Tanggal', "Nama Barang", "Harga", "Jumlah", "Total"]
        data_baru = csv.DictWriter(nama_file, fieldnames=area)
        data_baru.writeheader()
        nomor_baru = masukan_data()
        nomor_baru["Nomor"] = '1'
        data_baru.writerow(nomor_baru)
    print("\nData Pembelian baru telah dibuat")
    kembali()

def modifikasi_data(): #adalah fungsi untuk memproses data masukan dari user untuk sementara disimpan datanya
    #yang nantinya bisa digunakan pada fungsi memperbarui data dan menghapus data
    global nama_file_jadi
    data_sementara = []
    membaca_file()
    nama_file = nama_file_jadi
    with open('data pembelian/{}'.format(nama_file), 'r',) as nama_file:
        pembaca = csv.DictReader(nama_file)
        for baris in pembaca:
            data_sementara.append(baris)
        if pilih_menu == '4':
            nomor = input('Masukan Nomor Data Pembelian Yang akan diedit : ')
            indeks = 0
            for item in data_sementara:
                if (item['Nomor'] == nomor):
                    data_baru = masukan_data()
                    data_sementara[indeks]['Tanggal'] = data_baru['Tanggal']
                    data_sementara[indeks]['Nama Barang'] = data_baru['Nama Barang']
                    data_sementara[indeks]['Harga'] = data_baru['Harga']
                    data_sementara[indeks]['Jumlah'] = data_baru['Jumlah']
                    data_sementara[indeks]['Total'] = data_baru['Total']
                    return data_sementara
                elif indeks >=1000:
                    print('Data Tidak Ditemukan')
                    break
                indeks += 1
        elif pilih_menu == '5':
            nomor = input('Masukan Nomor Data Pembelian Yang akan dihapus : ')
            indeks = 0
            for item in data_sementara:
                if (item['Nomor'] == nomor):
                    data_sementara.remove(data_sementara[indeks])
                    return data_sementara
                indeks += 1

def data_baru(): #adalah fungsi yang berfungsi untuk memperbarui data file csv dengan data baru dari inputan user
    global nama_file_jadi
    membersihkan_layar()
    data_baru = modifikasi_data()
    nama_file = nama_file_jadi
    with open('data pembelian/{}'.format(nama_file), 'w', newline='') as nama_file:
        area = ['Nomor', 'Tanggal', "Nama Barang", "Harga", "Jumlah", "Total"]
        tulis_ulang = csv.DictWriter(nama_file, fieldnames=area)
        tulis_ulang.writeheader()
        for data_ulang in data_baru:
            tulis_ulang.writerow(data_ulang)
    print("\nData Pembelian dalam file telah diperbarui")
    kembali()

def hapus_data(): #adalah fungsi yang berfungsi untuk menghapus suatu baris dalam file csv sesuai pilihan user
    global nama_file_jadi
    membersihkan_layar()
    menghapus_data = modifikasi_data()
    nama_file = nama_file_jadi
    with open('data pembelian/{}'.format(nama_file), 'w', newline='') as nama_file:
        area = ['Nomor', 'Tanggal', "Nama Barang", "Harga", "Jumlah", "Total"]
        hapus_baris = csv.DictWriter(nama_file, fieldnames=area)
        hapus_baris.writeheader()
        indeks = 1
        for data_ulang in menghapus_data:
            data_ulang['Nomor'] = str(indeks)
            hapus_baris.writerow(data_ulang)
            indeks += 1
    print("\nData Pembelian dalam file telah tersebut diperbarui")
    kembali()

def hapus_file(): #adalah fungsi untuk menghapus file csv yang dipilih oleh user dalam direktori data pembelian
    membersihkan_layar()
    membaca_file()
    yakin = input("Apakah anda yakin untuk menghapus file tersebut? [y]/[t] : ")
    while yakin != 'y' and yakin != 't':
        print("INPUT SALAH!")
        yakin = input("\nApakah anda yakin untuk menghapus file tersebut? [y]/[t] : ")
    if yakin == 'y':
        os.remove(f"data pembelian/{nama_file_jadi}")
        print("File telah dihapus")
    elif yakin == 't':
        print("\nFungsi telah dibatalkan")
        kembali()

while True: # adalah perulangan yang senantia menampilkan laman utama kecuali terjadi error atau user memilih untuk keluar
    membersihkan_layar()
    print(
        "==============CSVEDITOR=============="
        "\n========= Mikli Oktrarianto ========="
        "\n"+"_" * 37,
        "\n[1]Membuat      | File Baru          "
        "\n[2]Melihat      | Data pada File Lama"
        "\n[3]Menambahkan  | Data Pada File Lama"
        "\n[4]Memodifikasi | Data Pada File Lama"
        "\n[5]Menghapus    | Data Pada File Lama"
        "\n[6]Menghapus    | File Data Pembelian"
        "\n[0]===========>KELUAR<==============="
        "\n"+"_"*37
    )
    pilih_menu = input("\nPilih Menu : ")
    pilihan()

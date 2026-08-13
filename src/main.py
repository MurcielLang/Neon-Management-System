import pandas as pd
df = pd.read_excel("data/Inventory.xlsx")

def check_inventory():
    print(df)

def search_id():
    ID = input("Masukkan ID Barang Yang Ingin Dicari: ").upper()
    hasil = df[df['ID'] == ID]
    if hasil.empty:
        print('Data tidak ditemukan!')
    else:
        print(hasil)     

def search_barang():
    barang = input('Masukkan Nama Barang Yang Ingin Dicari: ').title()
    hasil = df[df['Nama Barang'] == barang]
    if hasil.empty:
        print('Data tidak ditemukan!')
    else:
        print(hasil)

def search_jenis():
    jenis = input('Masukkan Jenis Barang Yang Ingin Dicari: ').title()
    if jenis == 'Atk':
        jenis = 'ATK'
    hasil = df[df['Jenis'] == jenis]
    if hasil.empty:
        print('Data tidak ditemukan!')
    else:
        print(hasil)

def search_harga():
    harga = int(input('Masukkan Harga Barang Yang Ingin Dicari: '))
    hasil = df[df['Harga'] == harga]
    if hasil.empty:
        print('Data tidak ditemukan!')
    else:
        print(hasil)

def search_stok():
    stok = int(input('Masukkan Stok Barang Yang Ingin Dicari: '))
    hasil = df[df['Stok'] == stok]
    if hasil.empty:
        print("Data tidak ditemukan!")
    else:
        print(hasil)

def main_menu():
    while True: 
        print()
        print('=' * 40)
        print('          WELCOME TO NEON MARKET          ')
        print("=" * 40)    
        print("1. Lihat Inventory")
        print("2. Cari Barang")
        print("3. Kelola Barang")
        print("4. Sortir Barang ")
        print("5. Filter Barang")
        print("0. Keluar")

        answer = int(input("Pilih Menu: "))
        if answer == 1:
            check_inventory()
            input('Tekan ENTER untuk kembali ke menu utama')
        elif answer == 2:
            while True:
                print("===== CARI BARANG =====")
                print("1. Cari barang berdasarkan ID")
                print("2. Cari barang berdasarkan nama")
                print("3. Cari barang berdasarkan jenis")
                print("4. Cari barang berdasarkan harga")
                print("5. Cari barang berdasarkan stok")
                print("0. Kembali ke menu utama")

                search = int(input("Pilih jenis pencarian: "))
                if search == 0:
                    break
                elif search == 1:
                    search_id()
                    input('Tekan ENTER untuk kembali ke menu cari barang')
                elif search == 2:
                    search_barang()
                    input('Tekan ENTER untuk kembali ke menu cari barang')
                elif search == 3:
                    search_jenis()
                    input('Tekan ENTER untuk kembali ke menu cari barang')
                elif search == 4:
                    search_harga()
                    input('Tekan ENTER untuk kembali ke menu cari barang')
                elif search == 5:
                    search_stok()
                    input('Tekan ENTER untuk kembali ke menu cari barang')

                else:
                    print("Pilihan tidak tersedia")
                

main_menu()




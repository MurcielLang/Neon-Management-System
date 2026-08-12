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
    stok = int(input('Masukan Stok Barang Yang Ingin Dicari: '))
    hasil = df[df['Stok'] == stok]
    if hasil.empty:
        print('Data tidak ditemukan!')
    else:
        print(hasil)

search_harga()
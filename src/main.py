import pandas as pd
df = pd.read_excel("data/Inventory.xlsx")

def check_inventory():
    print(df)

def search_menu():
    while True:
                print("\n===== CARI BARANG =====")
                print("1. Cari barang berdasarkan ID")
                print("2. Cari barang berdasarkan nama")
                print("3. Cari barang berdasarkan jenis")
                print("4. Cari barang berdasarkan harga")
                print("5. Cari barang berdasarkan stok")
                print("0. Kembali ke menu utama")

                while True:
                    try:
                        search = int(input("Pilih jenis pencarian: "))
                        break
                    except ValueError:
                        print("Error! Harap masukkan angka yang tersedia!")
                        continue

                if search == 0:
                    return
                elif search == 1:
                    search_id()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                elif search == 2:
                    search_barang()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                elif search == 3:
                    search_jenis()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                elif search == 4:
                    search_harga()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                elif search == 5:
                    search_stok()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                else:
                    print("Pilihan tidak tersedia")

def search_id():
    ID = int(input("Masukkan ID Barang Yang Ingin Dicari: "))
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
    while True:
        try:
            harga = int(input('Masukkan Harga Barang Yang Ingin Dicari: '))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")

    hasil = df[df['Harga'] == harga]
    if hasil.empty:
        print('Data tidak ditemukan!')
    else:
        print(hasil)
        

def search_stok():
    while True:
        try:
            stok = int(input('Masukkan Stok Barang Yang Ingin Dicari: '))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")
            
    hasil = df[df['Stok'] == stok]
    if hasil.empty:
        print("Data tidak ditemukan!")
    else:
        print(hasil)


def kelola_barang():
    while True:
        print("\n===== KELOLA BARANG =====")
        print("1. Tambah barang")
        print("2. Edit barang")
        print("3. Hapus Barang")
        print("0. Kembali ke menu utama")

        while True:
            try:
                answer = int(input("Pilih menu: "))
                break
            except ValueError:
                print("Error! Harap masukkan angka!")

        if answer == 0:
            return

        elif answer == 1:
            add_item()
        elif answer == 2:
            edit_item()


def add_item():
    global df
    print("\n===== TAMBAH BARANG =====")
    new_id = df['ID'].max() + 1

    barang = input("Masukkan Nama Barang: ").title()
    jenis = input("Masukkan jenis barang: ").title()
    if jenis == 'Atk':
        jenis = "ATK"

    while True:
        try:
            harga = int(input("Masukkan harga barang: "))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")
            continue

    while True:
        try:
            stok = int(input("Masukkan stok barang: "))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")
            continue

    new_data = pd.DataFrame([{
        "ID" : new_id,
        "Nama Barang" : barang,
        "Jenis" : jenis,
        "Harga" : harga,
        'Stok' : stok 
    }])

    df = pd.concat([df , new_data], ignore_index= True)
    df.to_excel("data/Inventory.xlsx", index = False)
    print('Barang berhasil ditambahkan!')

def edit_item():
    edit_id = int(input('Masukkan ID barang yang ingin diedit: '))

    if edit_id not in df["ID"].values:
        print("Data tidak ditemukan!")
        return

    hasil = df[df["ID"] == edit_id]
    print("Data barang: ")
    print(hasil)

    while True:
        print("\n===== EDIT BARANG =====")
        print("1. Edit nama barang")
        print("2. Edit jenis barang")
        print("3. Edit harga barang")
        print("4. Edit stok barang")
        print("0. Kembali")

        try:
            pilihan_edit = int(input("Pilih menu: "))
        except ValueError:
            print("Error! Harap masukkan angka yang tersedia!")
            continue

        if pilihan_edit == 1:
            nama_baru = input("Masukkan nama baru: ").title()

            df.loc[df['ID'] == edit_id, "Nama Barang"] = nama_baru
            df.to_excel("data/Inventory.xlsx", index=False)

            print("Nama barang berhasil diubah!")

        elif pilihan_edit == 2:
            jenis_baru = input("Masukkan jenis baru: ").title()
            if jenis_baru == "Atk":
                jenis_baru = 'ATK'

            df.loc[df["ID"] == edit_id, "Jenis"] = jenis_baru
            df.to_excel("data/Inventory.xlsx", index=False)

            print("Jenis barang berhasil diubah!")
        
        elif pilihan_edit == 3:
            while True:
                try:
                    harga_baru = int(input("Masukkan harga baru: "))
                    break
                except ValueError:
                    print("Error! Harga harus berupa angka!")

            df.loc[df["ID"] == edit_id, "Harga"] = harga_baru
            df.to_excel('data/Inventory.xlsx', index=False)

            print("Harga berhasil diubah!")

        elif pilihan_edit == 4:
            while True:
                try:
                    stok_baru = int(input("Masukkan stok baru: "))
                    break
                except ValueError:
                    print('Error stok harus berupa angka')

            df.loc[df["ID"]== edit_id, "Stok"] = stok_baru
            df.to_excel("data/Inventory.xlsx", index=False)

            print("Stok berhasil diubah!")

        elif pilihan_edit == 0:
            return

        else:
            print("Pilihan tidak tersedia!")



def main_menu():
    while True: 
        print()
        print("========== WELCOME TO NEON MARKET ==========")
        print("1. Lihat Inventory")
        print("2. Cari Barang")
        print("3. Kelola Barang")
        print("4. Sortir Barang ")
        print("5. Filter Barang")
        print("0. Keluar")

        while True:
            try:
                answer = int(input("Pilih Menu: "))
                break
            except ValueError:
                print("Error! Harap masukkan angka yang tersedia!")

        if answer == 0:
            print("Bye bye!")
            break

        elif answer == 1:
            check_inventory()
            input('Tekan ENTER untuk kembali ke menu utama')

        elif answer == 2:
            search_menu()

        elif answer == 3:
            kelola_barang()

        
            
main_menu()

import pandas as pd
df = pd.read_excel("data/Inventory.xlsx")

def check_inventory():
    print(df)

def search_inventory():
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
                        print("Error! Harap masukkan pilihan menu yang tersedia!")
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
                    print("Error! Harap masukkan pilihan menu yang tersedia!")

def search_id():
    while True:
            try:
                ID = int(input("Masukkan ID Barang Yang Ingin Dicari: "))
                break
            except ValueError:
                print('Error! Harap masukkan angka!')
                
            
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


def manage_inventory():
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
        elif answer == 3:
            delete_item()

        else:
            print("Error! Harap masukkan pilihan menu yang tersedia!")


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
    while True:
        try:
            edit_id = int(input('Masukkan ID barang yang ingin diedit: '))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")

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
            print("Error! Harap masukkan pilihan menu yang tersedia!")
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


def delete_item():
    while True:
        try:
            delete_id = int(input("Masukkan ID barang yang ingin dihapus: "))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")

    if delete_id not in df["ID"].values:
        print("Data tidak ditemukan!")
        return 

    hasil = df[df["ID"] == delete_id]
    print("Data barang:")
    print(hasil)

    while True:
        confirm = input("Yakin ingin menghapus barang ini? (y/n): ").lower()

        if confirm =="y":
            break
        elif confirm == "n":
            print("Penghapusan dibatalkan")
            return 
        else:
            print("Masukkan y atau n!")

    index_barang = df[df["ID"] == delete_id].index
    df.drop(index_barang, inplace=True)
    df.to_excel("data/Inventory.xlsx", index=False)

    print("Barang berhasil dihapus!")

def sort_id():

    print("\nUrutan:")
    print("1. Terkecil >>> Terbesar")
    print("2. Terbesar >>> Terkecil")

    while True:
        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")
            continue

        if pilihan == 1:
            hasil = df.sort_values("ID")
            print(hasil)
            break

        elif pilihan == 2:
            hasil = df.sort_values("ID", ascending=False)
            print(hasil)
            break

        else:
            print("Error! Harap pilih menu yang sudah tersedia!")
        


def sort_inventory():
    while True:
        print("\n===== SORTIR BARANG =====")
        print("1. Berdasarkan ID barang")
        print("2. Berdasarkan nama barang")
        print("3. Berdasarkan jenis barang")
        print("4. Berdasarkan harga barang")
        print("5. Berdasarkan stok barang")
        print("0. Kembali")

        while True:
            try:
                sortir = int(input("Pilih menu:"))
                break
            except ValueError:
                print("Error! Harap masukkan pilihan menu yang tersedia!")

        if sortir == 0:
            return 

        elif sortir == 1:
            sort_id()



        
def main_menu():
    while True: 
        print()
        print("========== WELCOME TO NEON STORE ==========")
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
            search_inventory()

        elif answer == 3:
            manage_inventory()

        elif answer == 4:
            sort_inventory()

        else:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")


        
            
main_menu()

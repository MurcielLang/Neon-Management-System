"""NeonStore - Inventory Management System

Main application for managing the NeonStore inventory.
"""

import pandas as pd


INVENTORY_FILE = "data/Inventory.xlsx"

df = pd.read_excel(INVENTORY_FILE)

def show_inventory():
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
                        choice = int(input("Pilih jenis pencarian: "))
                        break
                    except ValueError:
                        print("Error! Harap masukkan pilihan menu yang tersedia!")
                        continue

                if choice == 0:
                    return
                elif choice == 1:
                    search_id()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                elif choice == 2:
                    search_name()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                elif choice == 3:
                    search_type()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                elif choice == 4:
                    search_price()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                elif choice == 5:
                    search_stock()
                    input("Tekan ENTER untuk kembali ke menu cari barang")
                else:
                    print("Error! Harap masukkan pilihan menu yang tersedia!")

def search_id():
    while True:
            try:
                item_id = int(input("Masukkan ID Barang Yang Ingin Dicari: "))
                break
            except ValueError:
                print('Error! Harap masukkan angka!')
                
            
    result = df[df['ID'] == item_id]
    if result.empty:
        print('Data tidak ditemukan!')
    else:
        print(result)     

def search_name():
    item_name = input('Masukkan Nama Barang Yang Ingin Dicari: ').title()
    result = df[df['Nama Barang'] == item_name]
    if result.empty:
        print('Data tidak ditemukan!')
    else:
        print(result)

def search_type():
    item_type = input('Masukkan Jenis Barang Yang Ingin Dicari: ').title()
    if item_type == 'Atk':
        item_type = 'ATK'
    result = df[df['Jenis'] == item_type]
    if result.empty:
        print('Data tidak ditemukan!')
    else:
        print(result)

def search_price():
    while True:
        try:
            price = int(input('Masukkan Harga Barang Yang Ingin Dicari: '))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")

    result = df[df['Harga'] == price]
    if result.empty:
        print('Data tidak ditemukan!')
    else:
        print(result)
        

def search_stock():
    while True:
        try:
            stock = int(input('Masukkan Stok Barang Yang Ingin Dicari: '))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")
            
    result = df[df['Stok'] == stock]
    if result.empty:
        print("Data tidak ditemukan!")
    else:
        print(result)


def manage_menu():
    while True:
        print("\n===== KELOLA BARANG =====")
        print("1. Tambah barang")
        print("2. Edit barang")
        print("3. Hapus Barang")
        print("0. Kembali ke menu utama")

        while True:
            try:
                choice = int(input("Pilih menu: "))
                break
            except ValueError:
                print("Error! Harap masukkan angka!")

        if choice == 0:
            return

        elif choice == 1:
            add_item()
        elif choice == 2:
            edit_item()
        elif choice == 3:
            delete_item()

        else:
            print("Error! Harap masukkan pilihan menu yang tersedia!")


def add_item():
    global df
    print("\n===== TAMBAH BARANG =====")
    new_id = df['ID'].max() + 1

    item_name = input("Masukkan Nama Barang: ").title()
    item_type = input("Masukkan jenis barang: ").title()
    if item_type == 'Atk':
        item_type = "ATK"

    while True:
        try:
            price = int(input("Masukkan harga barang: "))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")
            continue

    while True:
        try:
            stock = int(input("Masukkan stok barang: "))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")
            continue

    new_item = pd.DataFrame([{
        "ID" : new_id,
        "Nama Barang" : item_name,
        "Jenis" : item_type,
        "Harga" : price,
        'Stok' : stock 
    }])

    df = pd.concat([df , new_item], ignore_index= True)
    df.to_excel("data/Inventory.xlsx", index = False)
    print('Barang berhasil ditambahkan!')

def edit_item():
    while True:
        try:
            item_id = int(input('Masukkan ID barang yang ingin diedit: '))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")

    if item_id not in df["ID"].values:
        print("Data tidak ditemukan!")
        return

    result = df[df["ID"] == item_id]
    print("Data barang: ")
    print(result)

    while True:
        print("\n===== EDIT BARANG =====")
        print("1. Edit nama barang")
        print("2. Edit jenis barang")
        print("3. Edit harga barang")
        print("4. Edit stok barang")
        print("0. Kembali")

        try:
            choice = int(input("Pilih menu: "))
        except ValueError:
            print("Error! Harap masukkan pilihan menu yang tersedia!")
            continue

        if choice == 1:
            new_name = input("Masukkan nama baru: ").title()

            df.loc[df['ID'] == item_id, "Nama Barang"] = new_name
            df.to_excel("data/Inventory.xlsx", index=False)

            print("Nama barang berhasil diubah!")

        elif choice == 2:
            new_type = input("Masukkan jenis baru: ").title()
            if new_type == "Atk":
                new_type = 'ATK'

            df.loc[df["ID"] == item_id, "Jenis"] = new_type
            df.to_excel("data/Inventory.xlsx", index=False)

            print("Jenis barang berhasil diubah!")
        
        elif choice == 3:
            while True:
                try:
                    new_price = int(input("Masukkan harga baru: "))
                    break
                except ValueError:
                    print("Error! Harga harus berupa angka!")

            df.loc[df["ID"] == item_id, "Harga"] = new_price
            df.to_excel('data/Inventory.xlsx', index=False)

            print("Harga berhasil diubah!")

        elif choice == 4:
            while True:
                try:
                    new_stock = int(input("Masukkan stok baru: "))
                    break
                except ValueError:
                    print('Error stok harus berupa angka')

            df.loc[df["ID"]== item_id, "Stok"] = new_stock
            df.to_excel("data/Inventory.xlsx", index=False)

            print("Stok berhasil diubah!")

        elif choice == 0:
            return

        else:
            print("Pilihan tidak tersedia!")


def delete_item():
    while True:
        try:
            item_id = int(input("Masukkan ID barang yang ingin dihapus: "))
            break
        except ValueError:
            print("Error! Harap masukkan angka!")

    if item_id not in df["ID"].values:
        print("Data tidak ditemukan!")
        return 

    result = df[df["ID"] == item_id]
    print("Data barang:")
    print(result)

    while True:
        confirmation = input("Yakin ingin menghapus barang ini? (y/n): ").lower()

        if confirmation =="y":
            break
        elif confirmation == "n":
            print("Penghapusan dibatalkan")
            return 
        else:
            print("Masukkan y atau n!")

    item_index = df[df["ID"] == item_id].index
    df.drop(item_index, inplace=True)
    df.to_excel("data/Inventory.xlsx", index=False)

    print("Barang berhasil dihapus!")

def sort_by_name():
    
    print("\nUrutan:")
    print("1. A >>> Z")
    print("2. Z >>> A ")

    while True:
        try:
            choice = int(input("Pilih menu: "))
        except ValueError:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")
            continue

        if choice == 1:
            result = df.sort_values("Nama Barang")
            print(result)
            break

        elif choice == 2:
            result = df.sort_values("Nama Barang", ascending=False)
            print(result)
            break

        else:
            print("Error! Harap pilih menu yang sudah tersedia!")

def sort_by_type():
    
    print("\nUrutan:")
    print("1. A >>> Z")
    print("2. Z >>> A")

    while True:
        try:
            choice = int(input("Pilih menu: "))
        except ValueError:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")
            continue

        if choice == 1:
            result = df.sort_values("Jenis")
            print(result)
            break

        elif choice == 2:
            result = df.sort_values("Jenis", ascending=False)
            print(result)
            break

        else:
            print("Error! Harap pilih menu yang sudah tersedia!")

def sort_by_price():
    
    print("\nUrutan:")
    print("1. Termurah >>> Termahal")
    print("2. Termahal >>> Termurah")

    while True:
        try:
            choice = int(input("Pilih menu: "))
        except ValueError:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")
            continue

        if choice == 1:
            result = df.sort_values("Harga")
            print(result)
            break

        elif choice == 2:
            result = df.sort_values("Harga", ascending=False)
            print(result)
            break

        else:
            print("Error! Harap pilih menu yang sudah tersedia!")

def sort_by_stock():
    
    print("\nUrutan:")
    print("1. Terkecil >>> Terbesar")
    print("2. Terbesar >>> Terkecil")

    while True:
        try:
            choice = int(input("Pilih menu: "))
        except ValueError:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")
            continue

        if choice == 1:
            result = df.sort_values("Stok")
            print(result)
            break

        elif choice == 2:
            result = df.sort_values("Stok", ascending=False)
            print(result)
            break

        else:
            print("Error! Harap pilih menu yang sudah tersedia!")

def sort_menu():
    while True:
        print("\n===== SORTIR BARANG =====")
        print("1. Berdasarkan Nama barang")
        print("2. Berdasarkan Jenis barang")
        print("3. Berdasarkan Harga barang")
        print("4. Berdasarkan Stok barang")
        print("0. Kembali")

        while True:
            try:
                choice = int(input("Pilih menu: "))
                break
            except ValueError:
                print("Error! Harap masukkan pilihan menu yang tersedia!")

        if choice == 0:
            return 

        elif choice == 1:
            sort_by_name()

        elif choice == 2:
            sort_by_type()

        elif choice == 3:
            sort_by_price()

        elif choice == 4:
            sort_by_stock()

        else:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")


def filter_by_price():
    while True:
        print("\n===== FILTER HARGA =====")
        print("1. Lebih dari")
        print("2. Kurang dari")
        print("3. Sama dengan")
        print("0. Kembali")

        while True:
            try:
                choice = int(input('Pilih menu: '))
                break
            except ValueError:
                print("Error! Harap masukkan pilihan menu yang sudah tersedia!")

        if choice == 0:
            break

        elif choice == 1:
            while True:
                try:
                    price = int(input("Masukkan harga: "))
                    break
                except ValueError:
                    print("Error! Harap masukkan angka!")

            result = df[df["Harga"] > price]
            if result.empty:
                print("Data tidak ditemukan!")

            else:
                print(result)

        elif choice == 2:
            while True:
                try:
                    price = int(input("Masukkan harga: "))
                    break
                except ValueError:
                    print("Error! Harap masukkan angka!")

            result = df[df["Harga"] < price]
            if result.empty:
                print("Data tidak ditemukan!")

            else:
                print(result)

        elif choice == 3:
            while True:
                try:
                    price = int(input("Masukkan harga: "))
                    break
                except ValueError:
                    print("Error! Harap masukkan angka!")

            result = df[df["Harga"] == price]
            if result.empty:
                print("Data tidak ditemukan!")

            else:
                print(result)

        else:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")


def filter_by_stock():
    while True:
        print("\n===== FILTER STOK =====")
        print("1. Lebih dari")
        print("2. Kurang dari")
        print("3. Sama dengan")
        print("0. Kembali")

        while True:
            try:
                choice = int(input('Pilih menu: '))
                break
            except ValueError:
                print("Error! Harap masukkan pilihan menu yang sudah tersedia!")

        if choice == 0:
            break

        
        elif choice == 1:
            while True:
                try:
                    stock = int(input("Masukkan stok: "))
                    break
                except ValueError:
                    print("Error! Harap masukkan angka!")

            result = df[df["Stok"] > stock]
            if result.empty:
                print("Data tidak ditemukan!")

            else:
                print(result)

        
        elif choice == 2:
            while True:
                try:
                    stock = int(input("Masukkan stok: "))
                    break
                except ValueError:
                    print("Error! Harap masukkan angka!")

            result = df[df["Stok"] < stock]
            if result.empty:
                print("Data tidak ditemukan!")

            else:
                print(result)

        elif choice == 3:
            while True:
                try:
                    stock = int(input("Masukkan stok: "))
                    break
                except ValueError:
                    print("Error! Harap masukkan angka!")

            result = df[df["Stok"] == stock]
            if result.empty:
                print("Data tidak ditemukan!")

            else:
                print(result)

        else:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")






def filter_menu():
    while True:
        print("\n===== FILTER BARANG =====")
        print("1. Filter jenis barang")
        print("2. Filter harga barang")
        print("3. Filter stok barang")
        print("0. Kembali")

        while True:
            try: 
                choice = int(input("Pilih menu: "))
                break
            except ValueError:
                print("Error! harap masukkan pilihan menu yang sudah tersedia!")
                
        if choice == 0:
            return

        elif choice == 1:
            item_type = input("Masukkan jenis barang yang ingin difilter: ").title()

            if item_type == "Atk":
                item_type = "ATK"

            result = df[df["Jenis"] == item_type]

            if result.empty:
                print("Data tidak ditemukan!")

            else:
                print(result)

        elif choice == 2:
            filter_by_price()

        elif choice == 3:
            filter_by_stock()

        else:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")



                    



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
                choice = int(input("Pilih Menu: "))
                break
            except ValueError:
                print("Error! Harap masukkan angka yang tersedia!")

        if choice == 0:
            print("Bye bye!")
            break

        elif choice == 1:
            show_inventory()
            input('Tekan ENTER untuk kembali ke menu utama')

        elif choice == 2:
            search_menu()

        elif choice == 3:
            manage_menu()

        elif choice == 4:
            sort_menu()

        elif choice == 5:
            filter_menu()

        else:
            print("Error! Harap masukkan pilihan menu yang sudah tersedia!")


        
            
main_menu()
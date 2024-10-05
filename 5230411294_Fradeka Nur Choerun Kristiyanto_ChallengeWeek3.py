class DaftarMenu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
    def __str__(self):
        return f"{self.nama}    Rp{self.harga:.2f}"
    
class Menu:
    def __init__(self):
        self.menu_list = []

    def tambah_item(self, item):
        self.menu_list.append(item)
    
    def displaymenu(self):
        for index, item in enumerate(self.menu_list, start=1):
            print(f"{index}. {item}")

def main():
    menumakanan = Menu()
    menuminuman = Menu()

    menumakanan.tambah_item(DaftarMenu("Soto", 10000))
    menuminuman.tambah_item(DaftarMenu("Esteh", 3000))

    while True:
        print("\n============ Daftar menu ============")
        print("1. Daftar menu makanan")
        print("2. Daftar menu minuman")
        print("3. Tambah menu makanan")
        print("0. Keluar")
        
        men = int(input("Masukkan pilihan anda: "))
        
        if men == 1:
            if menumakanan.menu_list:
                print("\n=== Menu Makanan ===")
                menumakanan.displaymenu()
        
        elif men == 2:
            if menuminuman.menu_list:
                print("\n=== Menu Minuman ===")
                menuminuman.displaymenu()

        elif men == 3:
            print("\n=== Tambah Menu  ===")
            print ("1. Tambah makanan")
            print ("2. Tambah minuman")
            menutambah = int(input("Masukkan pilihan : "))
            if menutambah == 1 :
                makan = input("Masukkan nama makanan: ")
                hargamakan = int(input("Masukkan harga makanan: Rp."))
                menumakanan.tambah_item(DaftarMenu(makan, hargamakan))
                print("Menu makanan berhasil ditambahkan.")
            elif menutambah == 2 :
                minum = input("Masukkan nama minuman: ")
                hargaminum = int(input("Masukkan harga minuman: Rp."))
                menuminuman.tambah_item(DaftarMenu(minum, hargaminum))
                print("Menu minuman berhasil ditambahkan.")
            else :
                print("Pilihan tidak valid")

        elif men == 0:
            print("Program akan keluar.")
            break
        
        else:
            print("Menu tidak valid.")

if __name__ == "__main__":
    main()
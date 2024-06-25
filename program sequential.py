def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

def main():
    arr = []

    while True:
        print("\nMenu:")
        print("1. Input data")
        print("2. Hapus data")
        print("3. Cari data")
        print("4. Lihat data")
        print("5. Keluar")

        choice = input("Masukkan pilihan Anda (1-5): ")

        if choice == '1':
            elem = input("Masukkan nama barang: ")
            arr.append(elem)
            print(f"barang {elem} telah ditambahkan ke dalam array")
        
        elif choice == '2':
            if len(arr) == 0:
                print("Data kosong, tidak ada barang untuk dihapus.")
            else:
                elem = input("Masukkan barang yang akan dihapus: ")
                if elem in arr:
                    arr.remove(elem)
                    print(f"Barang {elem} telah dihapus dari array")
                else:
                    print(f"Barang {elem} tidak ditemukan dalam array")
        
        elif choice == '3':
            if len(arr) == 0:
                print("Data kosong, tidak ada barang untuk dicari.")
            else:
                x = input("Masukkan nama barang yang akan dicari: ")
                result = sequential_search(arr, x)
                if result != -1:
                    print(f"Barang '{x}' ditemukan pada indeks ke {result}.")
                else:
                    print(f"Barang '{x}' tidak ditemukan dalam data")
        
        elif choice == '4':
            if len(arr) == 0:
                print("Data kosong, tidak ada data untuk ditampilkan")
            else:
                print("Isi data saat ini: ")
                for i, elem in enumerate(arr):
                    print(f"{i}. {elem}")
        
        elif choice == '5':
            print("Anda telah keluar dari program")
            break
        
        else:
            print("Pilihan tidak valid. Masukkan pilihan 1 sampai 5")

if __name__ == "__main__":
    main()

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
            num_elements = int(input("Masukkan berapa banyak angka yang ingin ditambahkan: "))
            for _ in range(num_elements):
                elem = int(input(f"Masukkan angka ke {_+1}: "))
                arr.append(elem)
                print(f"Angka {elem} telah ditambahkan ke dalam array")
        
        elif choice == '2':
            if len(arr) == 0:
                print("Data kosong, tidak ada angka untuk dihapus")
            else:
                elem = int(input("Masukkan angka yang ingin dihapus: "))
                if elem in arr:
                    arr.remove(elem)
                    print(f"Angka {elem} telah dihapus dari data")
                else:
                    print(f"Angka {elem} tidak ditemukan dalam data")
        
        elif choice == '3':
            if len(arr) == 0:
                print("Data kosong, tidak ada angka untuk dicari")
            else:
                x = int(input("Masukkan angka yang ingin dicari: "))
                result = linear_search(arr, x)
                if result != -1:
                    print(f"Angka {x} ditemukan pada baris ke {result}")
                else:
                    print(f"Angka {x} tidak ditemukan dalam data")
        
        elif choice == '4':
            if len(arr) == 0:
                print("Data kosong, tidak ada data untuk ditampilkan")
            else:
                print("Isi data saat ini:")
                for i, elem in enumerate(arr):
                    print(f"{i}. {elem}")
        
        elif choice == '5':
            print("Anda telah keluar dari program")
            break
        
        else:
            print("Pilihan tidak valid. Masukkan pilihan 1 sampai 5")

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    main()

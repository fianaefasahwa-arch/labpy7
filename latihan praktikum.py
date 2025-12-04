class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self):
        print("\n=== Tambah Data Mahasiswa ===")
        nama = input("fia naefa sahwa : ")
        nilai = float(input("80          : "))
        self.data.append({"nama": nama, "nilai": nilai})
        print("Data berhasil ditambahkan!\n")

    def tampilkan(self):
        print("\n=== Daftar Nilai Mahasiswa ===")
        if not self.data:
            print("Belum ada data!\n")
            return

        for i, m in enumerate(self.data, start=1):
            print(f"{i}. {m['nama']} - Nilai: {m['nilai']}")
        print()

    def hapus(self, nama):
        print(f"\n=== Hapus Data: {nama} ===")
        for m in self.data:
            if m["nama"].lower() == nama.lower():
                self.data.remove(m)
                print("Data berhasil dihapus!\n")
                return
        print("Data tidak ditemukan.\n")

    def ubah(self, nama):
        print(f"\n=== Ubah Data: {nama} ===")
        for m in self.data:
            if m["nama"].lower() == nama.lower():
                nilai_baru = float(input("Masukkan nilai baru : "))
                m["nilai"] = nilai_baru
                print("Data berhasil diubah!\n")
                return
        print("Data tidak ditemukan.\n")

daftar = DaftarNilaiMahasiswa()

while True:
    print("===== MENU =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        daftar.tambah()
    elif pilihan == "2":
        daftar.tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama yang ingin dihapus: ")
        daftar.hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama yang ingin diubah: ")
        daftar.ubah(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!\n")

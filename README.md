# labpy7
# Tugas Praktikum 7 OOP (Class & Metho)

Nama : Fia Naefa Sahwa

Nim : 312510170

Kelas : TI.25.A2

Mata Kuliah : Pengantar Pemrograman

## 1. Judul Praktikum

Program Pengelolaan Daftar Nilai Mahasiswa Menggunakan Class dan Method (OOP – Python).

## 2. Deskripsi Program

Program ini dibuat untuk mengaplikasikan konsep Object-Oriented Programming (OOP) pada Python.
Program menggunakan sebuah class untuk menyimpan, menampilkan, menghapus, dan mengubah data nilai mahasiswa.

Data mahasiswa disimpan dalam bentuk list berisi dictionary, dan setiap operasi dilakukan melalui method pada class.

## 3. Tujuan Praktikum

Mahasiswa mampu membuat dan menggunakan class pada Python.

Mahasiswa dapat mengimplementasikan method: tambah, tampilkan, hapus, dan ubah.

Mahasiswa mampu membuat class diagram, flowchart, dan penjelasan program.

Mahasiswa dapat melakukan commit dan push ke GitHub.

## 4. Kode Program
```
class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data = []  # list untuk menyimpan dictionary

    def tambah(self, nama, nilai):
        """Menambah data mahasiswa"""
        self.data.append({
            "nama": nama,
            "nilai": nilai
        })
        print(f"Data '{nama}' berhasil ditambahkan!")

    def tampilkan(self):
        """Menampilkan seluruh data"""
        if not self.data:
            print("Belum ada data.")
            return
        print("\n=== DAFTAR NILAI MAHASISWA ===")
        for mhs in self.data:
            print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

    def hapus(self, nama):
        """Menghapus data berdasar nama"""
        for mhs in self.data:
            if mhs['nama'].lower() == nama.lower():
                self.data.remove(mhs)
                print(f"Data '{nama}' berhasil dihapus!")
                return
        print(f"Data dengan nama '{nama}' tidak ditemukan!")

    def ubah(self, nama, nilai_baru):
        """Mengubah nilai berdasar nama"""
        for mhs in self.data:
            if mhs['nama'].lower() == nama.lower():
                mhs['nilai'] = nilai_baru
                print(f"Data '{nama}' berhasil diubah!")
                return
        print(f"Data dengan nama '{nama}' tidak ditemukan!")


# --- Contoh penggunaan ---
if __name__ == "__main__":
    daftar = DaftarNilaiMahasiswa()

    daftar.tambah("Ari", 90)
    daftar.tambah("Dina", 85)
    daftar.tampilkan()

    daftar.ubah("Dina", 92)
    daftar.hapus("Ari")

    daftar.tampilkan()
```
## 5. Class Diagram
```
+----------------------------------+
|     DaftarNilaiMahasiswa         |
+----------------------------------+
| - data : list                    |
+----------------------------------+
| + tambah(nama, nilai)            |
| + tampilkan()                    |
| + hapus(nama)                    |
| + ubah(nama, nilai_baru)         |
+----------------------------------+
```
## 6. Flowchart Program
```
                 +----------------------+
                 |       Mulai          |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |     Menu Utama       |
                 +----------------------+
              /       |        |        \
             v        v        v         v

   +-----------+  +-----------+  +------------+  +------------+
   | Tambah    |  | Tampilkan |  |   Hapus    |  |    Ubah    |
   +-----------+  +-----------+  +------------+  +------------+
         |               |              |              |
         v               v              v              v

   Input nama & nilai    Tampilkan      Input nama     Input nama &
   Masukkan ke list      seluruh data   Hapus jika ada Ubah nilai

                            \            |             /
                             \           |            /
                              +----------+-----------+
                                         |
                                         v
                             +-----------------------+
                             |     Kembali ke Menu   |
                             +-----------------------+
                                         |
                                         v
                                 +---------------+
                                 |    Selesai    |
                                 +---------------+
```
## 7. Penjelasan Program

Class & Atribut

Program menggunakan class DaftarNilaiMahasiswa, dengan atribut:

data → list untuk menyimpan seluruh data mahasiswa.

Method Program

tambah(nama, nilai)
Menambahkan data ke list.

tampilkan()
Menampilkan seluruh data mahasiswa.

hapus(nama)
Mencari data berdasarkan nama, lalu menghapusnya.

ubah(nama, nilai_baru)
Mengubah nilai mahasiswa berdasarkan nama.

## Cara Kerja Program

Data mahasiswa disimpan dalam list berisi dictionary.

Setiap operasi hanya dilakukan melalui method pada class.

Program mencetak hasil setiap operasi untuk memudahkan pengguna.

## 8. Cara Menjalankan Program

Simpan file sebagai main.py.

Jalankan di terminal / cmd:
```
pycharm

```
Program akan menampilkan proses tambah, tampil, ubah, dan hapus data.

## 9. Commit & Push ke GitHub
```
git add .
git commit -m "Tugas Praktikum OOP - Daftar Nilai Mahasiswa"
git push origin main
```

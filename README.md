# Analisis Kualitas Air Sungai dan Danau di Provinsi Aceh Tahun 2020

Mini project mata kuliah Pemrograman Komputer, Kelompok 9A.
Laboratorium Sistem Informasi dan Keputusan, Departemen Teknik Industri, Universitas Andalas.

## Tentang Program

Program ini membaca data kualitas air sungai dan danau di Provinsi Aceh tahun 2020, lalu membantu pengguna melihat kondisi tiap lokasi pengamatan. Parameter yang dipakai adalah pH, DO, BOD, dan COD. Selain itu, program juga menampilkan lokasi mana yang sebaiknya dipantau lebih dulu berdasarkan Nilai Indeks Pencemaran (IP) dan status mutu air.

Program dibuat dengan Python dan dijalankan lewat terminal. Tidak ada library tambahan yang perlu dipasang.

## Fitur

- Register dan login (login diberi 3 kali kesempatan)
- Rata-rata pH, DO, BOD, dan COD per lokasi pengamatan
- Pencarian data berdasarkan parameter: nilai tertinggi, terendah, atau rentang nilai tertentu
- Prioritas pemantauan, yaitu lokasi diurutkan dari Nilai IP terbesar, lengkap dengan jumlah titik untuk tiap status mutu air
- Filter daerah (kabupaten, sungai, atau lokasi) yang bisa diganti kapan saja
- Pengaturan terakhir tiap pengguna tersimpan, jadi tidak perlu memilih ulang setiap kali

## Data

Data diambil dari [Open Data Aceh](https://data.acehprov.go.id/id/dataset/parameter-kualitas-air-sungai-dan-danau/resource/0ee08406-9f75-426d-82fb-5e7370e12bb7) (Data Kualitas Air Sungai dan Danau Tahun 2020).

- Format file: CSV, pemisah titik koma (`;`)
- Jumlah data: 150 baris dan 34 kolom
- Setelah dibersihkan: 149 baris dipakai, 1 baris dibuang

Baris akan dibuang kalau kolomnya kurang dari 34, tahunnya bukan 2020, atau nilai pH, DO, BOD, COD, dan IP-nya kosong atau bukan angka. Tanda `<` pada nilai (misalnya `<3.2234`) dihapus, dan koma desimal diubah menjadi titik.

## Isi Folder

```
main.py                        program utama
data-kualitas-air-sungai.csv   dataset
akun.csv                       dibuat otomatis saat ada yang register
pengaturan.csv                 dibuat otomatis saat pengaturan disimpan
README.md
```

File `main.py` dan `data-kualitas-air-sungai.csv` harus berada di folder yang sama. Nama file CSV-nya harus persis seperti di atas.

## Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Taruh `main.py` dan `data-kualitas-air-sungai.csv` dalam satu folder.
3. Buka terminal di folder tersebut, lalu jalankan:

```
python main.py
```

Kalau berhasil, program akan menampilkan jumlah data yang terbaca, contohnya:

```
Data dimuat: 149 baris valid, 1 baris dibuang.
```

## Cara Pakai

Di menu awal, buat akun dulu lewat **Register** (password minimal 4 karakter), lalu masuk lewat **Login**.

Setelah login, ada lima menu:

1. **Rata-rata per lokasi**: menampilkan rata-rata pH, DO, BOD, dan COD untuk setiap sungai dan lokasi.
2. **Cari data**: pilih parameter (pH, DO, BOD, COD, atau Nilai IP), lalu pilih tertinggi, terendah, atau rentang nilai. Untuk tertinggi dan terendah, jumlah data yang ditampilkan bisa 5, 10, atau semua. Untuk rentang, isi nilai minimum dan maksimum.
3. **Prioritas pemantauan**: menampilkan lokasi dengan Nilai IP tertinggi (paling tercemar) lebih dulu, lalu ringkasan jumlah titik per status mutu air.
4. **Ganti daerah**: mengubah filter daerah.
5. **Logout**

Tentang filter daerah: saat pertama kali membuka menu 1, 2, atau 3, program akan menanyakan filternya, misalnya `Aceh Barat`. Dikosongkan berarti semua data. Pilihan ini disimpan dan dipakai lagi di menu lain sampai kamu menggantinya lewat menu 4. Pencarian tidak membedakan huruf besar dan kecil.

Tentang pengaturan terakhir: di menu 2 dan 3, kalau sebelumnya sudah pernah memilih, program akan bertanya apakah mau memakai pengaturan itu lagi (`y/n`).

## Contoh Hasil

Hasil berikut didapat dari data tahun 2020 tanpa filter:

- Jumlah lokasi unik: 78
- pH tertinggi: 8,66 (Krueng Jambo Ayee, Banda Aceh)
- pH terendah: 6,17 (Krueng Woyla, Aceh Barat)
- BOD tertinggi: sekitar 31,4 (Danau Aneuk Laot, Sabang)
- Nilai IP tertinggi: 7,89 (Krueng Lamnyong, Banda Aceh), status Cemar Sedang
- Status mutu air: Cemar Ringan 139 titik, Cemar Sedang 9 titik, Kondisi Baik 1 titik

## Struktur Kode

Kode dibagi menjadi tiga class:

- `Akun`: `register()` dan `login()`
- `Pengaturan`: `simpan()` untuk menyimpan pengaturan pengguna dan `daerah_aktif()` untuk filter daerah
- `Program`: membaca dan membersihkan data (`muat_data`), menyaring (`saring`), mengurutkan dengan bubble sort (`urutkan`), mencetak tabel (`cetak_tabel`), ketiga menu utama, dan `main()`

Ada juga tiga fungsi di luar class: `ke_angka()` untuk mengubah teks menjadi angka, serta `baca_csv()` dan `tulis_csv()` untuk membaca dan menulis file akun dan pengaturan.

Format isi file penyimpanan (pemisah `;`):

- `akun.csv`: `username;password`
- `pengaturan.csv`: `username;nama_pengaturan;nilai`

## Keterbatasan

- Hanya memakai data tahun 2020 dan parameter pH, DO, BOD, COD, serta Nilai IP.
- Nilai IP dan status mutu air diambil langsung dari dataset, tidak dihitung ulang oleh program.
- Password disimpan apa adanya di `akun.csv` tanpa enkripsi, jadi program ini hanya cocok untuk latihan.
- Program belum menangani file CSV yang benar-benar kosong (akan error), serta nilai `nan`/`inf` atau nilai yang tidak masuk akal (misalnya pH di atas 14).

## Anggota Kelompok 9A

- Gisella Zashika Zifi (2610931001)
- Muhammad Rauf (2610932020)
- Miftahul Irsyad Hali (2610932040)

Asisten pembimbing: Intan Permata Mustika
Dosen pengampu: Wisnel, S.T., M.Sc.

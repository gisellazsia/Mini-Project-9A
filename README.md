# Analisis Perbandingan Kualitas Air Sungai dan Danau Berdasarkan Rata-Rata Parameter pH, DO, BOD, dan COD untuk Menentukan Prioritas Pemantauan di Provinsi Aceh Tahun 2020

Mini project Pemrograman Komputer, Kelompok 9A.
Laboratorium Sistem Informasi dan Keputusan, Departemen Teknik Industri, Fakultas Teknik, Universitas Andalas.

## Tentang program

Program ini mengolah data kualitas air sungai dan danau di Provinsi Aceh tahun 2020. Parameter yang dipakai ada empat: pH, DO, BOD, dan COD. Dari data itu program bisa menghitung rata-rata tiap lokasi, mencari nilai tertinggi, terendah, atau rentang tertentu, lalu mengurutkan lokasi berdasarkan Nilai IP (Indeks Pencemaran) supaya kelihatan lokasi mana yang sebaiknya dipantau duluan.

Dibuat pakai Python dan dijalankan lewat terminal. Tidak perlu install apa-apa karena hanya memakai modul bawaan (`csv` dan `os`).

## Fitur

- Register dan login (login punya 3 kali kesempatan)
- Rata-rata pH, DO, BOD, dan COD per lokasi, bisa semua lokasi atau satu lokasi saja
- Cari data tertinggi, terendah, atau dalam rentang nilai tertentu
- Prioritas pemantauan, yaitu lokasi diurutkan dari Nilai IP terbesar disertai jumlah titik untuk tiap status mutu air
- Filter daerah (kabupaten/kota, sungai, atau lokasi) yang bisa diganti kapan saja
- Pengaturan terakhir diingat selama program masih jalan
- Setiap tabel ada status tiap nilai beserta keterangan rentang, risiko, dan solusinya

## Data

Datanya dari Open Data Aceh, judulnya "Data Kualitas Air Sungai dan Danau Tahun 2020":
https://data.acehprov.go.id/id/dataset/parameter-kualitas-air-sungai-dan-danau/resource/0ee08406-9f75-426d-82fb-5e7370e12bb7

- Format CSV, dipisah titik koma (`;`), encoding `cp1252`
- 150 baris dan 34 kolom
- Setelah dibersihkan, 149 baris terpakai dan 1 baris dibuang

Sebuah baris dibuang kalau kolomnya kurang dari 34, tahunnya bukan 2020, atau nilai pH, DO, BOD, COD, dan IP-nya kosong atau bukan angka. Tanda `<` di depan angka (misalnya `<3.2234`) dihapus dan koma desimal diganti titik.

## Isi folder

```
main.py                        program utama
data-kualitas-air-sungai.csv   dataset
README.md
```

`main.py` dan file CSV harus ada di satu folder, dan nama CSV-nya harus sama persis seperti di atas. Kalau tidak ketemu, program juga mencoba `data-kualitas-air-sungai (1).csv` dan `data-kualitas-air-sungai(1).csv`.

## Cara menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Taruh `main.py` dan file CSV dalam satu folder.
3. Buka terminal di folder itu, lalu jalankan:

```
python main.py
```

Kalau data berhasil dibaca, muncul tulisan seperti ini:

```
Data dimuat: 149 baris valid, 1 baris dibuang.
```

Kalau file CSV tidak ditemukan, program menampilkan pesan `File data tidak ditemukan` lalu berhenti.

## Cara pakai

Buat akun dulu lewat menu Register (username tidak boleh kosong atau sudah dipakai, password minimal 4 karakter), lalu masuk lewat Login. Setelah login ada lima menu:

| Menu | Fungsi |
| --- | --- |
| 1. Rata-rata per lokasi | Menampilkan rata-rata pH, DO, BOD, dan COD untuk tiap pasangan sungai dan lokasi. Bisa tampil semua (diurutkan dari yang tertinggi berdasarkan pH, DO, BOD, atau COD) atau cari satu lokasi. |
| 2. Cari data | Pilih parameter, lalu pilih tertinggi, terendah, atau rentang. Untuk tertinggi dan terendah, jumlah yang ditampilkan bisa 3, 5, atau semua. Untuk rentang, isi nilai minimum dan maksimum. |
| 3. Prioritas pemantauan | Menampilkan lokasi dengan Nilai IP tertinggi (paling tercemar) lebih dulu, bisa 3, 5, atau semua, lalu ringkasan jumlah titik per status mutu air. |
| 4. Ganti daerah | Mengubah filter daerah. |
| 5. Logout | Kembali ke menu awal. |

Soal filter daerah: waktu pertama kali membuka menu 1, 2, atau 3, program menanyakan filter, misalnya `Aceh Barat`. Kalau dikosongkan, semua data dipakai. Tanda `/` dipakai untuk memisahkan beberapa kata kunci yang semuanya harus cocok, misalnya `Aceh Barat / Krueng Woyla`. Huruf besar dan kecil tidak berpengaruh. Filter ini terus dipakai di menu lain sampai diganti lewat menu 4.

Di menu 2 dan 3, kalau sebelumnya sudah pernah memilih, program akan tanya apakah mau pakai pengaturan yang sama (`y/n`). Akun dan pengaturan hanya tersimpan selama program berjalan, jadi hilang kalau program ditutup.

## Contoh hasil

Dari data 2020 tanpa filter:

- Jumlah lokasi unik (pasangan sungai dan lokasi): 78
- pH tertinggi 8,66 di Krueng Jambo Ayee, Kota Banda Aceh
- pH terendah 6,17 di Krueng Woyla, Kabupaten Aceh Barat
- BOD tertinggi sekitar 31,4 di Danau Aneuk Laot, Kota Sabang
- Nilai IP tertinggi 7,89 di Krueng Lamnyong, Kota Banda Aceh (Cemar Sedang)
- Status mutu air: Cemar Ringan 139 titik, Cemar Sedang 9 titik, Kondisi Baik 1 titik

## Struktur kode

Ada dua class:

- `Akun` berisi `register()` dan `login()`. Akun disimpan di dictionary `self.akun`.
- `Program` berisi `muat_data()` untuk membaca dan membersihkan data, `cetak_tabel()` untuk mencetak tabel, `menu_rata_rata()`, `menu_cari()` (dipakai juga untuk prioritas pemantauan lewat `prioritas=True`), dan `main()`.

Di bagian atas kode ada beberapa konstanta: `PARAMETER`, `KRITERIA`, `NAMA`, `BATAS` (batas status mutu BOD, COD, dan DO), dan `KET` (keterangan rentang, risiko, solusi). Pengaturan pengguna disimpan di dictionary `pref` dengan kunci `(user, nama_pengaturan)`.

Status mutu air mengacu pada PP No. 22 Tahun 2021 Lampiran VI, sedangkan Nilai IP dan statusnya mengacu pada KepMen LH No. 115 Tahun 2003.

## Keterbatasan

- Hanya memakai data 2020 dan parameter pH, DO, BOD, COD, serta Nilai IP.
- Nilai IP dan status mutu air diambil langsung dari dataset, tidak dihitung ulang.
- Akun dan pengaturan hanya ada di memori, jadi hilang saat program ditutup.
- Password disimpan apa adanya tanpa enkripsi, jadi hanya cocok untuk latihan.
- File CSV yang benar-benar kosong akan bikin error, dan nilai `nan`/`inf` atau nilai tidak masuk akal (misalnya pH di atas 14) belum ditangani.

## Anggota Kelompok 9A

- Gisella Zashika Zifi (2610931001)
- Muhammad Rauf (2610932020)
- Miftahul Irsyad Hali (2610932040)

Asisten pembimbing: Intan Permata Mustika
Dosen pengampu: Wisnel, S.T., M.Sc.

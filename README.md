# Analisis Kualitas Air Sungai dan Danau Provinsi Aceh Tahun 2020

**Mini Project Pemrograman Komputer – Kelompok 9A**
Laboratorium Sistem Informasi dan Keputusan, Departemen Teknik Industri, Fakultas Teknik, Universitas Andalas (2026)

Program berbasis Python (CLI) untuk membandingkan kualitas air sungai dan danau di Provinsi Aceh berdasarkan rata-rata parameter **pH, DO, BOD, dan COD**, serta menentukan **prioritas lokasi pemantauan** berdasarkan **Nilai Indeks Pencemaran (IP)** dan status mutu air.

---

## Daftar Isi

- [Latar Belakang](#latar-belakang)
- [Fitur](#fitur)
- [Dataset](#dataset)
- [Struktur Folder](#struktur-folder)
- [Persyaratan](#persyaratan)
- [Cara Menjalankan](#cara-menjalankan)
- [Panduan Penggunaan](#panduan-penggunaan)
- [Daftar Fungsi](#daftar-fungsi)
- [Validasi Data](#validasi-data)
- [Hasil Pengujian](#hasil-pengujian)
- [Batasan](#batasan)
- [Tim](#tim)
- [Referensi](#referensi)

---

## Latar Belakang

Pengolahan dan perbandingan data kualitas air dari banyak lokasi secara manual memakan waktu dan rawan salah hitung. Program ini mengotomatiskan pembacaan data, penghitungan rata-rata parameter per lokasi, pencarian nilai tertinggi/terendah/rentang, dan pengurutan lokasi berdasarkan Nilai IP, sehingga lokasi yang paling perlu dipantau dapat diketahui dengan cepat dan konsisten.

Status mutu air mengacu pada metode Indeks Pencemaran (IP) sesuai **Kepmen LH No. 115 Tahun 2003**, dengan baku mutu **PP No. 22 Tahun 2021**.

## Fitur

| Fitur | Keterangan |
| --- | --- |
| Register & Login | Pembuatan akun dengan password yang di-hash; login maksimal 3 kali percobaan |
| Rata-rata per lokasi | Rata-rata pH, DO, BOD, COD dikelompokkan per sungai dan lokasi sampling, dengan filter kabupaten/sungai/lokasi |
| Cari data | Cari berdasarkan parameter (pH, DO, BOD, COD, Nilai IP) dengan kriteria **tertinggi**, **terendah**, atau **rentang nilai** |
| Prioritas pemantauan | Lokasi diurutkan dari Nilai IP terbesar (paling tercemar) beserta ringkasan jumlah per status mutu air |
| Validasi data | Baris tidak lengkap, bukan tahun 2020, atau berisi nilai tidak valid otomatis dilewati |

## Dataset

| Aspek | Keterangan |
| --- | --- |
| Nama | Data Kualitas Air Sungai dan Danau Tahun 2020 |
| Sumber | [Open Data Aceh](https://data.acehprov.go.id/id/dataset/parameter-kualitas-air-sungai-dan-danau/resource/0ee08406-9f75-426d-82fb-5e7370e12bb7) |
| Jenis | Data sekunder |
| Format | CSV (pemisah `;`, encoding `cp1252`) |
| Ukuran | 150 baris, 34 kolom |
| Hasil pemuatan | 149 baris valid, 1 baris dibuang |

Kolom yang dipakai program:

| Kolom CSV | Nama di program | Kegunaan |
| --- | --- | --- |
| `kemendagri_nama_kabupaten_kota` | `kabupaten` | Filter dan tampilan |
| `tahun` | – | Memilih data tahun 2020 |
| `Nama_Sungai` | `sungai` | Pengelompokan, filter, tampilan |
| `Lokasi_Sampling` | `lokasi` | Pengelompokan, filter, tampilan |
| `pH` | `ph` | Rata-rata, pencarian |
| `Do_(mg/L)` | `do` | Rata-rata, pencarian |
| `BOD_(mg/L)` | `bod` | Rata-rata, pencarian |
| `COD_(mg/L)` | `cod` | Rata-rata, pencarian |
| `Nilai_IP` | `ip` | Pencarian, prioritas pemantauan |
| `Status_MutuAir` | `status` | Tampilan dan ringkasan status |

## Struktur Folder

```
.
├── main.py                        # Program utama (nama file dapat disesuaikan)
├── data-kualitas-air-sungai.csv   # Dataset (harus satu folder dengan program)
└── README.md
```

> Program membaca dataset dari folder yang sama dengan file program. Pastikan nama file CSV persis `data-kualitas-air-sungai.csv`.

## Persyaratan

- Python 3.x
- Hanya memakai pustaka bawaan (`csv`, `os`), **tidak perlu instalasi paket tambahan**

## Cara Menjalankan

```bash
# 1. Clone repository
git clone <url-repository-anda>
cd <nama-folder-repository>

# 2. Pastikan data-kualitas-air-sungai.csv berada di folder yang sama dengan program

# 3. Jalankan
python main.py
```

Saat dijalankan, program menampilkan jumlah data yang berhasil dimuat, misalnya:

```
Data dimuat: 149 baris valid, 1 baris dibuang.
```

## Panduan Penggunaan

### 1. Menu awal

```
=== KUALITAS AIR SUNGAI & DANAU ACEH 2020 ===
 1. Register
 2. Login
 3. Keluar
```

- **Register**: masukkan username baru dan password (minimal 4 karakter). Registrasi gagal jika username kosong atau sudah dipakai.
- **Login**: masukkan username dan password. Tersedia 3 kali percobaan.

### 2. Menu utama (setelah login)

```
=== MENU UTAMA ===
 1. Rata-rata pH, DO, BOD, COD per lokasi
 2. Cari data (tertinggi / terendah / rentang)
 3. Prioritas pemantauan (Nilai IP & status)
 4. Logout
```

**Menu 1 – Rata-rata per lokasi.** Masukkan kata kunci filter (kabupaten, sungai, atau lokasi; tidak peka huruf besar/kecil) atau kosongkan untuk menampilkan semua. Contoh: `Aceh Barat`.

**Menu 2 – Cari data.**
1. Pilih parameter: pH, DO, BOD, COD, atau Nilai IP.
2. Pilih kriteria: tertinggi, terendah, atau rentang nilai.
3. Isi filter (opsional).
4. Untuk tertinggi/terendah, pilih jumlah tampilan (5, 10, atau semua). Untuk rentang, masukkan nilai minimum dan maksimum (batas bersifat inklusif).

**Menu 3 – Prioritas pemantauan.** Pilih jumlah lokasi teratas (5, 10, atau semua). Program menampilkan lokasi dengan Nilai IP tertinggi lebih dulu, lalu ringkasan jumlah titik per status mutu air.

### Contoh hasil (data 2020)

| Pengujian | Hasil |
| --- | --- |
| Jumlah lokasi unik (rata-rata tanpa filter) | 78 lokasi |
| pH tertinggi | 8,66 – Krueng Jambo Ayee, Banda Aceh |
| pH terendah | 6,17 – Krueng Woyla, Aceh Barat |
| BOD tertinggi | ± 31,4 – Danau Aneuk Laot, Sabang |
| Prioritas pertama (IP tertinggi) | 7,89 – Krueng Lamnyong, Banda Aceh (Cemar Sedang) |
| Ringkasan status mutu air | Cemar Ringan 139, Cemar Sedang 9, Kondisi Baik 1 (total 149) |

## Daftar Fungsi

| Fungsi | Deskripsi |
| --- | --- |
| `ke_angka(teks)` | Mengubah teks menjadi float; menghapus `<`, mengganti koma desimal dengan titik; mengembalikan `None` jika gagal |
| `input_password(password)` | Mengubah password menjadi kode hash sederhana |
| `saring(data, kata)` | Menyaring data berdasarkan kabupaten, sungai, atau lokasi (tidak peka huruf besar/kecil) |
| `urutkan(data, kunci, besar_dulu)` | Mengurutkan data dengan bubble sort, menaik atau menurun |
| `pilih_jumlah(total, satuan)` | Meminta pilihan jumlah tampilan: 5, 10, atau semua |
| `register(akun)` | Membuat akun baru |
| `login(akun)` | Verifikasi login dengan maksimal 3 percobaan |
| `muat_data()` | Membaca CSV, menyaring tahun 2020, dan memvalidasi nilai; mengembalikan `(data, dibuang)` |
| `cetak_tabel(hasil, kunci, label)` | Menampilkan hasil dalam bentuk tabel |
| `menu_rata_rata(data)` | Menghitung rata-rata pH, DO, BOD, COD per sungai dan lokasi |
| `menu_cari(data)` | Pencarian tertinggi, terendah, atau rentang nilai |
| `menu_prioritas(data)` | Mengurutkan lokasi berdasarkan Nilai IP dan merangkum status mutu air |
| `main()` | Mengatur alur program dari awal sampai selesai |

## Validasi Data

Saat memuat dataset, sebuah baris akan **dibuang** jika:

- jumlah kolomnya kurang dari 34,
- tahunnya bukan 2020,
- salah satu nilai pH, DO, BOD, COD, atau IP kosong atau tidak dapat dibaca sebagai angka.

Format angka yang ditangani: tanda `<` (mis. `<3.2234` dibaca `3.2234`) dan koma desimal (mis. `2,73` dibaca `2.73`).

## Hasil Pengujian

Pengujian mencakup kategori data normal, nilai batas, dataset kosong, data tidak valid, dan regresi. Skenario yang diuji antara lain:

- pemuatan data (149 valid, 1 dibuang),
- register dan login (password tepat 4 karakter, 3 karakter, username kosong/duplikat, 3 kali salah login),
- filter tidak peka huruf besar/kecil,
- rentang nilai inklusif (mis. pH 6,5–8,5 menghasilkan 142 data),
- penanganan input menu yang tidak valid.

Rincian lengkap test case dan tracing fungsi tersedia pada laporan (Bab III).

## Batasan

- Hanya memproses data kualitas air sungai dan danau Provinsi Aceh **tahun 2020**.
- Parameter dibatasi pada **pH, DO, BOD, COD** (ditambah Nilai IP dan status dari dataset).
- Nilai IP dan status mutu air **diambil dari dataset**, bukan dihitung ulang oleh program.
- Data bersifat sekunder; tidak ada pengambilan sampel atau pengukuran langsung.
- Hash password menggunakan fungsi sederhana untuk keperluan pembelajaran, **bukan** untuk keamanan produksi.
- Hasil pengujian mencatat beberapa kasus yang belum ditangani pada versi saat ini, yaitu file CSV kosong total (`StopIteration`), nilai `nan`/`inf`, dan nilai di luar batas fisik (mis. pH > 14). Perbaikan yang direncanakan: `next(baca, None)`, pemeriksaan `math.isfinite()`, dan validasi rentang nilai.

## Tim

**Kelompok 9A**

| Nama | NIM |
| --- | --- |
| Gisella Zashika Zifi | 2610931001 |
| Muhammad Rauf | 2610932020 |
| Miftahul Irsyad Hali | 2610932040 |

**Asisten Pembimbing:** Intan Permata Mustika
**Dosen Pengampu:** Wisnel, S.T., M.Sc.

## Referensi

- Keputusan Menteri Negara Lingkungan Hidup No. 115 Tahun 2003 tentang Pedoman Penentuan Status Mutu Air.
- Peraturan Pemerintah RI No. 22 Tahun 2021 tentang Penyelenggaraan Perlindungan dan Pengelolaan Lingkungan Hidup.
- Pemerintah Provinsi Aceh (2020). *Data kualitas air sungai dan danau tahun 2020*. Open Data Aceh.
- Effendi, H. (2003). *Telaah Kualitas Air*. Kanisius.
- Kamila, A., dkk. (2024). Penilaian status mutu air Sungai Citarum menggunakan metode indeks pencemaran. *Ruwa Jurai: Jurnal Kesehatan Lingkungan, 18*(2), 84–91.

Daftar pustaka lengkap tersedia pada laporan mini project.

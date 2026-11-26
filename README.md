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
- [Struktur Program](#struktur-program)
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
| Register & Login | Akun disimpan di `akun.csv`; password minimal 4 karakter; login maksimal 3 kali percobaan |
| Daerah aktif | Filter kabupaten/sungai/lokasi disimpan per pengguna dan dipakai di semua menu; dapat diganti lewat menu **Ganti daerah** |
| Rata-rata per lokasi | Rata-rata pH, DO, BOD, COD dikelompokkan per sungai dan lokasi sampling |
| Cari data | Cari berdasarkan parameter (pH, DO, BOD, COD, Nilai IP) dengan kriteria **tertinggi**, **terendah**, atau **rentang nilai** |
| Prioritas pemantauan | Lokasi diurutkan dari Nilai IP terbesar (paling tercemar) beserta ringkasan jumlah titik per status mutu air |
| Pengaturan tersimpan | Pilihan parameter, kriteria, jumlah tampilan, dan rentang nilai disimpan di `pengaturan.csv` dan dapat dipakai ulang pada pencarian berikutnya, bahkan di sesi lain |
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
├── akun.csv                       # Dibuat otomatis saat ada yang register
├── pengaturan.csv                 # Dibuat otomatis saat pengaturan disimpan
└── README.md
```

> Semua file dibaca dan ditulis di folder yang sama dengan file program. Pastikan nama file CSV dataset persis `data-kualitas-air-sungai.csv`. File `akun.csv` dan `pengaturan.csv` tidak perlu dibuat manual.

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
- **Login**: masukkan username dan password. Tersedia 3 kali percobaan dengan informasi sisa percobaan.

### 2. Menu utama (setelah login)

```
=== MENU UTAMA (user: <username>) ===
 1. Rata-rata pH, DO, BOD, COD per lokasi
 2. Cari data (tertinggi / terendah / rentang)
 3. Prioritas pemantauan (Nilai IP & status)
 4. Ganti daerah
 5. Logout
```

**Daerah aktif.** Saat pertama kali membuka menu 1, 2, atau 3, program meminta filter daerah (kabupaten, sungai, atau lokasi; tidak peka huruf besar/kecil; kosong = semua data). Filter ini disimpan dan otomatis dipakai pada pemakaian berikutnya. Contoh: `Aceh Barat`.

**Menu 1 – Rata-rata per lokasi.** Menampilkan rata-rata pH, DO, BOD, dan COD untuk setiap kombinasi sungai dan lokasi pada daerah aktif, beserta total jumlah lokasi.

**Menu 2 – Cari data.**
1. Jika sudah ada pengaturan tersimpan, program menawarkan: `Gunakan pengaturan terakhir ini? (y/n)`.
2. Jika tidak memakai pengaturan lama: pilih parameter (pH, DO, BOD, COD, atau Nilai IP), lalu kriteria (tertinggi, terendah, atau rentang nilai).
3. Untuk tertinggi/terendah, pilih jumlah tampilan (5, 10, atau semua). Untuk rentang, masukkan nilai minimum dan maksimum (batas bersifat inklusif).
4. Pilihan disimpan sebagai pengaturan terakhir.

**Menu 3 – Prioritas pemantauan.** Lokasi pada daerah aktif diurutkan dari Nilai IP terbesar. Pilih jumlah lokasi teratas (5, 10, atau semua) atau pakai pengaturan terakhir. Program juga menampilkan ringkasan jumlah titik per status mutu air.

**Menu 4 – Ganti daerah.** Mengubah filter daerah aktif dan menyimpannya.

**Menu 5 – Logout.** Kembali ke menu awal.

### Contoh hasil (data 2020, tanpa filter)

| Pengujian | Hasil |
| --- | --- |
| Jumlah lokasi unik (rata-rata tanpa filter) | 78 lokasi |
| pH tertinggi | 8,66 – Krueng Jambo Ayee, Banda Aceh |
| pH terendah | 6,17 – Krueng Woyla, Aceh Barat |
| BOD tertinggi | ± 31,4 – Danau Aneuk Laot, Sabang |
| Prioritas pertama (IP tertinggi) | 7,89 – Krueng Lamnyong, Banda Aceh (Cemar Sedang) |
| Ringkasan status mutu air | Cemar Ringan 139, Cemar Sedang 9, Kondisi Baik 1 (total 149) |

## Struktur Program

Program disusun dalam tiga class dan dua fungsi bantu untuk file CSV.

**Fungsi bantu**

| Fungsi | Deskripsi |
| --- | --- |
| `ke_angka(teks)` | Mengubah teks menjadi float; menghapus `<` dan mengganti koma desimal dengan titik; mengembalikan `None` jika gagal |
| `baca_csv(path)` | Membaca file CSV (pemisah `;`) menjadi daftar baris; mengembalikan daftar kosong jika file belum ada |
| `tulis_csv(path, baris_semua)` | Menulis daftar baris ke file CSV (pemisah `;`) |

**Class `Akun`**

| Method | Deskripsi |
| --- | --- |
| `register()` | Membuat akun baru dan menyimpannya ke `akun.csv` |
| `login()` | Memverifikasi username dan password (maksimal 3 percobaan); mengembalikan username atau `None` |

**Class `Pengaturan`**

| Method | Deskripsi |
| --- | --- |
| `simpan(user, nama, nilai)` | Menyimpan satu pengaturan pengguna ke `pengaturan.csv` |
| `daerah_aktif(user, ganti=False)` | Mengambil filter daerah aktif; meminta input baru jika belum ada atau jika `ganti=True` |

**Class `Program`**

| Method | Deskripsi |
| --- | --- |
| `muat_data()` | Membaca dataset, menyaring tahun 2020, memvalidasi nilai; mengembalikan `(data, dibuang)` |
| `saring(data, kata)` | Menyaring data berdasarkan kabupaten, sungai, atau lokasi (tidak peka huruf besar/kecil) |
| `urutkan(data, kunci, besar_dulu)` | Mengurutkan data dengan bubble sort, menaik atau menurun |
| `pilih_jumlah(satuan)` | Meminta pilihan jumlah tampilan: 5, 10, atau semua |
| `cetak_tabel(hasil, kunci, label)` | Menampilkan hasil dalam bentuk tabel |
| `menu_rata_rata(data, user)` | Rata-rata pH, DO, BOD, COD per sungai dan lokasi |
| `menu_cari(data, user)` | Pencarian tertinggi, terendah, atau rentang nilai dengan pengaturan tersimpan |
| `menu_prioritas(data, user)` | Pengurutan lokasi berdasarkan Nilai IP dan ringkasan status mutu air |
| `main()` | Mengatur alur program dari awal sampai selesai |

**Format file penyimpanan** (pemisah `;`, encoding UTF-8)

| File | Isi per baris |
| --- | --- |
| `akun.csv` | `username;password` |
| `pengaturan.csv` | `username;nama_pengaturan;nilai` |

Nama pengaturan yang disimpan: `daerah`, `param`, `kriteria`, `jumlah`, `bawah`, `atas`, `jml_prioritas`.

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
- Password disimpan apa adanya (tanpa enkripsi/hash) di `akun.csv`, sehingga program ini hanya untuk keperluan pembelajaran dan **tidak** untuk penggunaan produksi.
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

import csv
import os

folder = os.path.dirname(os.path.abspath(__file__))
file_data = os.path.join(folder, "data-kualitas-air-sungai.csv")

if not os.path.exists(file_data):
    for nama_alternatif in ("data-kualitas-air-sungai (1).csv", "data-kualitas-air-sungai(1).csv"):
        kandidat = os.path.join(folder, nama_alternatif)
        if os.path.exists(kandidat):
            file_data = kandidat
            break

PARAMETER = {"1": ("ph", "pH"), "2": ("do", "DO (mg/L)"), "3": ("bod", "BOD (mg/L)"),
             "4": ("cod", "COD (mg/L)"), "5": ("ip", "Nilai IP")}
KRITERIA = {"1": "Tertinggi", "2": "Terendah", "3": "Rentang nilai"}

NAMA = ["Sangat Baik", "Baik", "Sedang", "Buruk", "Sangat Buruk"]
BATAS = {"bod": [2, 3, 6, 12], "cod": [10, 25, 40, 80], "do": [6, 4, 3, 1]}

KET = {
    "ph": [("< 6", "Asam", "korosif, logam berat larut, ikan stres", "netralisasi limbah asam"),
           ("6 - 9", "Baik", "risiko rendah", "pertahankan, pantau rutin"),
           ("> 9", "Basa", "amonia lebih toksik, insang ikan terganggu", "kendalikan limbah basa/deterjen")],
    "bod": [("<= 2", "Sangat Baik", "bahan organik sangat sedikit", "pertahankan kualitas"),
            ("> 2 - 3", "Baik", "bahan organik rendah", "pantau rutin"),
            ("> 3 - 6", "Sedang", "oksigen mulai menurun", "bangun IPAL, kurangi limbah domestik"),
            ("> 6 - 12", "Buruk", "pencemaran organik tinggi", "wajibkan olah limbah sebelum dibuang"),
            ("> 12", "Sangat Buruk", "ekosistem terancam, bau, penyakit", "hentikan sumber pencemar, restorasi")],
    "cod": [("<= 10", "Sangat Baik", "pencemar sangat sedikit", "pertahankan kualitas"),
            ("> 10 - 25", "Baik", "pencemar rendah", "pantau rutin"),
            ("> 25 - 40", "Sedang", "pencemar kimia mulai tinggi", "perketat izin buangan, pasang IPAL"),
            ("> 40 - 80", "Buruk", "mengganggu kehidupan air", "olah limbah industri, audit sumber"),
            ("> 80", "Sangat Buruk", "berpotensi toksik bagi biota", "hentikan pencemar, remediasi")],
    "do": [(">= 6", "Sangat Baik", "oksigen sangat cukup", "pertahankan, jaga sempadan sungai"),
           ("4 - < 6", "Baik", "oksigen cukup", "pantau rutin"),
           ("3 - < 4", "Sedang", "ikan sensitif mulai terganggu", "kurangi beban organik"),
           ("1 - < 3", "Buruk", "banyak biota mati", "aerasi, kurangi limbah organik"),
           ("< 1", "Sangat Buruk", "kondisi anaerob, bau busuk", "hentikan pencemar, restorasi")],
    "ip": [("0 - 1", "Memenuhi Baku Mutu", "risiko rendah", "pertahankan, pantau rutin"),
           ("> 1 - 5", "Cemar Ringan", "kualitas mulai turun", "telusuri sumber pencemar"),
           ("> 5 - 10", "Cemar Sedang", "pemanfaatan air terbatas", "bangun IPAL, prioritaskan pemantauan"),
           ("> 10", "Cemar Berat", "risiko kesehatan tinggi", "penanganan segera, restorasi")],
}

pref = {}  

class Akun:
    def __init__(self):
        self.akun = {}

    def register(self):
        print("\n--- REGISTER ---")
        username = input("Username baru: ").strip()
        password = input("Password (min. 4 karakter): ")
        if username == "":
            print("Register gagal: username kosong.")
        elif username in self.akun:
            print("Register gagal: username sudah dipakai.")
        elif len(password) < 4:
            print("Register gagal: password terlalu pendek.")
        else:
            self.akun[username] = password
            print("Register berhasil! Silakan login.")

    def login(self):
        print("\n--- LOGIN ---")
        for i in range(3):
            username = input("Username: ").strip()
            password = input("Password: ")
            if username in self.akun and self.akun[username] == password:
                print("Login berhasil. Selamat datang,", username)
                return username
            print("Username/password salah. Sisa percobaan:", 2 - i)
        return None


class Program:
    def __init__(self):
        self.file_data = file_data

    def muat_data(self):
        data = []
        dibuang = 0
        with open(self.file_data, newline="", encoding="cp1252") as f:
            baca = csv.reader(f, delimiter=";")
            next(baca)
            for baris in baca:
                if len(baris) < 34 or baris[4].strip() != "2020":
                    dibuang += 1
                    continue
                try:
                    angka = [float(baris[i].strip().replace("<", "").replace(",", "."))
                             for i in (10, 14, 17, 18, 32)]
                except ValueError:
                    dibuang += 1
                    continue
                data.append({"kabupaten": baris[3].strip(), "sungai": baris[5].strip(),
                             "lokasi": baris[7].strip(), "ph": angka[0], "do": angka[1],
                             "bod": angka[2], "cod": angka[3], "ip": angka[4],
                             "status": baris[33].strip()})
        return data, dibuang

    def cetak_tabel(self, hasil, daftar, label):
        if len(hasil) == 0:
            print("Data tidak ditemukan.")
            return
        print("\nParameter:", label)
        ada_kab = "kabupaten" in hasil[0]
        kepala = "{:<3} ".format("No") + ("{:<22} ".format("Kabupaten/Kota") if ada_kab else "")
        kepala += "{:<20} {:<34}".format("Sungai", "Lokasi")
        for k in daftar:
            nama = "Nilai" if len(daftar) == 1 else ("pH" if k == "ph" else k.upper())
            kepala += " {:>7} {:<12}".format(nama, "Status")
        print(kepala)
        print("-" * len(kepala))
        for no, d in enumerate(hasil, 1):
            baris = "{:<3} ".format(no)
            if ada_kab:
                baris += "{:<22} ".format(d["kabupaten"][:22])
            baris += "{:<20} {:<34}".format(d["sungai"][:20], d["lokasi"][:34])
            for k in daftar:
                n = d[k]
                if k == "ip":
                    st = d["status"]
                elif k == "ph":
                    st = "Asam" if n < 6 else "Basa" if n > 9 else "Baik"
                else:
                    st = NAMA[4]
                    for i, b in enumerate(BATAS[k]):
                        if (n >= b) if k == "do" else (n <= b):
                            st = NAMA[i]
                            break
                baris += " {:>7.2f} {:<12}".format(n, st)
            print(baris)
        print("Total:", len(hasil), "data" if ada_kab else "lokasi")
        print("\nKETERANGAN (acuan: PP 22/2021 Lampiran VI; IP: KepMen LH 115/2003)")
        for k in daftar:
            print(k.upper() + ":")
            for rentang, st, risiko, solusi in KET[k]:
                print(f"  {rentang}: {st} | Risiko: {risiko} | Solusi: {solusi}")

    def menu_rata_rata(self, data, user):
        print("\n--- RATA-RATA PER LOKASI ---")
        kata_daerah = pref.get((user, "daerah"))
        if kata_daerah is None:
            kata_daerah = input("Filter (contoh: Aceh Barat / Krueng Woyla, kosong = semua): ").strip()
            pref[(user, "daerah")] = kata_daerah if kata_daerah != "" else "*"
            print("(Daerah disimpan)")
        elif kata_daerah == "*":
            kata_daerah = ""
        print("Daerah aktif:", kata_daerah if kata_daerah != "" else "(semua)")
        bagian_daerah = [b.strip().lower() for b in kata_daerah.split("/") if b.strip() != ""]
        data_daerah = [d for d in data
                       if all(b in (d["kabupaten"] + " " + d["sungai"] + " " + d["lokasi"]).lower()
                              for b in bagian_daerah)]
        kelompok = {}
        for d in data_daerah:
            kelompok.setdefault((d["sungai"], d["lokasi"]), []).append(d)
        if len(kelompok) == 0:
            print("Data tidak ditemukan.")
            return
        hasil = []
        for (sungai, lokasi), daftar in kelompok.items():
            item = {"sungai": sungai, "lokasi": lokasi}
            for p in ["ph", "do", "bod", "cod"]:
                item[p] = sum(x[p] for x in daftar) / len(daftar)
            hasil.append(item)
        print("1. Tampilkan semua lokasi\n2. Cari 1 lokasi")
        mode = input("Pilih (1-2): ").strip()
        if mode == "2":
            kata = input("Nama sungai/lokasi yang dicari: ").strip().lower()
            cocok = [r for r in hasil if kata != "" and kata in (r["sungai"] + " " + r["lokasi"]).lower()]
            if len(cocok) == 0:
                print("Lokasi tidak ditemukan.")
                return
            if len(cocok) > 1:
                print("\nDitemukan", len(cocok), "lokasi:")
                for no, r in enumerate(cocok, 1):
                    print(f"  {no}. {r['sungai']} - {r['lokasi']}")
                pilih = input("Pilih nomor lokasi: ").strip()
                if not pilih.isdigit() or not 1 <= int(pilih) <= len(cocok):
                    print("Pilihan tidak valid.")
                    return
                cocok = [cocok[int(pilih) - 1]]
            hasil = cocok
            print("\nHasil pencarian 1 lokasi")
        elif mode == "1":
            print("Urutkan tertinggi ke terendah berdasarkan: 1. pH  2. DO  3. BOD  4. COD")
            p = input("Pilih (1-4): ").strip()
            if p not in ("1", "2", "3", "4"):
                print("Pilihan tidak valid.")
                return
            hasil = sorted(hasil, key=lambda r: r[PARAMETER[p][0]], reverse=True)
            print("\nDiurutkan berdasarkan rata-rata", PARAMETER[p][1])
        else:
            print("Pilihan tidak valid.")
            return
        self.cetak_tabel(hasil, ["ph", "do", "bod", "cod"], "Rata-rata per lokasi")

    def menu_cari(self, data, user, prioritas=False):
        if prioritas:
            print("\n--- PRIORITAS PEMANTAUAN (Nilai IP) ---")
            print("Lokasi diurutkan dari Nilai IP terbesar (paling tercemar) ke terkecil.")
        else:
            print("\n--- CARI DATA ---")
        kata_daerah = pref.get((user, "daerah"))
        if kata_daerah is None:
            kata_daerah = input("Filter (contoh: Aceh Barat / Krueng Woyla, kosong = semua): ").strip()
            pref[(user, "daerah")] = kata_daerah if kata_daerah != "" else "*"
            print("(Daerah disimpan)")
        elif kata_daerah == "*":
            kata_daerah = ""
        print("Daerah aktif:", kata_daerah if kata_daerah != "" else "(semua)")
        bagian_daerah = [b.strip().lower() for b in kata_daerah.split("/") if b.strip() != ""]
        data_daerah = [d for d in data
                       if all(b in (d["kabupaten"] + " " + d["sungai"] + " " + d["lokasi"]).lower()
                              for b in bagian_daerah)]
        terfilter = data_daerah
        nama_jml = "jml_prioritas" if prioritas else "jumlah"
        satuan = "lokasi" if prioritas else "data"
        if prioritas:
            param, kriteria = "5", "1"
            ada = (user, nama_jml) in pref
        else:
            param = pref.get((user, "param"))
            kriteria = pref.get((user, "kriteria"))
            ada = param is not None and kriteria is not None
        pakai = False
        if ada:
            if prioritas:
                print("Pengaturan terakhir -> Jumlah lokasi teratas:", pref[(user, nama_jml)])
            else:
                print("Pengaturan terakhir -> Parameter:", PARAMETER[param][1],
                      "| Kriteria:", KRITERIA[kriteria])
            pakai = input("Gunakan pengaturan terakhir ini? (y/n): ").strip().lower() == "y"
        if not pakai:
            if not prioritas:
                print("  1. pH\n  2. DO (mg/L)\n  3. BOD (mg/L)\n  4. COD (mg/L)")
                param = input("Pilih parameter (1-4): ").strip()
                if param not in ("1", "2", "3", "4"):
                    print("Pilihan tidak valid.")
                    return
                print("Kriteria: 1. Tertinggi  2. Terendah  3. Rentang nilai")
                kriteria = input("Pilih kriteria (1-3): ").strip()
                if kriteria not in KRITERIA:
                    print("Kriteria tidak valid.")
                    return
            if kriteria == "3":
                bawah = input("Nilai minimum (contoh: 6.5): ").strip()
                atas = input("Nilai maksimum (contoh: 8.5): ").strip()
                try:
                    urut_benar = float(bawah.replace(",", ".")) <= float(atas.replace(",", "."))
                except ValueError:
                    print("Nilai harus berupa angka.")
                    return
                if not urut_benar:
                    print("Nilai minimum tidak boleh lebih besar dari nilai maksimum.")
                    return
                pref[(user, "bawah")] = bawah
                pref[(user, "atas")] = atas
            else:
                print("Tampilkan berapa", satuan + "?")
                print("  1. 3 " + satuan + "\n  2. 5 " + satuan + "\n  3. Semua " + satuan)
                pilih = input("Pilih (1-3): ").strip()
                if pilih not in ("1", "2", "3"):
                    print("Pilihan tidak valid.")
                    return
                pref[(user, nama_jml)] = {"1": "3", "2": "5", "3": "semua"}[pilih]
            if not prioritas:
                pref[(user, "param")] = param
                pref[(user, "kriteria")] = kriteria
            print("(Pengaturan disimpan)")
        kunci, label = PARAMETER[param]
        if kriteria == "3":
            bawah = float(pref[(user, "bawah")].replace(",", "."))
            atas = float(pref[(user, "atas")].replace(",", "."))
            hasil = [d for d in terfilter if bawah <= d[kunci] <= atas]
        else:
            kandidat = terfilter
            if prioritas:
                terbaik = {}
                for d in terfilter:
                    k = (d["sungai"], d["lokasi"])
                    if k not in terbaik or d["ip"] > terbaik[k]["ip"]:
                        terbaik[k] = d
                kandidat = list(terbaik.values())
            kode = pref[(user, nama_jml)]
            jumlah = len(kandidat) if kode == "semua" else int(kode)
            hasil = sorted(kandidat, key=lambda d: d[kunci], reverse=(kriteria == "1"))[:jumlah]
        self.cetak_tabel(hasil, [kunci], label)
        if prioritas:
            hitung = {}
            for d in terfilter:
                hitung[d["status"]] = hitung.get(d["status"], 0) + 1
            print("\nRingkasan status mutu air:")
            for st in sorted(hitung):
                print("  -", st + ":", hitung[st], "titik")

    def main(self):
        akun = Akun()
        if not os.path.exists(self.file_data):
            print("File data tidak ditemukan:", file_data)
            return
        data, dibuang = self.muat_data()
        print("Data dimuat:", len(data), "baris valid,", dibuang, "baris dibuang.")
        while True:
            print("\n=== KUALITAS AIR SUNGAI & DANAU ACEH 2020 ===")
            print(" 1. Register\n 2. Login\n 3. Keluar")
            pilih = input("Pilih (1-3): ").strip()
            if pilih == "1":
                akun.register()
            elif pilih == "2":
                user = akun.login()
                while user is not None:
                    print("\n=== MENU UTAMA (user:", user + ") ===")
                    print(" 1. Rata-rata pH, DO, BOD, COD per lokasi")
                    print(" 2. Cari data (tertinggi / terendah / rentang)")
                    print(" 3. Prioritas pemantauan (Nilai IP & status)")
                    print(" 4. Ganti daerah")
                    print(" 5. Logout")
                    menu = input("Pilih menu (1-5): ").strip()
                    if menu == "1":
                        self.menu_rata_rata(data, user)
                    elif menu == "2":
                        self.menu_cari(data, user)
                    elif menu == "3":
                        self.menu_cari(data, user, prioritas=True)
                    elif menu == "4":
                        print("\n--- GANTI DAERAH ---")
                        kata_daerah = input("Filter (contoh: Aceh Barat / Krueng Woyla, kosong = semua): ").strip()
                        pref[(user, "daerah")] = kata_daerah if kata_daerah != "" else "*"
                        print("(Daerah disimpan)")
                        if kata_daerah == "*":
                            kata_daerah = ""
                        print("Daerah aktif:", kata_daerah if kata_daerah != "" else "(semua)")
                        bagian_daerah = [b.strip().lower() for b in kata_daerah.split("/") if b.strip() != ""]
                        data_daerah = [d for d in data
                                       if all(b in (d["kabupaten"] + " " + d["sungai"] + " " + d["lokasi"]).lower()
                                              for b in bagian_daerah)]
                    elif menu == "5":
                        print("Anda telah logout.")
                        user = None
                    else:
                        print("Pilihan tidak valid.")
            elif pilih == "3":
                print("Terima kasih.")
                break
            else:
                print("Pilihan tidak valid.")


if __name__ == "__main__":
    Program().main()



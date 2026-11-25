import csv
import os

folder = os.path.dirname(os.path.abspath(__file__))
file_data = os.path.join(folder, "data-kualitas-air-sungai.csv")

def ke_angka(teks):
    teks = teks.strip().replace("<", "").replace(",", ".")
    try:
        return float(teks)
    except ValueError:
        return None


class Akun:
    def register(akun):
        print("\n--- REGISTER ---")
        username = input("Username baru: ").strip()
        password = input("Password (min. 4 karakter): ")

        if username == "":
            print("Register gagal: username kosong.")
        elif username in akun:
            print("Register gagal: username sudah dipakai.")
        elif len(password) < 4:
            print("Register gagal: password terlalu pendek.")
        else:
            akun[username] = password
            print("Register berhasil! Silakan login.")

    def login(akun):
        print("\n--- LOGIN ---")
        for i in range(3):
            username = input("Username: ").strip()
            password = input("Password: ")
            if username in akun and akun[username] == password:
                print("Login berhasil. Selamat datang,", username)
                return username
            print("Username/password salah. Sisa percobaan:", 2 - i)
        return None


class Program:
    def saring(data, kata):
        hasil = []
        for d in data:
            teks = d["kabupaten"] + " " + d["sungai"] + " " + d["lokasi"]
            if kata.lower() in teks.lower():
                hasil.append(d)
        return hasil

    def urutkan(data, kunci, besar_dulu):
        hasil = data[:]
        n = len(hasil)
        for i in range(n):
            for j in range(n - 1 - i):
                if besar_dulu:
                    tukar = hasil[j][kunci] < hasil[j + 1][kunci]
                else:
                    tukar = hasil[j][kunci] > hasil[j + 1][kunci]
                if tukar:
                    temp = hasil[j]
                    hasil[j] = hasil[j + 1]
                    hasil[j + 1] = temp
        return hasil

    def pilih_jumlah(total, satuan):
        print("Tampilkan berapa", satuan + "?")
        print("  1. 5 " + satuan)
        print("  2. 10 " + satuan)
        print("  3. Semua " + satuan)
        pilih = input("Pilih (1-3): ").strip()
        if pilih == "1":
            return 5
        elif pilih == "2":
            return 10
        elif pilih == "3":
            return total
        else:
            print("Pilihan tidak valid.")
            return None

    def muat_data():
        data = []
        dibuang = 0
        f = open(file_data, newline="", encoding="cp1252")
        baca = csv.reader(f, delimiter=";")
        next(baca)
        for baris in baca:
            if len(baris) < 34 or baris[4].strip() != "2020":
                dibuang += 1
                continue
            d = {}
            d["kabupaten"] = baris[3].strip()
            d["sungai"] = baris[5].strip()
            d["lokasi"] = baris[7].strip()
            d["ph"] = ke_angka(baris[10])
            d["do"] = ke_angka(baris[14])
            d["bod"] = ke_angka(baris[17])
            d["cod"] = ke_angka(baris[18])
            d["ip"] = ke_angka(baris[32])
            d["status"] = baris[33].strip()

            if d["ph"] is None or d["do"] is None or d["bod"] is None \
                    or d["cod"] is None or d["ip"] is None:
                dibuang += 1
                continue
            data.append(d)
        f.close()
        return data, dibuang

    def cetak_tabel(hasil, kunci, label):
        if len(hasil) == 0:
            print("Data tidak ditemukan.")
            return
        print("\nParameter:", label)
        print("{:<3} {:<22} {:<20} {:<34} {:>7}  {}".format(
            "No", "Kabupaten/Kota", "Sungai", "Lokasi", "Nilai", "Status"))
        print("-" * 103)
        no = 1
        for d in hasil:
            print("{:<3} {:<22} {:<20} {:<34} {:>7.2f}  {}".format(
                no, d["kabupaten"][:22], d["sungai"][:20],
                d["lokasi"][:34], d[kunci], d["status"]))
            no += 1
        print("Total:", len(hasil), "data")

    def menu_rata_rata(data):
        print("\n--- RATA-RATA PER LOKASI ---")
        kata = input("Filter (contoh: Aceh Barat / Krueng Woyla, kosong = semua): ").strip()
        terfilter = Program.saring(data, kata)

        kelompok = {}
        for d in terfilter:
            kunci = (d["sungai"], d["lokasi"])
            if kunci not in kelompok:
                kelompok[kunci] = []
            kelompok[kunci].append(d)

        if len(kelompok) == 0:
            print("Data tidak ditemukan.")
            return

        print("\n{:<20} {:<40} {:>6} {:>6} {:>7} {:>8}".format(
            "Sungai", "Lokasi", "pH", "DO", "BOD", "COD"))
        print("-" * 92)
        for kunci in kelompok:
            daftar = kelompok[kunci]
            n = len(daftar)
            total_ph = 0
            total_do = 0
            total_bod = 0
            total_cod = 0
            for x in daftar:
                total_ph += x["ph"]
                total_do += x["do"]
                total_bod += x["bod"]
                total_cod += x["cod"]
            print("{:<20} {:<40} {:>6.2f} {:>6.2f} {:>7.2f} {:>8.2f}".format(
                kunci[0][:20], kunci[1][:40],
                total_ph / n, total_do / n, total_bod / n, total_cod / n))
        print("Total:", len(kelompok), "lokasi")

    def menu_cari(data):
        print("\n--- CARI DATA ---")
        print("  1. pH")
        print("  2. DO (mg/L)")
        print("  3. BOD (mg/L)")
        print("  4. COD (mg/L)")
        print("  5. Nilai IP")
        pilih = input("Pilih parameter (1-5): ").strip()

        if pilih == "1":
            kunci = "ph"
            label = "pH"
        elif pilih == "2":
            kunci = "do"
            label = "DO (mg/L)"
        elif pilih == "3":
            kunci = "bod"
            label = "BOD (mg/L)"
        elif pilih == "4":
            kunci = "cod"
            label = "COD (mg/L)"
        elif pilih == "5":
            kunci = "ip"
            label = "Nilai IP"
        else:
            print("Pilihan tidak valid.")
            return

        print("Kriteria: 1. Tertinggi  2. Terendah  3. Rentang nilai")
        kriteria = input("Pilih kriteria (1-3): ").strip()
        kata = input("Filter (contoh: Aceh Barat / Krueng Woyla, kosong = semua): ").strip()
        terfilter = Program.saring(data, kata)

        if kriteria == "1" or kriteria == "2":
            jumlah = Program.pilih_jumlah(len(terfilter), "data")
            if jumlah is None:
                return
            urut = Program.urutkan(terfilter, kunci, kriteria == "1")
            hasil = urut[:jumlah]
        elif kriteria == "3":
            bawah = ke_angka(input("Nilai minimum (contoh: 6.5): "))
            atas = ke_angka(input("Nilai maksimum (contoh: 8.5): "))
            if bawah is None or atas is None:
                print("Nilai harus berupa angka.")
                return
            hasil = []
            for d in terfilter:
                if d[kunci] >= bawah and d[kunci] <= atas:
                    hasil.append(d)
        else:
            print("Kriteria tidak valid.")
            return

        Program.cetak_tabel(hasil, kunci, label)

    def menu_prioritas(data):
        print("\n--- PRIORITAS PEMANTAUAN (Nilai IP) ---")
        print("Lokasi diurutkan dari Nilai IP terbesar (paling tercemar) ke terkecil.")
        print("Pilih berapa lokasi dari urutan paling atas yang ingin dilihat.")
        jumlah = Program.pilih_jumlah(len(data), "lokasi")
        if jumlah is None:
            return

        urut = Program.urutkan(data, "ip", True)
        Program.cetak_tabel(urut[:jumlah], "ip", "Nilai IP")

        hitung = {}
        for d in data:
            if d["status"] in hitung:
                hitung[d["status"]] += 1
            else:
                hitung[d["status"]] = 1
        print("\nRingkasan status mutu air:")
        for status in hitung:
            print("  -", status + ":", hitung[status], "titik")

    def main():
        if not os.path.exists(file_data):
            print("File data tidak ditemukan:", file_data)
            return

        data, dibuang = Program.muat_data()
        print("Data dimuat:", len(data), "baris valid,", dibuang, "baris dibuang.")

        akun = {}

        while True:
            print("\n=== KUALITAS AIR SUNGAI & DANAU ACEH 2020 ===")
            print(" 1. Register")
            print(" 2. Login")
            print(" 3. Keluar")
            pilih = input("Pilih (1-3): ").strip()

            if pilih == "1":
                Akun.register(akun)
            elif pilih == "2":
                user = Akun.login(akun)
                while user is not None:
                    print("\n=== MENU UTAMA (user:", user + ") ===")
                    print(" 1. Rata-rata pH, DO, BOD, COD per lokasi")
                    print(" 2. Cari data (tertinggi / terendah / rentang)")
                    print(" 3. Prioritas pemantauan (Nilai IP & status)")
                    print(" 4. Logout")
                    menu = input("Pilih menu (1-4): ").strip()

                    if menu == "1":
                        Program.menu_rata_rata(data)
                    elif menu == "2":
                        Program.menu_cari(data)
                    elif menu == "3":
                        Program.menu_prioritas(data)
                    elif menu == "4":
                        print("Anda telah logout.")
                        user = None
                    else:
                        print("Pilihan tidak valid.")
            elif pilih == "3":
                print("Terima kasih.")
                break
            else:
                print("Pilihan tidak valid.")


Program.main()
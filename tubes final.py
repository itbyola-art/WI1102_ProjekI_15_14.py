# Program pembelajaran: Smart Diet Tracker (versi dengan array/list).
# Nilai kalori makanan dan olahraga adalah asumsi sederhana, bukan data gizi resmi.
# Olahraga dihitung per 30 menit (jogging 300 kalori, bersepeda 200 kalori).

# KAMUS
# nama : string
# target_kalori, target_air_minum : float
# total_kalori_masuk, kalori_terbakar, total_minuman_masuk : float
# nama_makanan, nama_olahraga : list of string
# kalori_makanan, bakar_per_30_menit : list of float
# riwayat_makanan, riwayat_olahraga, riwayat_minuman : list
# pilihan : string
# menu_makanan, olahraga, idx, i : integer
# porsi, kalori, durasi, bakar, air_harian : float
# kalori_bersih, sisa, sisa_air : float

# Algoritma

# Data menu disimpan dalam array (list)
nama_makanan = ["Nasi Putih", "Ayam Goreng", "Telur Rebus", "Sayur / Buah"]
kalori_makanan = [200, 260, 75, 50]

nama_olahraga = ["Jogging", "Bersepeda"]
bakar_per_30_menit = [300, 200]

# Array untuk menyimpan riwayat pencatatan
riwayat_makanan = []
riwayat_olahraga = []
riwayat_minuman = []

print("=== PROGRAM SMART DIET TRACKER ===")

# 1. Input Data Pengguna
nama = input("Masukkan nama Anda: ")
target_kalori = float(input("Masukkan target kalori harian: "))
target_air_minum = float(input("Masukkan target air minum harian (ml): "))

total_kalori_masuk = 0
kalori_terbakar = 0
total_minuman_masuk = 0

# 2. Perulangan Menu Utama
while True:
    print("\n--- MENU UTAMA ---")
    print("1. Catat Makanan")
    print("2. Catat Olahraga")
    print("3. Catat konsumsi minuman harian")
    print("4. Selesai & Lihat Hasil")

    pilihan = input("Pilih menu (1/2/3/4): ")

    # Pilihan 1: Catat Makanan
    if pilihan == "1":
        print("\nPilih Makanan:")
        for i in range(len(nama_makanan)):
            print(f"{i + 1}. {nama_makanan[i]} ({kalori_makanan[i]} kalori)")

        # Langsung diubah ke angka (int), jadi tidak perlu isdigit()
        menu_makanan = int(input(f"Pilih nomor makanan (1-{len(nama_makanan)}): "))
        porsi = float(input("Masukkan jumlah porsi: "))

        if porsi <= 0:
            print("Porsi harus lebih dari 0!")
            continue

        if 1 <= menu_makanan <= len(nama_makanan):
            idx = menu_makanan - 1
            kalori = porsi * kalori_makanan[idx]
            print("-> Berhasil tambah", nama_makanan[idx])
        else:
            print("Pilihan tidak ada!")
            continue

        total_kalori_masuk = total_kalori_masuk + kalori
        riwayat_makanan.append(f"{nama_makanan[idx]} x{porsi} = {kalori} kalori")

    # Pilihan 2: Catat Olahraga
    elif pilihan == "2":
        print("\nPilih Olahraga:")
        for i in range(len(nama_olahraga)):
            print(f"{i + 1}. {nama_olahraga[i]} (bakar ~{bakar_per_30_menit[i]} kalori per 30 menit)")

        olahraga = int(input(f"Pilih nomor olahraga (1-{len(nama_olahraga)}): "))
        durasi = float(input("Masukkan durasi (menit): "))

        if durasi <= 0:
            print("Durasi harus lebih dari 0!")
            continue

        if 1 <= olahraga <= len(nama_olahraga):
            idx = olahraga - 1
            bakar = (durasi / 30) * bakar_per_30_menit[idx]
            print("-> Berhasil catat", nama_olahraga[idx])
        else:
            print("Pilihan tidak ada!")
            continue

        kalori_terbakar = kalori_terbakar + bakar
        riwayat_olahraga.append(f"{nama_olahraga[idx]} {durasi} menit = {bakar} kalori terbakar")

    # Pilihan 3: Catat air minum harian
    elif pilihan == "3":
        air_harian = float(input("Masukkan jumlah air yang dikonsumsi hari ini (ml): "))

        if air_harian <= 0:
            print("Jumlah air harus lebih dari 0!")
            continue

        total_minuman_masuk += air_harian
        riwayat_minuman.append(air_harian)
        print(f"-> Berhasil menambah {air_harian} ml air minum!")

    # Pilihan 4: Keluar dan Selesai
    elif pilihan == "4":
        break
    else:
        print("Pilihan salah, silakan pilih 1, 2, 3, atau 4!")

# 3. Hasil Rekapitulasi Akhir
kalori_bersih = total_kalori_masuk - kalori_terbakar
sisa = target_kalori - kalori_bersih
sisa_air = target_air_minum - total_minuman_masuk

print("\n=== REKAPITULASI AKHIR ===")
print("Nama Pengguna      :", nama)

print("\n--- Riwayat Makanan ---")
if len(riwayat_makanan) == 0:
    print("(belum ada makanan dicatat)")
else:
    for i in range(len(riwayat_makanan)):
        print(f"{i + 1}. {riwayat_makanan[i]}")

print("\n--- Riwayat Olahraga ---")
if len(riwayat_olahraga) == 0:
    print("(belum ada olahraga dicatat)")
else:
    for i in range(len(riwayat_olahraga)):
        print(f"{i + 1}. {riwayat_olahraga[i]}")

print("\n--- Riwayat Minuman ---")
if len(riwayat_minuman) == 0:
    print("(belum ada minuman dicatat)")
else:
    for i in range(len(riwayat_minuman)):
        print(f"{i + 1}. {riwayat_minuman[i]} ml")

print("\n--- Ringkasan ---")
print("Target Kalori      :", target_kalori)
print("Total Kalori Masuk :", total_kalori_masuk)
print("Kalori Terbakar    :", kalori_terbakar)
print("Kalori Bersih      :", kalori_bersih)

if sisa >= 0:
    print("Status             : Sisa kuota", sisa, "kalori (AMAN)")
else:
    print("Status             : Kelebihan", abs(sisa), "kalori (OVER KALORI)")

print("Target Air Minum   :", target_air_minum, "ml")
print("Total Air Diminum  :", total_minuman_masuk, "ml")

if sisa_air <= 0:
    print("Status Air         : Target air minum tercapai (AMAN)")
else:
    print("Status Air         : Kurang", sisa_air, "ml dari target")
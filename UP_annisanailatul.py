# Aplikasi Pemesanan Tiket Bioskop

print("=== APLIKASI PEMESANAN TIKET BIOSKOP ===")

while True:

    nama = input(" Masukkan Nama Pelanggan (ketik 'selesao' untuk keluar):")
    if nama.lower() == 'selesai':
        print("Terima kasih ! Program selesai. ")
        break

    print("Jenis tiket: Reguler / VIP / Premium")
    jenis = input("Masukkan jenis tiket: ").lower()
    jumlah = int(input("Masukkan jumlah tiket: "))

    if jenis == "reguler":
        harga = 35000
    elif jenis == "VIP":
        harga = 50000
    elif jenis == "premium":
        harga = 75000
    else:
        print("Jenis tiket tidak valid!")
        continue

    subtotal = harga * jumlah

    if jumlah > 3:
        diskon = subtotal * 0.10
        print("Selamat! Anda dapat diskon 10%")
    else:
        diskon = 0

    total_bayar = subtotal - diskon

    # Tampilkan hasil
    print("\n----- STRUK PEMBAYARAN -----")
    print(f"Nama Pelanggan : {nama}")
    print(f"Jenis Tiket    : {jenis.capitalize()}")
    print(f"Jumlah Tiket   : {jumlah}")
    print(f"Harga Satuan   : Rp{harga}")
    print(f"Subtotal       : Rp{subtotal}")
    print(f"Diskon         : Rp{int(diskon)}")
    print(f"TOTAL BAYAR    : Rp{int(total_bayar)}")
    print("-----------------------------")
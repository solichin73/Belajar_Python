transaksi = ["Kabel", 500, "Mouse", 1200, "Kabel", 700, "Keyboard", 2500, "Kabel", 400]

total_bayar = 0

for i, item in enumerate(transaksi):
    if item == "Kabel":
        # ambil harga asli
        harga_asli = transaksi[i + 1]
        if harga_asli > 500:
            #hitung diskon
            diskon = harga_asli * 0.10
        else:
            diskon = 0
        #hitung harga setelah diskon
        harga_setelah_diskon = harga_asli - diskon
        # tambahkan ke total bayar
        total_bayar += harga_setelah_diskon

print("Total yang harus dibayar untuk kabel:", total_bayar)
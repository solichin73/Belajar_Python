daftar_pipa = [3, 8, 2, 10, 5, 12, -1, 0, 7]
pipa_siap_pakai = []
total_panjang = 0

for pipa in daftar_pipa:
    if pipa > 5:
        pipa_siap_pakai.append(pipa)
        total_panjang += pipa

jumlah_pipa_siap_pakai = len(pipa_siap_pakai)
rata_rata = total_panjang / jumlah_pipa_siap_pakai

print("Pipa yang siap pakai:", pipa_siap_pakai)
print("Total panjang pipa yang siap pakai:", total_panjang)
print("Rata-rata panjang pipa yang siap pakai:", rata_rata)
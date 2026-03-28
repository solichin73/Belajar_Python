nilai = [70, 85, 90, 60, 100, 80]

angka_terendah = nilai[0]

for angka in nilai:
    if angka < angka_terendah:
        angka_terendah = angka


print("Nilai terendah adalah:", angka_terendah)
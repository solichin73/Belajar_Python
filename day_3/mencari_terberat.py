beban_material = [150, 300, 450, 100, 600, 250]
paling_berat = 0

for berat in beban_material:
    # 1. Masukkan logika IF di sini untuk mengecek siapa yang paling besar
    if berat > paling_berat:
         paling_berat = berat
    # 2. Update variabel 'paling_berat' jika berat > paling_berat
    pass

print("Material paling berat adalah:", paling_berat)
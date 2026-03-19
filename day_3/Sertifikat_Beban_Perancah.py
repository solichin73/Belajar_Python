beban_material = [150, 300, 450, 100, 600, 250]
batas_beban = 400

total_berat_bahaya = 0
jumlah_material_berbahaya = 0

for berat in beban_material:
    if berat > batas_beban:
        total_berat_bahaya += berat
        jumlah_material_berbahaya += 1


print("Total berat material berbahaya:", total_berat_bahaya)
print("Jumlah material yang melebihi batas:", jumlah_material_berbahaya)
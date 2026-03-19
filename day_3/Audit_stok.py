stok_gudang = ["Laptop", 5, "Monitor", 10, "Laptop", 3, "Mouse", 15, "Laptop", 2]
total_Monitor = 0

for i, item in enumerate(stok_gudang):
    if item == "Monitor":
        total_Monitor += stok_gudang[i + 1]

print("Total stok monitor:", total_Monitor)
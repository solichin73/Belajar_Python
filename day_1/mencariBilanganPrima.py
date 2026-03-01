import math

def statistik_prima(batas_maksimal):
    list_prima = [] # Tempat menyimpan semua angka prima yang ditemukan
    
    print(f"\n--- Menganalisis Bilangan Prima (2 sampai {batas_maksimal}) ---")
    
    for angka in range(2, batas_maksimal + 1):
        is_prima = True
        
        # Menggunakan math.isqrt untuk efisiensi maksimal
        batas_cek = math.isqrt(angka) + 1
        
        for pembagi in range(2, batas_cek):
            if angka % pembagi == 0:
                is_prima = False
                break
        
        if is_prima:
            list_prima.append(angka) # Masukkan angka ke dalam list

    # --- Menampilkan Hasil Statistik ---
    print(f"Daftar Angka: {list_prima}")
    print("-" * 40)
    print(f"📊 Total Bilangan Prima ditemukan : {len(list_prima)} angka")
    print(f"🧮 Jumlah jika semua ditambahkan  : {sum(list_prima)}")
    print(f"🔝 Angka Prima terbesar           : {max(list_prima) if list_prima else 0}")
    print("-" * 40)

# --- Jalankan Program ---
try:
    user_input = int(input("Cek sampai angka berapa? "))
    if user_input < 2:
        print("Bilangan prima dimulai dari angka 2, kawan!")
    else:
        statistik_prima(user_input)
except ValueError:
    print("Aduh! Masukkan angka bulat yang bener ya.")

print("Good Bye!")
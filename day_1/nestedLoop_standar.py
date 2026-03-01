#ini adalah program pencari bilangan prima
#menggunakan for dan else

#contoh kasus mencari bilangan prima dari 2 sampai 99

for i in range(2, 100):
    #cek pembagian 2 sampai akar kuadrat dari i
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        #bagian ini hanya jalan jika Tidak ada j yang membagi i
        print(f"{i} ini bilangan prima.")

print("Good Bye!")
#contoh penggunaan nested loop
""" CATATAN """
# Penggunaan modulo pada kondisional mengasumsikan
#nilai selain no sebagai True (benar) dan nol sebagai False(salah)

i = 97 
while i < 1000:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j +1

    if j > (i / j):
        print(i, "ini bilangan prima.")

    i = i + 1

print("Good Bye!")
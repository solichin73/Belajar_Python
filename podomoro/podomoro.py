import tkinter as tk
import math

# --- KONFIGURASI ---
WARNA_HIJAU = "#9bdeac"
WARNA_MERAH = "#e7305b"
WARNA_KUNING = "#f7f5dd"
WARNA_ABU = "#d3d3d3"
MENIT_KERJA = 25
timer = None
waktu_tersisa = 0  # Untuk menyimpan angka saat di-Stop

# --- FUNGSI SAKTI ---

def mulai_timer():
    global waktu_tersisa
    # Kalau baru mulai atau habis di-reset
    if waktu_tersisa == 0:
        waktu_total = MENIT_KERJA * 60
    else:
        # Kalau lanjut setelah di-Stop
        waktu_total = waktu_tersisa
        
    hitung_mundur(waktu_total, MENIT_KERJA * 60)
    label_judul.config(text="Fokus!", fg=WARNA_HIJAU)

def stop_timer():
    global timer
    if timer:
        # Perintah: "Berhenti menghitung sekarang!"
        window.after_cancel(timer)
        timer = None
        label_judul.config(text="Berhenti", fg=WARNA_MERAH)

def reset_timer():
    global timer, waktu_tersisa
    # Hapus semua jadwal hitungan
    if timer:
        window.after_cancel(timer)
    
    # Kembalikan semua ke awal
    timer = None
    waktu_tersisa = 0
    canvas.itemconfig(teks_waktu, text="25:00")
    canvas.itemconfig(animasi_lingkaran, extent=360)
    label_judul.config(text="Siap?", fg=WARNA_HIJAU)

def hitung_mundur(hitung, total_awal):
    global timer, waktu_tersisa
    waktu_tersisa = hitung # Simpan angkanya setiap detik
    
    menit = math.floor(hitung / 60)
    detik = hitung % 60
    canvas.itemconfig(teks_waktu, text=f"{menit:02d}:{detik:02d}")

    # Update Animasi Lingkaran
    derajat = (hitung / total_awal) * 360
    canvas.itemconfig(animasi_lingkaran, extent=derajat)

    if hitung > 0:
        timer = window.after(1000, hitung_mundur, hitung - 1, total_awal)
    else:
        window.bell()
        label_judul.config(text="Selesai!", fg=WARNA_MERAH)

# --- TAMPILAN (GUI) ---
window = tk.Tk()
window.title("Pomodoro Lengkap")
window.config(padx=50, pady=20, bg=WARNA_KUNING)

label_judul = tk.Label(text="Siap?", fg=WARNA_HIJAU, bg=WARNA_KUNING, font=("Courier", 30, "bold"))
label_judul.grid(column=1, row=0, pady=(0, 20))

canvas = tk.Canvas(width=220, height=220, bg=WARNA_KUNING, highlightthickness=0)
canvas.create_oval(10, 10, 210, 210, outline=WARNA_ABU, width=5)
animasi_lingkaran = canvas.create_arc(10, 10, 210, 210, start=90, extent=360, outline=WARNA_HIJAU, width=10, style="arc")
teks_waktu = canvas.create_text(110, 110, text="25:00", fill="black", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

# Wadah untuk tombol supaya berjejer rapi
bingkai_tombol = tk.Frame(bg=WARNA_KUNING)
bingkai_tombol.grid(column=1, row=2, pady=20)

tk.Button(bingkai_tombol, text="Mulai", command=mulai_timer).pack(side="left", padx=5)
tk.Button(bingkai_tombol, text="Stop", command=stop_timer).pack(side="left", padx=5)
tk.Button(bingkai_tombol, text="Reset", command=reset_timer).pack(side="left", padx=5)

window.mainloop()
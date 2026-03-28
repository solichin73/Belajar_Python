import tkinter as tk
import math
from gui import PomodoroGUI
from ai_logic import berikan_saran

# Variabel Global
timer = None
detik_tersisa = 25 * 60
jumlah_stop = 0

def update_timer():
    global detik_tersisa, timer
    menit = math.floor(detik_tersisa / 60)
    detik = detik_tersisa % 60
    app.canvas.itemconfig(app.teks_waktu, text=f"{menit:02d}:{detik:02d}")
    
    # Update Lingkaran
    app.canvas.itemconfig(app.obat_nyamuk, extent=(detik_tersisa / (25*60)) * 360)
    
    if detik_tersisa > 0:
        detik_tersisa -= 1
        timer = root.after(1000, update_timer)
    else:
        root.bell()
        app.label_judul.config(text="SELESAI!", fg="#f1c40f")

def start():
    global timer
    if not timer:
        update_timer()

def stop():
    global timer, jumlah_stop
    if timer:
        root.after_cancel(timer)
        timer = None
        jumlah_stop += 1
        # Panggil Saran dari AI PyTorch
        pesan, warna = berikan_saran(detik_tersisa, jumlah_stop)
        app.label_saran.config(text=pesan, fg=warna)

def reset():
    global timer, detik_tersisa, jumlah_stop
    if timer:
        root.after_cancel(timer)
    timer = None
    detik_tersisa = 25 * 60
    jumlah_stop = 0
    app.canvas.itemconfig(app.teks_waktu, text="25:00")
    app.canvas.itemconfig(app.obat_nyamuk, extent=360)
    app.label_saran.config(text="Sistem di-reset.", fg="#bdc3c7")

# Menjalankan Aplikasi
root = tk.Tk()
app = PomodoroGUI(root, start, stop, reset)
root.mainloop()
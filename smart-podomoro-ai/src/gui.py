import tkinter as tk

class PomodoroGUI:
    def __init__(self, root, start_callback, stop_callback, reset_callback):
        self.root = root
        self.root.title("Smart Pomodoro AI")
        self.root.config(padx=50, pady=30, bg="#2c3e50")
        
        # Label Judul
        self.label_judul = tk.Label(text="SIAP FOKUS?", fg="#ecf0f1", bg="#2c3e50", font=("Courier", 20, "bold"))
        self.label_judul.pack(pady=10)

        # Canvas Lingkaran
        self.canvas = tk.Canvas(width=220, height=220, bg="#2c3e50", highlightthickness=0)
        self.canvas.create_oval(10, 10, 210, 210, outline="#34495e", width=5)
        self.obat_nyamuk = self.canvas.create_arc(10, 10, 210, 210, start=90, extent=360, outline="#2ecc71", width=10, style="arc")
        self.teks_waktu = self.canvas.create_text(110, 110, text="25:00", fill="white", font=("Courier", 35, "bold"))
        self.canvas.pack()

        # Label Saran AI
        self.label_saran = tk.Label(text="Tekan MULAI untuk berlatih", fg="#bdc3c7", bg="#2c3e50", font=("Arial", 10, "italic"))
        self.label_saran.pack(pady=15)

        # Tombol-tombol
        frame_btn = tk.Frame(bg="#2c3e50")
        frame_btn.pack()
        tk.Button(frame_btn, text="MULAI", command=start_callback, bg="#27ae60", fg="white", width=8).pack(side="left", padx=5)
        tk.Button(frame_btn, text="STOP", command=stop_callback, bg="#c0392b", fg="white", width=8).pack(side="left", padx=5)
        tk.Button(frame_btn, text="RESET", command=reset_callback, width=8).pack(side="left", padx=5)
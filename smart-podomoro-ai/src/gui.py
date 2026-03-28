import customtkinter as ctk

class PomodoroGUI(ctk.CTk):
    def __init__(self, start_cmd, stop_cmd, reset_cmd):
        super().__init__()

        self.title("Smart Pomodoro AI - Premium Edition")
        self.geometry("450x620")
        self.resizable(False, False)

        # Inisialisasi Callback
        self.start_cmd = start_cmd
        self.stop_cmd = stop_cmd
        self.reset_cmd = reset_cmd

        self.setup_ui()

    def setup_ui(self):
        # Header / Judul
        self.label_title = ctk.CTkLabel(self, text="MODE FOKUS", font=("Roboto", 28, "bold"), text_color="#5dade2")
        self.label_title.pack(pady=(30, 10))

        # Canvas untuk Lingkaran Progress (menggunakan standar tkinter di dalam CTK)
        self.canvas = ctk.CTkCanvas(self, width=250, height=250, bg="#242424", highlightthickness=0)
        self.canvas.pack(pady=20)
        
        # Lingkaran Latar Belakang
        self.circle_bg = self.canvas.create_oval(10, 10, 240, 240, outline="#3b3b3b", width=10)
        
        # Busur Progress (Lingkaran yang berkurang)
        self.progress_arc = self.canvas.create_arc(10, 10, 240, 240, start=90, extent=360, 
                                                 outline="#5dade2", width=12, style="arc")
        
        # Teks Waktu Digital
        self.time_text = self.canvas.create_text(125, 125, text="25:00", fill="white", font=("Roboto", 45, "bold"))

        # Area Umpan Balik AI
        self.ai_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=12)
        self.ai_frame.pack(pady=10, padx=40, fill="x")
        self.label_ai = ctk.CTkLabel(self.ai_frame, text="AI: Siap membantumu fokus hari ini", 
                                    font=("Arial", 13, "italic"), text_color="#abb2b9")
        self.label_ai.pack(pady=15)

        # Panel Tombol Kontrol
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=25)

        self.start_btn = ctk.CTkButton(self.btn_frame, text="MULAI", command=self.start_cmd, 
                                      fg_color="#27ae60", hover_color="#219150", width=110, font=("Roboto", 14, "bold"))
        self.start_btn.pack(side="left", padx=10)

        self.stop_btn = ctk.CTkButton(self.btn_frame, text="STOP", command=self.stop_cmd, 
                                     fg_color="#c0392b", hover_color="#a93226", width=110, font=("Roboto", 14, "bold"))
        self.stop_btn.pack(side="left", padx=10)

        self.reset_btn = ctk.CTkButton(self.btn_frame, text="RESET", command=self.reset_cmd, 
                                      fg_color="#7f8c8d", hover_color="#707b7c", width=110, font=("Roboto", 14, "bold"))
        self.reset_btn.pack(side="left", padx=10)

    def update_visuals(self, menit, detik, extent):
        """Memperbarui teks waktu dan lingkaran progress."""
        self.canvas.itemconfig(self.time_text, text=f"{menit:02d}:{detik:02d}")
        self.canvas.itemconfig(self.progress_arc, extent=extent)
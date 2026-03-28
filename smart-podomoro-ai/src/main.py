import customtkinter as ctk
import math
from gui import PomodoroGUI
from ai_logic import AIAgent, hitung_saran_ai

# Pengaturan Tema Global
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Controller:
    def __init__(self):
        # Konfigurasi Waktu (25 Menit)
        self.WAKTU_FOKUS = 25 * 60 
        self.detik_tersisa = self.WAKTU_FOKUS
        self.jumlah_stop = 0
        self.timer_id = None
        self.sedang_jalan = False

        # Inisialisasi Otak AI
        self.ai_model = AIAgent()

        # Inisialisasi Tampilan
        self.app = PomodoroGUI(self.mulai_timer, self.stop_timer, self.reset_timer)

    def update_countdown(self):
        if self.detik_tersisa >= 0:
            menit, detik = divmod(self.detik_tersisa, 60)
            # Hitung derajat lingkaran (360 derajat)
            persentase = (self.detik_tersisa / self.WAKTU_FOKUS) * 360
            
            self.app.update_visuals(menit, detik, persentase)
            
            self.detik_tersisa -= 1
            self.timer_id = self.app.after(1000, self.update_countdown)
        else:
            self.sedang_jalan = False
            self.app.label_title.configure(text="SESI SELESAI", text_color="#f1c40f")

    def mulai_timer(self):
        if not self.sedang_jalan:
            self.sedang_jalan = True
            self.app.label_title.configure(text="SEDANG FOKUS", text_color="#5dade2")
            self.update_countdown()

    def stop_timer(self):
        if self.sedang_jalan:
            self.app.after_cancel(self.timer_id)
            self.sedang_jalan = False
            self.jumlah_stop += 1
            self.app.label_title.configure(text="ISTIRAHAT SEJENAK", text_color="#e67e22")
            
            # Meminta saran dari AI
            pesan, warna = hitung_saran_ai(self.ai_model, self.detik_tersisa, self.jumlah_stop)
            self.app.label_ai.configure(text=pesan, text_color=warna)

    def reset_timer(self):
        if self.timer_id:
            self.app.after_cancel(self.timer_id)
        self.sedang_jalan = False
        self.detik_tersisa = self.WAKTU_FOKUS
        self.jumlah_stop = 0
        self.app.update_visuals(25, 0, 360)
        self.app.label_title.configure(text="MODE FOKUS", text_color="#5dade2")
        self.app.label_ai.configure(text="AI: Siap membantumu fokus hari ini", text_color="#abb2b9")

if __name__ == "__main__":
    program = Controller()
    program.app.mainloop()
import customtkinter as ctk
import math
import pygame
import os
import sys
import threading # Digunakan agar proses berat tidak membuat aplikasi macet

# Fungsi pembantu untuk menentukan path aset (PENTING untuk PyInstaller)
def resource_path(relative_path):
    """ Mendapatkan path absolut ke sumber daya, berfungsi untuk dev dan untuk PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Tambahkan path src agar modul gui dan ai_logic terbaca
sys.path.append(os.path.join(os.path.dirname(__file__)))

try:
    from gui import PomodoroGUI
except ImportError:
    from src.gui import PomodoroGUI

# Pengaturan Tema Global
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Controller:
    def __init__(self):
        # Konfigurasi Waktu (Default: 25 Menit)
        self.WAKTU_FOKUS = 25 * 60 
        self.detik_tersisa = self.WAKTU_FOKUS
        self.jumlah_stop = 0
        self.timer_id = None
        self.sedang_jalan = False
        
        # Inisialisasi Model AI secara bertahap (Lazy Init)
        self.ai_model = None 

        # Inisialisasi Tampilan (Dibuat dulu agar muncul instan)
        self.app = PomodoroGUI(self.mulai_timer, self.stop_timer, self.reset_timer)
        
        # Inisialisasi Suara di latar belakang
        threading.Thread(target=self._init_audio, daemon=True).start()

    def _init_audio(self):
        """Inisialisasi audio tanpa mengganggu startup aplikasi."""
        try:
            pygame.mixer.init()
            pygame.mixer.music.set_volume(0.7)
        except:
            pass

    def mainkan_suara(self, jenis):
        if not pygame.mixer.get_init(): return
        try:
            path_map = {
                "mulai": "assets/start.mp3",
                "stop": "assets/stop.mp3",
                "reset": "assets/reset.mp3",
                "alarm": "assets/alarm.wav"
            }
            path = resource_path(path_map.get(jenis, ""))
            if os.path.exists(path):
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(-1 if jenis == "alarm" else 0)
            else:
                self.app.bell()
        except:
            self.app.bell()

    def update_countdown(self):
        if self.detik_tersisa >= 0:
            menit, detik = divmod(self.detik_tersisa, 60)
            persentase = (self.detik_tersisa / self.WAKTU_FOKUS) * 360
            self.app.update_visuals(menit, detik, persentase)
            self.detik_tersisa -= 1
            self.timer_id = self.app.after(1000, self.update_countdown)
        else:
            self.sedang_jalan = False
            self.app.label_title.configure(text="WAKTU HABIS!", text_color="#f1c40f")
            self.mainkan_suara("alarm")

    def mulai_timer(self):
        if not self.sedang_jalan:
            pygame.mixer.music.stop()
            self.mainkan_suara("mulai")
            self.sedang_jalan = True
            self.app.label_title.configure(text="SEDANG FOKUS", text_color="#5dade2")
            self.update_countdown()

    def stop_timer(self):
        if self.sedang_jalan:
            self.mainkan_suara("stop")
            self.app.after_cancel(self.timer_id)
            self.sedang_jalan = False
            self.jumlah_stop += 1
            self.app.label_title.configure(text="ISTIRAHAT SEJENAK", text_color="#e67e22")
            
            # Jalankan analisis AI di thread terpisah agar UI tidak hang
            threading.Thread(target=self.proses_analisis_ai, daemon=True).start()

    def proses_analisis_ai(self):
        """Memuat AI hanya saat dibutuhkan (Lazy Loading)."""
        try:
            from ai_logic import AIAgent, hitung_saran_ai
            if self.ai_model is None:
                self.ai_model = AIAgent()
            
            pesan, warna = hitung_saran_ai(self.ai_model, self.detik_tersisa, self.jumlah_stop)
            # Update UI harus kembali ke main thread
            self.app.after(0, lambda: self.app.label_ai.configure(text=pesan, text_color=warna))
        except Exception as e:
            print(f"Gagal memuat AI: {e}")

    def reset_timer(self):
        pygame.mixer.music.stop()
        self.mainkan_suara("reset")
        if self.timer_id: self.app.after_cancel(self.timer_id)
        self.sedang_jalan = False
        self.detik_tersisa = self.WAKTU_FOKUS
        self.jumlah_stop = 0
        self.app.update_visuals(25, 0, 360)
        self.app.label_title.configure(text="MODE FOKUS", text_color="#5dade2")
        self.app.label_ai.configure(text="AI: Siap membantumu fokus hari ini", text_color="#abb2b9")

if __name__ == "__main__":
    program = Controller()
    program.app.mainloop()
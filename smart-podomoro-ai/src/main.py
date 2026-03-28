import customtkinter as ctk
import math
import pygame
import os
import sys
from gui import PomodoroGUI
from ai_logic import AIAgent, hitung_saran_ai

# Fungsi pembantu untuk menentukan path aset (PENTING untuk PyInstaller)
def resource_path(relative_path):
    """ Mendapatkan path absolut ke sumber daya, berfungsi untuk dev dan untuk PyInstaller """
    try:
        # PyInstaller membuat folder sementara dan menyimpan path di _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

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
        self.mode_istirahat = False

        # Inisialisasi Otak AI
        self.ai_model = AIAgent()

        # Inisialisasi Tampilan
        self.app = PomodoroGUI(self.mulai_timer, self.stop_timer, self.reset_timer)
        
        # Inisialisasi Mesin Suara dengan Volume 70%
        try:
            pygame.mixer.init()
            pygame.mixer.music.set_volume(0.7)
        except Exception as e:
            print(f"Sistem suara tidak tersedia: {e}")

    def mainkan_suara(self, jenis):
        """Fungsi untuk memutar efek suara singkat"""
        if not pygame.mixer.get_init():
            return

        try:
            path_suara = ""
            if jenis == "mulai":
                path_suara = resource_path("assets/start.mp3")
            elif jenis == "stop":
                path_suara = resource_path("assets/stop.mp3")
            elif jenis == "reset":
                path_suara = resource_path("assets/reset.mp3+ls")
            
            if os.path.exists(path_suara):
                pygame.mixer.music.load(path_suara)
                pygame.mixer.music.play()
            else:
                self.app.bell()
        except Exception:
            self.app.bell()

    def mainkan_alarm(self):
        """Fungsi khusus untuk memutar alarm terus-menerus saat waktu habis"""
        if not pygame.mixer.get_init():
            return

        try:
            path_alarm = resource_path("assets/alarm.wav")
            if os.path.exists(path_alarm):
                pygame.mixer.music.load(path_alarm)
                pygame.mixer.music.play(-1) # Loop selamanya
            else:
                for _ in range(3): self.app.bell()
        except Exception:
            for _ in range(3): self.app.bell()

    def stop_semua_suara(self):
        """Menghentikan semua suara yang sedang diputar"""
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()

    def update_countdown(self):
        """Fungsi utama hitung mundur"""
        if self.detik_tersisa >= 0:
            menit, detik = divmod(self.detik_tersisa, 60)
            # Hitung derajat lingkaran (360 ke 0)
            persentase = (self.detik_tersisa / self.WAKTU_FOKUS) * 360
            self.app.update_visuals(menit, detik, persentase)
            
            self.detik_tersisa -= 1
            self.timer_id = self.app.after(1000, self.update_countdown)
        else:
            self.sedang_jalan = False
            self.mode_istirahat = True
            self.app.label_title.configure(text="WAKTU HABIS!", text_color="#f1c40f")
            self.mainkan_alarm()
            self.app.label_ai.configure(text="AI: Sesi selesai! Ambil napas sejenak.", text_color="#f1c40f")

    def mulai_timer(self):
        """Aksi saat tombol MULAI ditekan"""
        if not self.sedang_jalan:
            self.stop_semua_suara()
            self.mainkan_suara("mulai")
            self.sedang_jalan = True
            self.mode_istirahat = False
            self.app.label_title.configure(text="SEDANG FOKUS", text_color="#5dade2")
            self.update_countdown()

    def stop_timer(self):
        """Aksi saat tombol STOP ditekan"""
        if self.sedang_jalan:
            self.mainkan_suara("stop")
            self.app.after_cancel(self.timer_id)
            self.sedang_jalan = False
            self.jumlah_stop += 1
            self.app.label_title.configure(text="ISTIRAHAT SEJENAK", text_color="#e67e22")
            
            # Meminta analisis AI dari ai_logic.py
            pesan, warna = hitung_saran_ai(self.ai_model, self.detik_tersisa, self.jumlah_stop)
            self.app.label_ai.configure(text=pesan, text_color=warna)

    def reset_timer(self):
        """Aksi saat tombol RESET ditekan"""
        self.stop_semua_suara()
        self.mainkan_suara("reset")
        
        if self.timer_id:
            self.app.after_cancel(self.timer_id)
            
        self.sedang_jalan = False
        self.mode_istirahat = False
        self.detik_tersisa = self.WAKTU_FOKUS
        self.jumlah_stop = 0
        
        # Kembalikan tampilan ke awal
        self.app.update_visuals(25, 0, 360)
        self.app.label_title.configure(text="MODE FOKUS", text_color="#5dade2")
        self.app.label_ai.configure(text="AI: Siap membantumu fokus hari ini", text_color="#abb2b9")

if __name__ == "__main__":
    # Inisialisasi aplikasi
    program = Controller()
    # Menjalankan loop utama antarmuka
    program.app.mainloop()
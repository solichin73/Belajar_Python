import numpy as np

class AIAgent:
    """
    Versi Ringan AIAgent menggunakan NumPy.
    Menggantikan PyTorch untuk mengurangi ukuran aplikasi dari GB ke MB.
    """
    def __init__(self):
        # Inisialisasi bobot (weights) secara manual (simulasi Neural Network sederhana)
        # Baris ini menggantikan nn.Linear(2, 8) dan nn.Linear(8, 1)
        np.random.seed(42)
        self.w1 = np.random.randn(2, 4) * 0.1
        self.w2 = np.random.randn(4, 1) * 0.1
        self.b1 = np.zeros((1, 4))
        self.b2 = np.zeros((1, 1))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, x):
        """Proses forward pass manual."""
        # Layer 1: Linear + ReLU
        z1 = np.dot(x, self.w1) + self.b1
        a1 = np.maximum(0, z1) # ReLU
        
        # Layer 2: Linear + Sigmoid
        z2 = np.dot(a1, self.w2) + self.b2
        return self.sigmoid(z2)

def hitung_saran_ai(model, sisa_detik, jumlah_stop):
    """
    Mengambil keputusan berdasarkan data input menggunakan NumPy.
    """
    # Menyiapkan data input (Normalisasi sederhana)
    # x1: Sisa detik (0-1500), x2: Jumlah stop (0-10)
    input_data = np.array([[sisa_detik / 1500.0, jumlah_stop / 10.0]])
    
    # Prediksi skor
    skor = model.predict(input_data)[0][0]
    
    # Logika penentuan pesan berdasarkan skor prediksi
    if skor < 0.3:
        return "AI: Kamu terlihat lelah. Istirahat sejenak?", "#e74c3c"
    elif jumlah_stop > 3:
        return "AI: Fokusmu terganggu. Coba tarik napas dalam.", "#f1c40f"
    else:
        return "AI: Kerja bagus! Pertahankan momentum ini.", "#2ecc71"
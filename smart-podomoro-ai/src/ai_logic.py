import torch
import torch.nn as nn

class AIAgent(nn.Module):
    """Neural Network untuk memprediksi tingkat fokus pengguna."""
    def __init__(self):
        super(AIAgent, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)

def hitung_saran_ai(model, sisa_detik, jumlah_stop):
    """Mengambil keputusan berdasarkan data input."""
    # Menyiapkan data untuk PyTorch
    input_data = torch.tensor([[float(sisa_detik), float(jumlah_stop)]])
    
    with torch.no_grad():
        skor = model(input_data).item()
    
    # Memberikan umpan balik berdasarkan skor (0.0 - 1.0)
    if skor < 0.4:
        return "AI: Kamu terlihat lelah. Istirahat sejenak?", "#e74c3c"
    elif jumlah_stop > 2:
        return "AI: Fokusmu terganggu. Coba tarik napas dalam.", "#f1c40f"
    else:
        return "AI: Kerja bagus! Pertahankan momentum ini.", "#2ecc71"
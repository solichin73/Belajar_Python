import torch
import torch.nn as nn

# Model Sederhana: Input (Sisa Waktu, Jumlah Stop) -> Output (Tenaga Otak)
class OtakFokus(nn.Module):
    def __init__(self):
        super(OtakFokus, self).__init__()
        self.linear_stack = nn.Sequential(
            nn.Linear(2, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.linear_stack(x)

# Fungsi untuk memberikan saran
def berikan_saran(waktu_jalan, jumlah_stop):
    model = OtakFokus() # Dalam versi asli, ini akan me-load file .pth
    input_data = torch.tensor([[float(waktu_jalan), float(jumlah_stop)]])
    
    with torch.no_grad():
        skor_tenaga = model(input_data).item()
    
    if skor_tenaga < 0.3 or jumlah_stop > 4:
        return "⚠️ AI: Kamu tampak lelah. Coba istirahat 10 menit?", "#e74c3c"
    else:
        return "✅ AI: Fokusmu stabil. Gaspol!", "#2ecc71"
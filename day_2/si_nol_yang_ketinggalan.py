class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        ans = []
        
        # 1. Loop pertama: Ambil yang BUKAN NOL
        for angka in nums:
            if angka != 0:
                # Masukkan ke ans menggunakan append
                ans.append(angka)
                pass
        
        # 2. Hitung berapa nol yang harus ditambahkan
        # Caranya: Panjang nums asli dikurangi panjang ans sekarang
        jumlah_nol = len(nums) - len(ans)
        
        # 3. Tambahkan angka 0 sebanyak jumlah_nol tersebut
        # Petunjuk: Gunakan perulangan 'for i in range(jumlah_nol):'
        for i in range(jumlah_nol):
            ans.append(0)
        
        return ans
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        
        # 1. Loop pertama untuk angka_i
        for i in range(n):
            # 2. Loop kedua untuk angka_j (mulai dari i + 1 agar tidak bentrok)
            for j in range(i + 1, n):
                # 3. MASUKKAN LOGIKA IF DI SINI:
                # Apakah nums[i] + nums[j] sama dengan target?
                if nums[i] + nums[j] == target:
                # 4. KEMBALIKAN [i, j] JIKA BENAR
                    return [i, j]
        return []  # Kembalikan list kosong jika tidak ditemukan pasangan yang sesuai
# meet5.py
# contoh operasi aritmatika dasar dan prioritas operasi dalam python
# Operasi Aritmatika (x : -)
a = 17
b = 3

# 1. Penjumlahan
hasil = a + b
print(a, "+", b, "=", hasil)

# 2. Pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

# 3. Perkalian
hasil = a * b
print(a, "*", b, "=", hasil)

# 4. Pembagian
hasil = a / b
print(a, "/", b, "=", hasil)

# 5. Perpangkatan
hasil = a ** b
print(a, "**", b, "=", hasil)

# 6. Modulus (Sisa Bagi)
# Perbaikan: Baris 22 di gambar memiliki 'hasil = a * b'. Seharusnya menggunakan operator % untuk modulus.
hasil = a % b
print(a, "%", b, "=", hasil)

# 7. Floor Division // (Pembulatan ke bawah)
hasil = a // b
print(a, "//", b, "=", hasil)

# ---

# Operasi Prioritas (Urutan Operasi - PEMDAS/BODMAS)
# 1. ()
# 2. Pangkat (**) / Akar (gunakan **)
# 3. Kali (*), Bagi (/), Modulus (%), Floor Division (//) -> dari kiri ke kanan
# 4. Tambah (+), Kurang (-) -> dari kiri ke kanan

print("\n--- Contoh Prioritas Operasi ---")
x = 10
y = 2
z = 3

# Contoh 1: Prioritas perkalian lebih tinggi dari penjumlahan
# Hasil: (y * z) + x -> (2 * 3) + 10 -> 6 + 10 = 16
contoh1 = x + y * z
print("Contoh 1: 10 + 2 * 3 =", contoh1)

# Contoh 2: Menggunakan tanda kurung untuk mengubah prioritas
# Hasil: (x + y) * z -> (10 + 2) * 3 -> 12 * 3 = 36
contoh2 = (x + y) * z
print("Contoh 2: (10 + 2) * 3 =", contoh2)

# Contoh 3: Kombinasi
# Hasil: (x / y) ** z + (x % z)
# Langkah 1: Tanda kurung (10 / 2) -> 5.0, (10 % 3) -> 1
# Langkah 2: Pangkat (5.0 ** 3) -> 125.0
# Langkah 3: Penjumlahan 125.0 + 1 = 126.0
contoh3 = (x / y) ** z + (x % z)
print("Contoh 3: (10 / 2) ** 3 + (10 % 3) =", contoh3)
print("\n--- Akhir dari meet5.py ---")

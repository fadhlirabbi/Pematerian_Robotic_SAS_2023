def funcTambah(a, b):
    return a + b

def funcKurang(a, b):
    return a - b

def funcBagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Pembagian oleh nol tidak diperbolehkan."

def funcKali(a, b):
    return a * b

# Meminta pengguna untuk memilih operasi
print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Bagi")
print("4. Kali")

choice = int(input("Masukkan nomor operasi yang dipilih (1-4): "))

# Meminta input dari pengguna
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Memanggil fungsi sesuai dengan pilihan pengguna
if choice == 1:
    result = funcTambah(a, b)
elif choice == 2:
    result = funcKurang(a, b)
elif choice == 3:
    result = funcBagi(a, b)
elif choice == 4:
    result = funcKali(a, b)
else:
    result = "Pilihan tidak valid."

# Menampilkan hasil
print("Hasil operasi:", result)

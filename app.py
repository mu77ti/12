# normality_calculator.py

def hitung_mol(berat, massa_molar):
    return berat / massa_molar

def hitung_normalitas(mol, volume_liter):
    return mol / volume_liter

def normalitas_dari_berat(berat, massa_molar, volume_ml, valensi=1):
    volume_liter = volume_ml / 1000
    mol = hitung_mol(berat, massa_molar)
    normalitas = hitung_normalitas(mol, volume_liter) * valensi
    return normalitas

def main():
    print("=== Kalkulator Normalitas ===")
    try:
        berat = float(input("Masukkan berat zat (gram): "))
        massa_molar = float(input("Masukkan massa molar (g/mol): "))
        volume_ml = float(input("Masukkan volume larutan (mL): "))
        valensi = int(input("Masukkan valensi zat (contoh: HCl = 1, H2SO4 = 2): "))

        hasil = normalitas_dari_berat(berat, massa_molar, volume_ml, valensi)
        print(f"\n>> Normalitas larutan: {hasil:.4f} N")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

if __name__ == "__main__":
    main()


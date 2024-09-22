# Bangun ruang Tabung
phi = 3.14
jari_jari = int(input("Masukkan jari-jari = "))
tinggi = int(input("Masukkan tinggi = "))

def volume_tabung(phi, jari_jari, tinggi) :
    return phi * (jari_jari ** 2) * tinggi

def luas_permukaan(phi, jari_jari, tinggi) :
    return 2 * phi * jari_jari * (jari_jari + tinggi)

print("Volume tabung : ", volume_tabung(phi, jari_jari, tinggi))
print("Luas permukaan tabung : ", luas_permukaan(phi, jari_jari, tinggi))
import random

nama = str('Andikari')
nama1 = str('Razka')
umur = int(15)
kelas = float(10.2)
kalimat = str('Murid biasa aja')

nama_andi = input("MASUKIN NAMAMU WOY : ")
if nama_andi == nama:
    kalimat = str('Murid keren')
elif nama_andi == nama1:
    kalimat = str('Murid gila')

print(f'nama ku {nama_andi} dan umurku adalah {umur} dan berada di kelas {kelas} aku adalah {kalimat}')

start = input("Ada seorang komputer jahat menghampirii mu. Lawan dengan permainan SUIT!!!! (Lawan/Kabur)")
if start == "Lawan":
    
elif start == "Kabur":

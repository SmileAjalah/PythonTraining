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

menang = int(0)
kalah = int(0)
seri = int(0)

start = input("Ada seorang komputer jahat menghampirii mu. Lawan dengan permainan SUIT!!!! (Lawan/Kabur) : ")
if start == "Lawan":
    act = input("Serang dengan... (Batu/Gunting/Kertas) : ")
    poss = ["Batu", "Gunting", "Kertas"]
    kom = random.choice(poss)
    print(f'Kamu menyerang dengan {act} lalu dia menyerang dengan {kom}')
    if act == kom:
        print("Kalian seri!")
    elif act == ("Batu"):
        if kom == ("Gunting"):
            print("Guntingnya hancur dengan pukulan batumu! kamu menang!!")
        else:
            print("Pukulan batu mu ditahan olehnya dan dikembalikan pada mu, kamu kalah")
    elif act == ("Gunting"):
        if kom == ("Kertas"):
            print("Kamu membelah tangan kertasnya dengan pedang guntingmu! kamu menang!!")
        else:
            print("Guntingmu hancur dengan pukulan batunya, kamu kalah")
    elif act == ("Kertas"):
        if kom == ("Batu"):
            print("Pukulan batunya ditahan olehmu dan dikembalikan padanya! kamu menang!!")
        else:
            print("Dia membelah tangan kertasmu dengan pedang guntingnya, kamu kalah")
elif start == "Kabur":
    print("Ihhh Lemah")
    exit()
else:
    while(True):
        start = input("Pilihannya hanya ada dua! :")
        if start == "Lawan":
            print("Menang: ", menang)
            print("Kalah : ", kalah)
            print("Seri :", seri)
            act = input("Serang dengan... (Batu/Gunting/Kertas) : ")
            poss = ["Batu", "Gunting", "Kertas"]
            kom = random.choice(poss)
            print(f'Kamu menyerang dengan {act} lalu dia menyerang dengan {kom}')
            if act == kom:
                print("Kalian seri!")
                seri += 1
            elif act == ("Batu"):
                if kom == ("Gunting"):
                    print("Guntingnya hancur dengan pukulan batumu! kamu menang!!")
                    menang += 1
                else:
                    print("Pukulan batu mu ditahan olehnya dan dikembalikan pada mu, kamu kalah")
                    kalah += 1
            elif act == ("Gunting"):
                if kom == ("Kertas"):
                    print("Kamu membelah tangan kertasnya dengan pedang guntingmu! kamu menang!!")
                    menang += 1
                else:
                    print("Guntingmu hancur dengan pukulan batunya, kamu kalah")
                    kalah += 1
            elif act == ("Kertas"):
                if kom == ("Batu"):
                    print("Pukulan batunya ditahan olehmu dan dikembalikan padanya! kamu menang!!")
                    menang += 1
                else:
                    print("Dia membelah tangan kertasmu dengan pedang guntingnya, kamu kalah")
                    kalah += 1
        elif start == "Kabur":
            print("Ihhh Lemah")
            exit()
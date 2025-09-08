import random
import time

name = str("L")
gender = str("")
money = int(100)

print("Selamat datang di Casino")
print("Berikan identitas mu")
name = input("Pertama, Siapa namamu? : ")
gender = input("Kedua, kamu laki laki atau perempuan(L/P)? : ")
while(True):
    if gender == "L":
        gender = "Laki Laki"
        break
    elif gender == "P":
        gender = "Perempuan"
        break
    else:
        gender = input("Tolong ulangi, kamu laki laki atau perempuan(L/P)? : ")

print(f'Kamu telah masuk ke Casino sebagai {name}')
print("")

while(True):
    print("Sekarang apa yang sedang kamu lakukan?")
    print("-ID CARD(ID)")
    print("-Game Start(GS)")
    act = input("ACT(ID/GS) : ")
    if act == "ID":
        print("")
        print("ID CARD/IDENTITAS")
        print("Name : ", name)
        print("Gender : ", gender)
        print("Money : ", money)
        print("")
        input("Press Enter Jika Sudah")
        print("")
        print("")
    if act == "GS":
        while(True):
            print("")
            print("Your Bet?")
            print("-5")
            print("-10")
            print("-25")
            print("-50")
            print("-100")
            print("Your Money : ", money)
            print("")
            bet = input("Bet(5/10/25/50/100) : ")
            if bet == "5":
                while (True):
                    money -= 5
                    print("")
                    print("GAMEMODE")
                    print("-Slot(S)")
                    print("-High and Low(H)")
                    mode = input("Mode(S/H) : ")
                    if mode == "S":
                        slposs = ["X", "O", "7"]
                        s = random.choice(slposs)
                        sa = random.choice(slposs)
                        sb = random.choice(slposs)
                        print("Rolling")
                        time.sleep(2.5)
                        print(f"===={s}|Z|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|{sb}====")
                        if s == sa:
                            if s == sb:
                                if s == "7":
                                    print("====JACKPOT====")
                                    money += 20
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 15 money!")
                                else:
                                    print("====WIN====")
                                    money += 15
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 10 money!")
                            else:
                                print("====LOSE====")
                                time.sleep(1.0)
                                print("")
                                print("Kamu kehilangan 5 money...")
                        else:
                            print("====LOSE====")
                            time.sleep(1.0)
                            print("")
                            print("Kamu kehilangan 5 money...")
                        print("MONEY : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
                    if mode == "H":
                        kpos = [2,3,4,5,6,7,8,9,10,11,12,13,14]
                        ku = random.choice(kpos)
                        kk = random.choice(kpos)
                        while ku == kk:
                            kk = random.choice(kpos)
                        while(True):
                            print("")
                            print("Kartu mu adalah ", ku)
                            hact = input("apa lawan mu lebih tinggi(H) atau lebih rendah(L)? : ")
                            if hact == "H":
                                if ku <= kk:
                                    money += 8
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 3 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 5 money")
                                break
                            if hact == "L":
                                if ku >= kk:
                                    money += 8
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 3 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 5 money")
                                break
                        print("Money : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
            if bet == "10":
                while (True):
                    money -= 10
                    print("")
                    print("GAMEMODE")
                    print("-Slot(S)")
                    print("-High and Low(H)")
                    mode = input("Mode(S/H) : ")
                    if mode == "S":
                        slposs = ["X", "O", "7"]
                        s = random.choice(slposs)
                        sa = random.choice(slposs)
                        sb = random.choice(slposs)
                        print("Rolling")
                        time.sleep(2.5)
                        print(f"===={s}|Z|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|{sb}====")
                        if s == sa:
                            if s == sb:
                                if s == "7":
                                    print("====JACKPOT====")
                                    money += 40
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 30 money!")
                                else:
                                    print("====WIN====")
                                    money += 30
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 20 money!")
                            else:
                                print("====LOSE====")
                                time.sleep(1.0)
                                print("")
                                print("Kamu kehilangan 10 money...")
                        else:
                            print("====LOSE====")
                            time.sleep(1.0)
                            print("")
                            print("Kamu kehilangan 10 money...")
                        print("MONEY : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
                    if mode == "H":
                        kpos = [2,3,4,5,6,7,8,9,10,11,12,13,14]
                        ku = random.choice(kpos)
                        kk = random.choice(kpos)
                        while ku == kk:
                            kk = random.choice(kpos)
                        while(True):
                            print("")
                            print("Kartu mu adalah ", ku)
                            hact = input("apa lawan mu lebih tinggi(H) atau lebih rendah(L)? : ")
                            if hact == "H":
                                if ku <= kk:
                                    money += 15
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 5 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 10 money")
                                break
                            if hact == "L":
                                if ku >= kk:
                                    money += 15
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 5 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 10 money")
                                break
                        print("Money : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
            if bet == "25":
                while (True):
                    money -= 25
                    print("")
                    print("GAMEMODE")
                    print("-Slot(S)")
                    print("-High and Low(H)")
                    mode = input("Mode(S/H) : ")
                    if mode == "S":
                        slposs = ["X", "O", "7"]
                        s = random.choice(slposs)
                        sa = random.choice(slposs)
                        sb = random.choice(slposs)
                        print("Rolling")
                        time.sleep(2.5)
                        print(f"===={s}|Z|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|{sb}====")
                        if s == sa:
                            if s == sb:
                                if s == "7":
                                    print("====JACKPOT====")
                                    money += 100
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 75 money!")
                                else:
                                    print("====WIN====")
                                    money += 75
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 50 money!")
                            else:
                                print("====LOSE====")
                                time.sleep(1.0)
                                print("")
                                print("Kamu kehilangan 25 money...")
                        else:
                            print("====LOSE====")
                            time.sleep(1.0)
                            print("")
                            print("Kamu kehilangan 25 money...")
                        print("MONEY : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
                    if mode == "H":
                        kpos = [2,3,4,5,6,7,8,9,10,11,12,13,14]
                        ku = random.choice(kpos)
                        kk = random.choice(kpos)
                        while ku == kk:
                            kk = random.choice(kpos)
                        while(True):
                            print("")
                            print("Kartu mu adalah ", ku)
                            hact = input("apa lawan mu lebih tinggi(H) atau lebih rendah(L)? : ")
                            if hact == "H":
                                if ku <= kk:
                                    money += 38
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 13 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 25 money")
                                break
                            if hact == "L":
                                if ku >= kk:
                                    money += 38
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 13 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 25 money")
                                break
                        print("Money : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
            if bet == "50":
                while (True):
                    money -= 50
                    print("")
                    print("GAMEMODE")
                    print("-Slot(S)")
                    print("-High and Low(H)")
                    mode = input("Mode(S/H) : ")
                    if mode == "S":
                        slposs = ["X", "O", "7"]
                        s = random.choice(slposs)
                        sa = random.choice(slposs)
                        sb = random.choice(slposs)
                        print("Rolling")
                        time.sleep(2.5)
                        print(f"===={s}|Z|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|{sb}====")
                        if s == sa:
                            if s == sb:
                                if s == "7":
                                    print("====JACKPOT====")
                                    money += 200
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 150 money!")
                                else:
                                    print("====WIN====")
                                    money += 150
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 100 money!")
                            else:
                                print("====LOSE====")
                                time.sleep(1.0)
                                print("")
                                print("Kamu kehilangan 50 money...")
                        else:
                            print("====LOSE====")
                            time.sleep(1.0)
                            print("")
                            print("Kamu kehilangan 50 money...")
                        print("MONEY : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
                    if mode == "H":
                        kpos = [2,3,4,5,6,7,8,9,10,11,12,13,14]
                        ku = random.choice(kpos)
                        kk = random.choice(kpos)
                        while ku == kk:
                            kk = random.choice(kpos)
                        while(True):
                            print("")
                            print("Kartu mu adalah ", ku)
                            hact = input("apa lawan mu lebih tinggi(H) atau lebih rendah(L)? : ")
                            if hact == "H":
                                if ku <= kk:
                                    money += 75
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 25 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 50 money")
                                break
                            if hact == "L":
                                if ku >= kk:
                                    money += 75
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 25 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 50 money")
                                break
                        print("Money : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
            if bet == "100":
                while (True):
                    money -= 100
                    print("")
                    print("GAMEMODE")
                    print("-Slot(S)")
                    print("-High and Low(H)")
                    mode = input("Mode(S/H) : ")
                    if mode == "S":
                        slposs = ["X", "O", "7"]
                        s = random.choice(slposs)
                        sa = random.choice(slposs)
                        sb = random.choice(slposs)
                        print("Rolling")
                        time.sleep(2.5)
                        print(f"===={s}|Z|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|Z====")
                        time.sleep(2.5)
                        print(f"===={s}|{sa}|{sb}====")
                        if s == sa:
                            if s == sb:
                                if s == "7":
                                    print("====JACKPOT====")
                                    money += 400
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 300 money!")
                                else:
                                    print("====WIN====")
                                    money += 300
                                    time.sleep(1.0)
                                    print("")
                                    print("Kamu mendapatkan 200 money!")
                            else:
                                print("====LOSE====")
                                time.sleep(1.0)
                                print("")
                                print("Kamu kehilangan 100 money...")
                        else:
                            print("====LOSE====")
                            time.sleep(1.0)
                            print("")
                            print("Kamu kehilangan 100 money...")
                        print("MONEY : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
                    if mode == "H":
                        kpos = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                        ku = random.choice(kpos)
                        kk = random.choice(kpos)
                        while ku == kk:
                            kk = random.choice(kpos)
                        while (True):
                            print("")
                            print("Kartu mu adalah ", ku)
                            hact = input("apa lawan mu lebih tinggi(H) atau lebih rendah(L)? : ")
                            if hact == "H":
                                if ku <= kk:
                                    money += 150
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 50 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 100 money")
                                break
                            if hact == "L":
                                if ku >= kk:
                                    money += 150
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu menang! kamu mendapatkan 50 money")
                                else:
                                    print("Kartu lawan adalah...")
                                    time.sleep(1)
                                    print(f"===={kk}====")
                                    print("Kamu kalah, kamu kehilangan 100 money")
                                break
                        print("Money : ", money)
                        print("")
                        repeat = input("Ulangi(Y/N) : ")
                        if repeat == "Y":
                            print("")
                        else:
                            break
            break
            

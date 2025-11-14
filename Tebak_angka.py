import os,time,random
print("Selamat Datang di Tebak Angka!")
print("--Rules--")
print("lebih kecil, jika angka lebih besar dari target")
print("lebih besar, jika angka lebih kecil dari target")
print("1. Mulai")
print("2. Pulang")
limit_easy = 5
limit_normal = 7
limit_hard = 10
limit_EX= 100
start = int(input("= "))
while True:
    if start == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Tolong Pilih Tingkat Kesulitan Anda")
        print("1. easy")
        print("2. normal")
        print("3. hard")
        pilihan = int(input("= "))
        if pilihan == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            guess = int(input("tebaklah angkanya"))
            print("Percobaan tersisa",limit_easy)
            limit_easy=limit_easy-1
            easy = random.randint(1,10)
            while True:
                if(limit_easy < 0):
                    print("Maaf! Kesempatan Habis!")
                    time.sleep(3)
                    break
                if (guess == easy):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("benar")
                    break
                elif (guess > easy):
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    guess = int(input("lebih kecil"))
                    print("Percobaan tersisa",limit_easy)
                    limit_easy=limit_easy-1
                    continue
                elif (guess < easy):
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    guess = int(input("lebih besar"))
                    print("Percobaan tersisa",limit_easy)
                    limit_easy=limit_easy-1
                    continue
                
                continue
        elif pilihan == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            guess = int(input("tebaklah angkanya"))
            print("Percobaan tersisa",limit_normal)
            limit_normal=limit_normal-1
            normal = random.randint(1,10)
            while True:
                if(limit_normal < 0):
                    print("Maaf! Kesempatan Habis!")
                    time.sleep(3)
                    break
                if (guess == normal):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(1)
                    print("benar")
                    break
                elif (guess > normal):
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    guess = int(input("lebih kecil"))
                    print("Percobaan tersisa",normal)
                    limit_normal=limit_normal-1
                    continue
                elif (guess < normal):
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    guess = int(input("lebih besar"))
                    print("Percobaan tersisa",limit_normal)
                    limit_normal=limit_normal-1
                    continue 
            continue
        elif pilihan == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            guess = int(input("tebaklah angkanya"))
            hard = random.randint(1,1000)
            while True:
                if(limit_hard < 0):
                    print("Maaf! Kesempatan Habis!")
                    time.sleep(3)
                    break
                if (guess == hard):
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("benar")
                    break
                elif guess > hard:
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    guess = int(input("lebih kecil"))
                    print("Percobaan tersisa",limit_hard)
                    limit_hard=limit_hard-1
                    continue
                elif guess < hard:
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    guess = int(input("lebih besar"))
                    print("Percobaan tersisa",limit_hard)
                    limit_hard=limit_hard-1
                    continue
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            EX = random.randint(1,100000)
            print("Selamat Datang di mode EX! HAHAHAHAHA")
            guess = int(input("tebaklah angkanya"))
            while True:
                if (guess == EX):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Tak Mungkin!")
                    break
                elif guess > EX:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    guess = int(input("lebih kecil!"))
                    continue
                elif guess < EX:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    guess = int(input("lebih besar!"))
                    continue
            break
    elif start == 2:
        print("Selamat Tinggal")
        break
    else:
        print("Kembalilah Biadap!")
        break
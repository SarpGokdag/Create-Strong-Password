import random
import argparse

def karakterler():
    harfler = "a b c ç d e f g ğ h ı i j k l m n o ö p r s ş t u ü v w x y z q".split()
    semboller = "! @ # $ % ^ & * ( ) _ - + = ? : ; ß Ý Û ∱ ∑ √ ⫚ ⟑ 𝛞 𝛟 𝛠 𝛡 𝛙 𝛏 𝛎 𝛑 𝛌 𝛃 𝛀 𝚹 𝚵".split()
    chars = []
    chars.append(random.choice(harfler))
    chars.append(random.choice(harfler).upper())
    chars.append(str(random.randint(0,9)))
    chars.append(random.choice(semboller))

    return chars

def yeni_sifre(length=32):
    harf = karakterler()
    while len(harf) < length:
        harf.append(random.choice(karakterler()))
    random.shuffle(harf)
    return "".join(harf)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--sayı", dest='sayı', type=int, default=1, help='<default 1>')
    parser.add_argument("-l", "--length", type=int, default=64, help='<default 8>')
    args = parser.parse_args()

    for n in range(args.sayı):
        print(yeni_sifre(args.length))
'''
   _____    _____   _____   ______   _   _    _____   ______                __  __   ____    _____     ____     _____   _____            
  / ____|  / ____| |_   _| |  ____| | \ | |  / ____| |  ____|       /\     |  \/  | |  _ \  |  __ \   / __ \   / ____| |_   _|     /\    
 | (___   | |        | |   | |__    |  \| | | |      | |__         /  \    | \  / | | |_) | | |__) | | |  | | | (___     | |      /  \   
  \___ \  | |        | |   |  __|   | . ` | | |      |  __|       / /\ \   | |\/| | |  _ <  |  _  /  | |  | |  \___ \    | |     / /\ \  
  ____) | | |____   _| |_  | |____  | |\  | | |____  | |____     / ____ \  | |  | | | |_) | | | \ \  | |__| |  ____) |  _| |_   / ____ \ 
 |_____/   \_____| |_____| |______| |_| \_|  \_____| |______|   /_/    \_\ |_|  |_| |____/  |_|  \_\  \____/  |_____/  |_____| /_/    \_\ 
 '''                                                                                                                                                                                                                                                                                                                                                                                                                 

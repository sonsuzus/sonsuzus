import random
import platform
from os import system

def main():
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")

    print('-'*75)
    print("Merhaba! Senin tuttuğun sayıyı bulmaya çalışacağım.\nŞimdi içinden 1 ile 100 arasında bir sayı tut ve ben de tahmin edeyim.")
    print("Tahmin Ettiğinde Enter'a bas")
    print('-' * 75)
    input()
    print()
    minimum = 1
    maximum = 101
    hp = 7
    guess = 0
    inp = None
    while hp > 0:
        try:
            guess = random.randrange(minimum, maximum)
        except:
            print("1 ile 100 arasında tuttuğuna emin misin?")
            exit(0)
        inp = input("Tahminim: {}\nCanım: {}\nEğer çok yüksekse 'Y' alçaksa 'A' doğruysa 'T' giriniz: ".format(guess, hp))
        print()
        inp = inp.lower()
        if inp[0] == 'a':
            minimum = guess + 1
            hp -= 1
        elif inp[0] == 'y':
            maximum = guess
            hp -= 1
        elif inp[0] == 't':
            print("Nasıl buldum ama :)")
            print("Oynadığın için teşekkürler!")
            exit(0)
        else: print("Ne girdiğini anlayamadım?")
    print("Bu sefer bulamadım :(")
    print("Bir dahaki sefere bulacağım ama!")

if __name__ == "__main__":
    main()
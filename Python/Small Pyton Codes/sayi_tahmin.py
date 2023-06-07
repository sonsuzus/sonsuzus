import random

def main():
    number = random.randint(1, 100)
    guess = 0
    hp = 7
    print("Merhaba! 1'den 100'e kadar bir sayı tuttum. Bakalım en çok",hp,"denemede bulabilecek misin?")
    print()
    while guess != number and hp > 0:
        print("Canınız:", hp)
        guess = int(input("Tahmininizi Giriniz: "))
        print()
        if guess == number:
            print("Bravo Doğru Tahmin! Tuttuğum Sayıyı Buldun!")
            exit(0)
        if guess > number: print("Çok Yüksek Bir Sayı Girdiniz!")
        else: print("Çok Düşük Bir Sayı Girdiniz!")
        hp -= 1
        print()
    print("Malesef bulamadın :(")
    print("Tuttuğum Sayı", number,"idi")

if __name__ == "__main__":
    main()
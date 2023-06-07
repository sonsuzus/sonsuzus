from datetime import datetime

birthday = input("Doğum gününüzü GG/AA/YYYY şeklinde yazınız: ")
try:
    birthday = datetime.strptime(birthday, "%d/%m/%Y")
except ValueError:
    print("Lütfen düzgün değerler giriniz...")
else:
    now = datetime.now()
    if birthday > now:
        print("Gelecekte doğmuş olamazsınız!")
        exit(0)
    delta = now - birthday
    print(delta.days, "günlüksünüz.")
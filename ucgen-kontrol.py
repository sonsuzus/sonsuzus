#üç kenarı girildikten sonra üçgen olup olmadığı eğer üçgense nasıl bir üçgen olduğunu bulan program
a = int(input("Birinci kenarı giriniz: "))
b = int(input("İkinci kenarı giriniz: "))
c = int(input("Üçüncü kenarı giriniz: "))
if a+b>c and a+c>b and b+c>a:
    print("Bu bir üçgendir.")
    #burası çalışıyor ilginç
    if a==b==c:
        print("Bu bir eşkenar üçgendir")
    elif a==b or a==c or b==c:
        print("Bu bir ikizkenar üçgendir")
    elif a**2+b**2==c**2 or a*a+c*c==b*b or b*b+c*c==a*a:
        print("Bu bir dik üçgendir")
    else:
        print("Bu bir çeşitkenar üçgendir")

else:
    print("Bu bir üçgen değildir.")





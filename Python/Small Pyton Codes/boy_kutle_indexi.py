def main():
    mass = float(input("Kütleniz: "))
    height = float(input("Boyunuz (m): "))

    value = mass / (height ** 2)
    value = round(value, 3)

    print(f"Boy kütle indeksiniz: {value}")
    if value <= 18.4:
        print("Zayıfsınız")
    elif value > 18.4 and value <= 24.9:
        print("Normal Kilolusunuz")
    elif value > 24.9 and value <= 29.9:
        print("Fazla Kilolusunuz")
    elif value > 29.9 and value <= 34.9:
        print("Obezsiniz")


if __name__ == '__main__':
    main()
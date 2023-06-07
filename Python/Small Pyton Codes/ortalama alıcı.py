def main():
    my_list = list()
    while True:
        inp = float(input('> '))
        if inp < 0:
            break
        my_list.append(inp)
    print(sum(my_list) / len(my_list))

if __name__ == '__main__':
    main()
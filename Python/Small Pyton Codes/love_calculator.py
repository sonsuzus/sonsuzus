import random
import math

def main():
    name1 = input('Enter the first name: ')
    name2 = input('Enter the second name: ')

    name_cat = name1.upper().replace(' ', '') + name2.upper().replace(' ', '')
    n_sum = sum(ord(c) for c in name_cat)

    random.seed(n_sum)
    percent = random.randint(0, 10000)
    percent = int(math.sqrt(percent))

    print(f'{name1} and {name2} match {percent}%')

if __name__ == '__main__':
    main()

def pascalTriangle(n: int):
    triangle = list()
    prev = [1]
    for i in range(2, n + 1):
        triangle.append(prev)
        my_list = list()
        for _ in range(i):
            my_list.append(0)
        for j in range(i):
            if j == 0:
                my_list[j] = prev[0]
            elif j == i - 1:
                my_list[j] = prev[-1]
            else:
                my_list[j] = prev[j - 1] + prev[j]
        prev = my_list.copy()
    triangle.append(prev)
    return triangle

def main():

    n = int(input('Row: '))
    triangle = pascalTriangle(n)
    last_row_length = 0
    for x in triangle[-1]:
        last_row_length += len(str(x)) + 1
    last_row_length -= 1

    for line in triangle:
        line_str = ''
        for elem in line:
            line_str += str(elem) + ' '
        line_str = line_str[:-1].center(last_row_length)
        print(line_str)

if __name__ == '__main__':
    main()
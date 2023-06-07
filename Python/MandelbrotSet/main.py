import os
import cmath
import math

full_block = '█'
def is_close(a, b, diff):
    return math.fabs(a - b) < diff

def func(z, c):
    return z*z + c

def run_n_times(f, n, x, c):
    last = x
    for i in range(n):
        last = f(last, c)
    return last


def main():
    terminal_size = os.get_terminal_size()
    os.system('clear')
    coords = {
        'top': float(terminal_size.lines) / 20.0,
        'left': -float(terminal_size.columns) / 20.0,
        'bottom': -float(terminal_size.lines) / 20.0,
        'right': float(terminal_size.columns) / 20.0,
    }
    # print(coords)
    # print(run_n_times(func, 100, 0, .5j))

    y = coords['top']
    while (not is_close(y, coords['bottom'], .01)) and (y > coords['bottom']):
        x = coords['left']
        while (not is_close(x, coords['right'], .01)) and (x < coords['right']):
            result = run_n_times(func, 100, 0, x + y*1j)
            if cmath.isinf(result) or cmath.isnan(result):
                print('\033[30m' + full_block, end='')
            else:
                print('\033[34m' + full_block, end='')
            x += .1
        y -= .1
    print('\033[0m', end='')

if __name__ == '__main__':
    main()
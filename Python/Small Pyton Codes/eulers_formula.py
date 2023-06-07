import math

def e_xi(x):
    real_part = math.cos(x)
    imaginary_part = math.sin(x)
    if math.isclose(real_part, 0, abs_tol=1e-8):
        real_part = 0
    if math.isclose(imaginary_part, 0, abs_tol=1e-8):
        imaginary_part = 0

    return real_part + imaginary_part * 1j

def main():
    a = input("Please enter a number: ")
    a = a.replace("tau", str(math.tau)).replace("pi", str(math.pi)).replace("e", str(math.e))
    a = float(a)

    print("e^({}*i) = ".format(a), end='')
    result = e_xi(a)

    if result.real != 0:
        print("{} ".format(result.real), end='')
    if result.imag != 0:
        if result.imag < 0:
            print("- {}i".format(result.imag * -1))
        else:
            print("+ {}i".format(result.imag))

if __name__ == "__main__": main()

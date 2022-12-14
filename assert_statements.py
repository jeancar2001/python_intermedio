def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes ingresar un número superior a 1"
    assert 4 == 9, '4 no es igual a 9'
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()
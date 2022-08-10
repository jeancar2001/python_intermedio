lista = [1,2,3,4,5,6,7,8,9]

def run(number):
    a = []
    for i in number:
        if i >5:
            a.append(i)
    return(a)


palindromo = lambda number: run(number)

print(palindromo(lista))
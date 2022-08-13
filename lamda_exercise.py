lista = [1,2,3,4,5,6,8,9]

def run(number):
    try:    
      a = []
      for i in lista:
          if i >5:
            a.append(i)
          if i==7:
            print('''excepcion encontrada
             lista actualmente''')
            print(a)
            raise Exception('Excepcion i igual a 7')
    except Exception as ven:
      print('''ocurrio una excepcion''')
      print(ven)
      exit()
    else:      
      print('igual me ejecuto')      
      return(a)


palindromo = lambda number: run(number)

print(palindromo(lista))
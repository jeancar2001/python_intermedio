from dbm import error
import os
import random

def archivo():
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        word = [i for i in f]
    return random.choice(word).replace("\n","")

def main():
    word = archivo()
    contador = 0
    while True:
        a = {i:{b:"___ "} for i,b in enumerate(word)}
        while True:
            os.system("clear")
            print(a)
            print("\n\n")
            if contador == 1:
                print("pierdes una vida")
                contador = 0
            b = [b for i in a.values() for b in i.values()]
            print("".join(b))
            print("\n")
            try:
                word_user = input("Ingrese una letra: ")
                if word_user.isnumeric():
                    raise Exception ("Coloque solo letras en el espacio")
            except Exception as f:
                os.system("clear")
                print(f)
                continue
            z = [i for i,p in enumerate(word) if p == word_user ]
            if len(z)==0:
                contador += 1
            
            
            break
        break
        
if __name__=="__main__":
    main()
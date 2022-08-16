import os
import random

def archivo():
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        word = [i for i in f]
    return random.choice(word).replace("\n","")

def main():
    word = archivo()
    os.system("clear")
    print("\n\n")
    while True:
        print(word)
        a = {i:{b:"___ "} for i,b in enumerate(word)}
        while True:
            b = [b for i in a.values() for b in i.values()]
            print("".join(b))
            print("\n")
            try:
                word_user = input("Ingrese una letra: ")
                if word_user.isnumeric():
                    raise Exception ("Coloque solo letras en el espacio")
            except Exception as f:
                print(f)
                continue
            pass
            break
        break
        
if __name__=="__main__":
    main()
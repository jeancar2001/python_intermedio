import os
import random

def archivo():
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        word = [i for i in f]
    return random.choice(word).replace("\n","")

def tildes(word,numer1,numer2):
    a = [("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u")]
    for i in a:
        word = word.replace(i[numer1],i[numer2])
    return word

def reemplazo(lista,word,dict):
    for i in lista:
        dict[i]=word[i].upper()+" "
    return dict



def main():
    word = archivo()
    word_tilde = tildes(word,1,0)
    word_sin_tilde = tildes(word,0,1)
    a = {i[0]:"___ " for i in enumerate(word)}
    os.system("clear")
    print("Bienvenido al Juego de ahorcado")
    while True:
        print("\n\n")
        print("".join([i for i in a.values()]))
        print("\n")
        t = list(filter(lambda i:i=="___ ",a.values()))
        if len(t)==0:
            break
        try:
            word_user = input("Ingrese una letra: ")
            if word_user.isnumeric() or len(word_user)==0:
                raise Exception ("Coloque solo letras en el espacio")
            if len(word_user)>1:
                raise Exception ("Debe colocar una sola letra")
        except Exception as f:
            os.system("clear")
            print(f)
            continue
        z = [i[0] for i in enumerate(word_sin_tilde) if i[1]==word_user]+[i[0] for i in enumerate(word_tilde) if i[1]==word_user]
        if len(z)==0:
            os.system("clear")
            continue
        a = reemplazo(z,word,a)
        os.system("clear")
        
        
if __name__=="__main__":
    main()
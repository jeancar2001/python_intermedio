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
def drew(number):
    drew = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    return drew[number]



def main():
    word = archivo()
    word_tilde = tildes(word,1,0)
    word_sin_tilde = tildes(word,0,1)
    word_user_list = []
    a = {i[0]:"___ " for i in enumerate(word)}
    os.system("clear")
    print("Bienvenido al Juego de ahorcado")
    vida = 6
    puntuacion = 0
    while True:
        print("\n")
        print(f"VIDAS: {vida}")
        print("\n\n")
        print(drew(vida))
        print("\n")
        print("".join([i for i in a.values()]))
        print("\n")
        t = list(filter(lambda i:i=="___ ",a.values()))
        if len(t)==0:
            print(f"""
Ganaste
Puntuacion: {puntuacion}
            """)
            
            break
        elif vida== 0:
            if puntuacion<0:
                puntuacion = 0
            print(f"""
Se acabaron tus vidas fin del juego
La palabra es: {word}
Puntuacion: {puntuacion}
                """)
            break
        try:
            word_user = input("Ingrese una letra: ")
            if word_user.isnumeric() or len(word_user.replace("\t","").replace(" ",""))==0:
                raise Exception ("Coloque solo letras en el espacio")
            if len(word_user)>1:
                raise Exception ("Debe colocar una sola letra")
        except Exception as f:
            os.system("clear")
            print(f)
            continue
        if len(list(filter(lambda x: x==word_user ,word_user_list))) ==1:
            os.system("clear")
            print("Ingrese otra letra no repetida")
            continue
        else:
            word_user_list.append(word_user)
        z = [i[0] for i in enumerate(word_sin_tilde) if i[1]==word_user]+[i[0] for i in enumerate(word_tilde) if i[1]==word_user]
        if len(z)==0:
            os.system("clear")
            vida -= 1
            if vida>0:
                print("PIERDES UNA VIDA")
            puntuacion -= 5
            continue
        a = reemplazo(z,word,a)
        puntuacion += 20
        os.system("clear")
        print("Bien sigue asi")
        
        
if __name__=="__main__":
    main()
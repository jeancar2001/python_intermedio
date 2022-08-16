import os
import random

def archivo():
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        word = [i for i in f]
    return random.choice(word)

def main():
    word = archivo()
    os.system("clear")
    print("\n\n")
    while True:
        print(word)
        a = {i:{b:"___ "} for i,b in enumerate(word)}
        b = [b for i in a.values() for b in i.values()]
        print("".join(b))
        break
if __name__=="__main__":
    main()
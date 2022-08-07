import math
def main():
    dictionary = {i:round(math.sqrt(i),3) for i in range(1,1001)}
    print(dictionary)



if __name__ == "__main__":
    main()
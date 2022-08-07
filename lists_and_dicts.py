def main():
    super_list = [
        {"name" : "royer" , "firstname" : "martinez"},
        {"name" : "camilo" , "firstname" : "martinez"},
        {"name" : "jose" , "firstname" : "chicay"}
    ]

    for i in super_list:
        print(i["name"], "-" , i["firstname"], end="  -  ")


if __name__ == '__main__':
    main()
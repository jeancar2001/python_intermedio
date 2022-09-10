
def main():
  with open('./archivos/data.txt','r',encoding="utf-8") as b:
    a = b.read().replace("\n","-")
  
  print(a)
    
if __name__=='__main__':
  main()
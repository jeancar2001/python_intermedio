
def main():
  a = []
  with open('./archivos/data.txt','r',encoding="utf-8") as b:
    for i in b:
      i = i.replace("\n","")
      a.append(i)
  
  print(a)
    
if __name__=='__main__':
  main()
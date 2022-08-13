def main():
  a = 'hola mundo'
  with open('./archivos/number.txt','a',encoding='utf-8') as f:
    f.write(a)
    
if __name__=='__main__':
  main()
#print("""
#        bbbbbbbbb   b  bbbbbb b     b b           b bbbbbb b     b  b  bbb        bbb
#        b        b  b  b      bb    b  b         b  b      bb    b  b  b   b    b     b
#        b       b   b  b      b b   b   b       b   b      b b   b  b  b    b  b       b
#        bbbbbbbb    b  bbbbbb b  b  b    b     b    bbbbbb b  b  b  b  b    b  b       b
#        b       b   b  b      b   b b     b   b     b      b   b b  b  b    b  b       b
#        b        b  b  b      b    bb      b b      b      b    bb  b  b   b    b     b 
#        bbbbbbbbb   b  bbbbbb b     b       b       bbbbbb b     b  b  bbb        bbb
#        """)


from wsgiref.validate import InputWrapper


a = ['''
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
print(len(a))
print(a[int(input("intrduzca"))])
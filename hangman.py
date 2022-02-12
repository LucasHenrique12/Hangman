import random


board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

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
/|\\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']

class Hangman:
    def __init__(self,word):
        self.word=word
        self.guessed_letters=[]
        self.missed_letters=[]
    
    def guess(self,letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        elif letter not in self.word:
            self.missed_letters.append(letter)
            return False
    
    def game_over(self):
        if (len(self.missed_letters)==6):
            return True
        else:
            self.winner()
           
    
    def winner(self):
        if self.guessed_letters== self.word:
            return True
        else:
            return False
    
    def hide_word(self):
        rtn=''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn +='_'
            else:
                rtn+= letter
        return rtn
    
    def print_game_status(self):
        if (len(self.missed_letters)<=6):
            print(board[len(self.missed_letters)])
        print('\nPalavra: '+ self.hide_word())
        print('\nLetras erradas: ',)
        for letter in self.missed_letters:
            print(letter,)
        if(len(self.missed_letters)>6):
           return self.game_over()


def rand_word():
    with open("basico_de_python\\POO_python\\jogo_da_forca\\palavras.txt", "rt") as f:
        bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip()
    

    
    
                 
        

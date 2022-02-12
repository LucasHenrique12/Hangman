from hangman import Hangman
from hangman import rand_word

def main():
    game=Hangman(rand_word())
    
    while not game.game_over():
        game.print_game_status()
        user_input = input('\nDigite a proxima letra')
        game.guess(user_input)
    game.print_game_status()

    if game.game_over():
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)
        print('\nFoi bom jogar com você!\n')
        
    elif game.winner(): 
       print('\nParabéns! Você venceu!!')
       print('\nFoi bom jogar com você!\n')
    
if __name__ == '__main__':
    main()
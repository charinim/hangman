from random import choice, random, randint

dictionary_file = "dictionary.txt"  


l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []
l10 = []
l11 = []
l12 = []

with open('dictionary.txt', 'r') as dictionary_file:
    x = dictionary_file.readlines()
    for i in x:
        m = i.strip()
        k = m.strip('\n')
        if len(m) == 2:
            l2.append(m.strip('\n'))
        elif len(m) ==3:
            l3.append(m.strip('\n'))
        elif len(m) ==4:
            l4.append(m.strip().strip('\n'))
        elif len(m) ==5:
            l5.append(m.strip().strip('\n'))
        elif len(m) ==6:
            l6.append(m.strip().strip('\n'))
        elif len(m) ==7:
            l7.append(m.strip().strip('\n'))
        elif len(m) ==8:
            l8.append(m.strip().strip('\n'))
        elif len(m) ==9:
            l9.append(m.strip().strip('\n'))
        elif len(m) ==10:
            l10.append(m.strip().strip('\n'))
        elif len(m) ==11:
            l11.append(m.strip().strip('\n'))
        else:
            l12.append(m.strip().strip('\n'))


def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    try :
        dictionary[2] = l2
        dictionary[3] = l3
        dictionary[4] = l4
        dictionary[5] = l5
        dictionary[6] = l6
        dictionary[7] = l7
        dictionary[8] = l8
        dictionary[9] = l9
        dictionary[10] = l10
        dictionary[11] = l11
        dictionary[12] = l12
    except Exception :
        pass
    return dictionary


def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary)


def get_game_options () :

    try:
        size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]: \n"))
        
        if size>12 or size<3:
            size = randint(3,12)
        print(f'A dictionary word of {size} letters will be chosen\n')

    except:
        print("A dictionary word of any size will be chosen.\n")
        size = randint(3,12)
    
    
    
    try:

        lives = int(input("Please choose a number of lives [1 - 10, default 5]: \n"))
        
        if lives>10 or lives<1:
            lives = randint(1,10)
        print(f'You have {lives} lives.\n')
    except:
        print("You have 5 lives.\n")
        lives = 5
    
    
    return (size, lives)



if __name__ == '__main__' :


    print("\nWelcome to the Hangman Game!\n")
    
    dictionary = import_dictionary(dictionary_file)
    
    
    x = 'y'
    while x == "y" or x == "Y":
        (size, lives) = get_game_options()
        chosen_word = choice(dictionary[size])
        chosen_word = chosen_word.upper()
        letters = []
        
        dash = []
        for i in range(size):
            dash.append("__")
        
        life = list('O'*lives)

        if '-' in chosen_word:
            a = '-'.index(chosen_word)
            dash[a] = '-'
        
        
        
        print(f'Letters chosen: {" ".join(letters)}\n')
        print(f'{" ".join(dash)}   lives: {"".join(life)}\n')

            
        while "__" in dash and 'O' in life:
            s = (input("Please choose a new letter > ")).upper()

            while s in letters:
                s = input("You have already chosen this letter \nPlease choose a new letter > ").upper()
            letters.append(s)
            
            if s in chosen_word:
                print("You guessed right!\n")
                print(f'Letters chosen: {" ".join(letters)}\n')
                
                w = []
                for i in range(len(chosen_word)):
                    if chosen_word[i] == s:
                        w.append(i)
                for i in w:
                    dash[i] = chosen_word[i]
                
                print(f'{" ".join(dash)}   lives: {"".join(life)}')
                
            else:
                print("You guessed wrong, you lost one life.\n")
                print(f'Letters chosen: {" ".join(letters)}\n')
                life[life.index("O")]="X"
                print(f'{" ".join(dash)}   lives: {"".join(life)}')
                
        
            
            if "O" not in life and "__" in dash:
                print(f"You lost! The word was {chosen_word}!\n")
            elif "O" in life and "__" not in dash:
                print("You won!!\n")


        x = input("Would you like to play again [Y/N]?")
    else:
        print("\nGoodbye!") 
        

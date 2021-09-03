from random import randint
from time import sleep 
from os import system


def number_guesser():


    total_guesses = 1

    try:
        x = int(input('Enter the lowest number here : '))
        y = int(input('Enter the highest number here : '))
        a = randint(x, y)
    except:
        print('Incorrect input!')
        sleep(1)
        number_guesser()


    while True:
        try: 
            x = int(input('Enter your guess here : '))
            sleep(0.3)
        except: 
            print('Incorrect input!')
            sleep(0.5)
            continue

        if x == a:
            print('Correct, you won! You guessed' ,total_guesses, 'times. Do you want to go again?')
            c = str(input('Y / N : '))

            if c == 'y' or c == 'Y':
                system('cls')
                number_guesser()
            elif c == 'n' or c == 'N':
                print('Okay, goodbye.')
                sleep(1)
                system('cls')
                exit()
            else:
                print('Fuck youuuuu')
                sleep(1)
                exit()
                    
                        
        elif x < a: 
            print('Incorrect, you guessed too low! Try again.')
            total_guesses += 1

        elif x > a:
            print('Incorrect, you guessed too high! Try again.')
            total_guesses += 1
            

        else:
            print('Fuck youuu')
            sleep(1)
            exit()


number_guesser()
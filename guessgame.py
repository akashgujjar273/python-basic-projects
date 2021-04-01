from random import randint

def game():
    
    turn=1
    guess_limit=5
    secret=randint(1,10)
    while turn<guess_limit:
        print(secret)
        user=int(input("Enter your number:\n"))
        turn=turn+1
        if user==secret:
            print("you guessed it right")
            break
        elif user>secret:
            print("its higher number guess low")
        elif user<secret:
            print("its lower number guess high")
        elif turn<guess_limit:
            print("GAME OVER")
        
    

a=game()
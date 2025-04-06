import random

def random_number_game(guessed_number):
    randoly_generated_number = random.randint(1,10)
    randoly_generated_number = int(randoly_generated_number)
    
    while(guessed_number != randoly_generated_number):
        if(guessed_number < randoly_generated_number):
            print("Your guess is too low")
        elif guessed_number>randoly_generated_number:
            print("Your guess is too high")

        guessed_number = input("please guess a number between 1-10\n")
        guessed_number = int(guessed_number)
    print(f"Congrats you guessed the number {guessed_number} correctly")

guessed_number = input("please guess a number between 1-10\n")
guessed_number = int(guessed_number)
random_number_game(guessed_number)
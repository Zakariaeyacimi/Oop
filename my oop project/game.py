import random

class game:
     
  def create_number_guesser(self):

 
    print("Guess a number between 1 and 188. I'll tell you if the number is lower or higher than your guess.")
     
    rand_number = random.randint(1, 108)
    guess = None
    
    while rand_number != guess:
       s = input("Your guess: ")
       guess = int (s)
       if rand_number > guess:
        print("Higher")
       elif rand_number < guess:
        print("Lower")
    
       else:
            print("You guessed it! The number is ()".format(rand_number))


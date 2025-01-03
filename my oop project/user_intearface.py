from manager import *
from game import *
#from user_check import*


class user_intearface :
    def __init__(self):
        self.manager = manager()
        self.game=game()
    #self.user_check=user_check()
    def print_menu(self):
    
        print("\nprogram options: ")
        messages = [
            '1) new logain',
            '2) play a game',
            '3) Delete account by name',
            '4) End the program',
            
        ]
        print('\n'.join(messages))
        msg = f'Enter your choice ( from 1 to {len(messages)})'
        return input_is_valid(msg, 1, len(messages))

        
        
       
    def run (self):
        
            
        while True:    
            choice=self.print_menu()
            if choice == 1:
                self.manager.add_user()
            elif choice == 2:
                self.game.create_number_guesser()
            elif choice ==3: 
                input_name = (input("Enter your name : \n"))
                self.manager.dellete_user()
            elif choice ==4:
                print ('task is ended')
                break
            else:
               
               break   

from manager import *
from inp import *
class manager_interface :
    def __init__(self):
        self.manager =manager()


    def print_menu(self):
        print("\nprogram options: ")
        messages =[
            '1) add new user',
            '2) List all users',
            '3) Delete account',
            '4) End the program'
        ]
       
        print('\n'.join(messages))
        msg = f'Enter your choice ( from 1 to {len(messages)})'
        return input_is_valid(msg, 1, len(messages))

    def main(self,input_name):
        self.input_name=input_name
        while True :
            choice = self.print_menu()
            if choice == 1:
                self.manager.add_user()
            elif choice == 2:
                self.manager.users_list()
            elif choice ==3:
                input_name=input('enter name ')
                self.manager.dellete_user(self.input_name)

            elif choice ==4:
                self.manager. end_tasks()
            else:
                
                break
             

            
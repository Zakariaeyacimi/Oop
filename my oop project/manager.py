from chatbot import *
from inp import *
class manager:  
   
  def __init__(self):
    self.user = []
  
  def add_user(self):
   
    print('Enter user data')
    name =input("Enter user name\n")
    age=input_is_valid("Enter user age: \n")
    gender=input("Enter user gender: \n")
    self.user.append(chatbot(name, age,gender))
    
  
  def users_list(self):

    if len ( self.user)==0:
      print ('list is empty')
      return
    else:                                                                                                                                     
      for usr in self.user :
        print(usr)

  def dellete_user(self,input_name):
    self.input_name=self.input_name
    for usr in self.user:
      if self.input_name == self.usr(name):
        print (f'\tuser deleted{usr.input_name}')
      self.user.remove(usr)
      
 
  

                                                                                                                                                                                                                                                                                        
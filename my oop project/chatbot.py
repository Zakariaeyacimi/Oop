
class chatbot:
    def __init__(self,name,age,gender):
          
        self.name=name
        self.age=age
        self.gender=gender
    def __str__(self):
        return F'the user {self.name} has age {self.age} ,and gender {self.gender}'
    
    def __repr__(self):
       return F'user(name={self.name}, age={self.age},gender {self.gender}'

    

#constructor
'''class Dog:
    def __init__(self, name, age):
       self.name= name
       self.age= age
my_dog=Dog("Buddy",3)
print(my_dog.name)'''

   #method overriding
'''class Dog:
    def __init__(self, name, age=0):
       self.name= name
       self.age= age
puppy=Dog("Max")     #age defaults to 0
adult=Dog("Buddy",3) #age overridden to 3
print(puppy.name,puppy.age)
print(adult.name,adult.age)'''

  #full step of constructor
'''class BankAccount:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance

    def display(self):
        print("Name:",self.name)
        print("Account:",self.account_number)
        print("Balance:",self.balance)

account1=BankAccount("Eldhos","331207",100000)
account2=BankAccount("John","331208",50000)

account1.display()
account2.display()'''

#iterator
     #iter
'''numbers=[10,20,30]
iterator=iter(numbers)
#print(iterator)      #iter

print(next(iterator))  #next
print(next(iterator))
print(next(iterator))
print(next(iterator))'''

#Generator
'''def numbers():
    yield 1
    yield 2
    yield 3
print(numbers)'''

  # full step of generator
'''def numbers():
    yield 1
    yield 2
    yield 3'''
#result=numbers()
#print(result)
'''print(next(result))
print(next(result)) 
print(next(result))
print(next(result))'''

'''for number in numbers(): #work in loop
    print(number)'''  

#decorator
''' def decorator_function(function):
    def wrapper():
        print("Before the function is called.")
        function()
        print("After the function is called.")
    return wrapper
@decorator_function
def greet():
    print("Hello!")
greet()'''

#decorator with arguments
'''def decorator_function(function):
    def wrapper(name):
        print("Before function.")
        function(name)
        print("After function.")
    return wrapper
@decorator_function
def greet(name):
    print("Hello,", name)
greet("Eldhos")'''

#Abstract
'''from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(vehicle):
    def start(self):
        print("Car starts.")

car=Car()
car.start()'''

'''class student:
    def __init__(self,):
        self.name="Eldhos"
        self._age=20
        self.__marks=95
Student = student()
print(Student.name)      #public
print(Student._age)      #protected 
print(Student.__marks)   #private'''   

class student:
    def __init__(self,marks):
        self.__marks=marks
    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
            self.__marks=value
        else:
            print("Invalid Marks")

s1=student(90)
print(s1.marks)  
s1.marks=95     
print(s1.marks)  






















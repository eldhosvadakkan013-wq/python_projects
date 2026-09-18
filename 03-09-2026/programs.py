# Inheritance
'''class Animal: #parent class
    def eat(self):
        print("Animal is eating.")

class Dog(Animal): #child class
    def bark(self):
        print("Dog is barking.")

d=Dog()

d.eat()
d.bark()'''

#method overriding
'''class Animal: #parent class
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal): #child class
    def sound(self):
        print("Dog barks.")

a=Animal()
d=Dog()

a.sound()
d.sound()'''

#Example of Inheritance
'''class Vehicle:
    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

car1=Car()
car1.start() #Inherited method
car1.drive() #child class method'''

#method polymorphism
class Dog:
    def sound(self):                   #sound is the common method name in both classes
        print("Dog barks.")

class Cat:
    def sound(self):             
        print("Cat meows.")    

def make_sound(animal):
    animal.sound()

dog=Dog()
cat=Cat()
make_sound(dog)
make_sound(cat)
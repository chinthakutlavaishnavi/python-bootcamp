class Animal:
    def  speak():
          return"Animal is speaking"
    #SINGLE inh
class Dog(Animal):
    def bark():
          return"Bow-----"
obj1=Animal
obj2=Dog
print(obj1.speak())
print(obj2.bark())
#multi level inheritance
class puppy(Dog):
     def puppy_speak():       
          return"im puppy"
obj3=puppy
print(obj3.puppy_speak())
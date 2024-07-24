class animal:
    def speak():
        return "speaking...."
class dog(animal):
    def speak():
        return" dog is speaking....."
class puppy(dog):
    def speak():
        return"puppy is speaking...."
obj1=puppy
print(obj1.speak())
    
def run():
        return"running"
def run():
        return"hello"
print(run())
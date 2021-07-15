class Toy:
    def talk(self):
        raise NotImplementedError("This method should implement by childclass")

class Dog(Toy):
    def talk(self):
        print("Wow")
class Cat(Toy):
    def talk(self):
        print('Meow')
class ToyFactory:
    def getToy(self, type):
        if type == "Cat":
            return Cat()
        if type == "Dog":
            return Dog()
        return None
tf = ToyFactory()
a = tf.getToy('Dog')
a.talk()




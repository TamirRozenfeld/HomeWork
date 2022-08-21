# (1)
class HoneyBee:

    def __init__(self, color, environment, age, name):
        self.color = color
        self.environment = environment
        self.age = age
        self.name = name

class Adult_male(HoneyBee):

    def sting(self):
        pass

    def food(self):
        print("my foods are nectar and pollen")

    def speak(self):
        print("Zzzzzz")

    def function(self):
        pass

    def flight(self):
        print("I have wings")

    def Identification(self):
        print(f"My color {self.color} i live in {self.environment} my age {self.age} days and my name is {self.name}")


class Egg(HoneyBee):

    def function(self):
        pass


    def Identification(self):
        print(f"My color {self.color} i live {self.environment} my age {self.age} day and my name is {self.name}")


class Larva(HoneyBee):

    def function(self):
        pass

    def Identification(self):
        print(f"My color {self.color} i live {self.environment} my age {self.age} days and my name is {self.name}")


class Pupa(HoneyBee):

    def function(self):
        pass

    def flight(self):
        print("I have small wings")

    def Identification(self):
        print(f"My color {self.color} i live {self.environment} my age {self.age} days and my name is {self.name}")


class Queen(HoneyBee):

    def sting(self):
        pass

    def flight(self):
        print("I have wings")

    def food(self):
        pass
        print("my foods are nectar and pollen")
    def speak(self):
        print("Zzzzzz")

    def function(self):
        pass

    def Identification(self):
        print(f"My color {self.color} i live in {self.environment} my age {self.age} days and my name is {self.name}")




b = Adult_male("light brown","meadows", 21, "Tamir" )
b.Identification()
b.speak()
b.flight()
b.food()
c = Queen("light brown","meadows", 16,"Ron")
c.Identification()
c.speak()
b.flight()
b.food()
d = Pupa("whitish", "inside a honeycomb", 8 ,"Yael")
d.Identification()
b.flight()
e = Larva("whitish", "inside a honeycomb", 4,"Kobi")
e.Identification()
f = Egg("whitish", "inside a honeycomb", 1,"David")
f.Identification()


# (2)
# The problems that might arise from scaling such a game on one machine could
# be the same problems that happened to me in my last project(Object Detection) when i tried to run the training command,
# it had to run for a long time. With million of bees in all stages moving around, my computer would probably crash, this is why
# clouds/hadoops developed, these apps using maps reduce in order to make things more accesible by using multiple machine
# at the same time and by this making  all the process more efficient and faster.
# more advantage could be that more machines easily added if necessary, And a failure of one machine arn't leading to failure of the entire system
# other machines can still communicate with each other.

#(3)
# 1.It is difficult to provide adequate security in distributed systems because the nodes as well as the connections need to be secured.
# 2.Some messages and data can be lost in the network while moving from one node to another.
# 3.The database connected to the distributed systems is quite complicated and difficult to handle as compared to a single user system.
# 4.Overloading may occur in the network if all the nodes of the distributed system try to send data at once.

(4)









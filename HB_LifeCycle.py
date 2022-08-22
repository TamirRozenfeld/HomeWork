# (1)
from functools import cache
Bear = "Big and Brown"
Food = "nectar"
class HoneyBee:
    @cache
    def __init__(self, color, environment, age, name,):
        self.color = color
        self.environment = environment
        self.age = age
        self.name = name

class Adult_male(HoneyBee):

    @cache
    def food(self):
        print("Sucks when u see something beautiful, aromatic, colourful, garden-fresh and decagon")


    @cache
    def speak(self):
        print("Zzzzzz every 5 seconds")

    @cache
    def function(self):
        print("When i see head with two antennae, a thorax with six legs and red lower body press Mating function")

    @cache
    def run(self):
        for i in range(len(Bear)):
            print(Bear[i])
            if i == 4:
                print("run!")
            elif i == 5:
                print("Zzzz")

    @cache
    def mating(self):
            print("Go over the object and press bomb")
    @cache
    def bomb(self):
            print("Throw the bomb and press on suicide")
    @cache
    def suicide(self):
        print("Trow self bomb")
    @cache
    def flight(self):
        print("push and pull")

    @cache
    def Identification(self):
        print(f"I'm adult male my color {self.color} i live in the {self.environment} my age is {self.age} days and my name is {self.name}")


class Egg(HoneyBee):

    @cache
    def Identification(self):
        print(f"I'm Egg my color is {self.color} i live {self.environment} my age is {self.age} day and my name is {self.name}")

class Larva(HoneyBee):
    @cache
    def food(self):
        print("When i see two head with two antennae, a thorax with six legs press feed")

    @cache
    def feed(self):
        print("Open mouth and press suck")

    @cache
    def suck(self):
        print("Press button one")

    @cache
    def one(self):
         print("Done sucking")

    @cache
    def Identification(self):
        print(f"I'm Larva  my color is {self.color} i live {self.environment} my age is {self.age} days and my name is {self.name}")


class Pupa(HoneyBee):
    @cache
    def flight(self):
        print("press on red button in order to open the hole for the wings")

    @cache
    def Identification(self):
        print(f"I'm Pupa My color {self.color} i live {self.environment} my age is {self.age} days and my name is {self.name}")

class Queen(HoneyBee):

    @cache
    def sting(self):
        print(f"When i see a head with two antennae, a thorax with six legs, and an abdomen that i haven't seen before,i push and pull my wings, press on my attack button")

    @cache
    def waggeling(self):
        if Food == "nectar":
            print("Back to hive")

            @cache
            def pull_trigger():
                print("dance")

    @cache
    def attack(self):
        print("Shoot an arrow")

    @cache
    def flight(self):
        print("Push and pull")

    @cache
    def food(self):
        print("Sucks when I see something beautiful, aromatic, colourful, garden-fresh")

    @cache
    def speak(self):
        print("Zzzzzz every 5 seconds")

    @cache
    def function(self):
        print("When all cell empty i should laying my eggs")

    @cache
    def run(self):
        for i in range(len(Bear)):
            print(Bear[i])
            if i == 4:
                print("run!")
            elif i == 5:
                print("Zzzz")
    @cache
    def Identification(self):
        print(f"I'm the Queen my color {self.color} i live in the{self.environment} my age is {self.age} days and my name is {self.name}")








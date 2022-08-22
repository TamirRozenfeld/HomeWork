# (1)
from functools import cache


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
        print("My foods are nectar and pollen")

    @cache
    def speak(self):
        print("Zzzzzz")

    @cache
    def function(self):
        print("My function is  mating with the queen")

    @cache
    def flight(self):
        print("I have wings")

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
        print("My parents feed me Larva royal jelly")

    @cache
    def Identification(self):
        print(f"I'm Larva  my color is {self.color} i live {self.environment} my age is {self.age} days and my name is {self.name}")


class Pupa(HoneyBee):
    @cache
    def flight(self):
        print("I have small wings")

    @cache
    def Identification(self):
        print(f"I'm Pupa My color {self.color} i live {self.environment} my age is {self.age} days and my name is {self.name}")

class Queen(HoneyBee):
    @cache
    def sting(self):
        print("my sting Uses for dispatching rival queens")

    @cache
    def flight(self):
        print("I have wings")

    @cache
    def food(self):
        print("My foods are nectar and pollen")

    @cache
    def speak(self):
        print("Zzzzzz")

    @cache
    def function(self):
        print("I live for Laying eggs")

    @cache
    def Identification(self):
        print(f"I'm the Queen my color {self.color} i live in the{self.environment} my age is {self.age} days and my name is {self.name}")








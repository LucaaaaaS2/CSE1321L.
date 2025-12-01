class Dog:
    def __init__(self, age, weight, name, furColor, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.furColor = furColor
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def rename(self, newName):
        self.name = newName

    def eat(self, foodWeight):
        self.weight += foodWeight


print("You are about to create a dog.")
age = int(input(" How old is the dog: "))
weight = float(input(" How much does the dog weigh: "))
name = input(" What is the dog's name: ")
fur = input(" What color is the dog: ")
breed = input(" What breed is the dog: ")

dog = Dog(age, weight, name, fur, breed)

print(f" {dog.name} is a {dog.age} year old {dog.furColor} {dog.breed} that weighs {dog.weight} lbs.")
dog.bark()

food = float(input(f" {dog.name} is hungry, how much should he eat: "))
dog.eat(food)

new_name = input(f" {dog.name} isn't a very good name. What should they be renamed to: ")
dog.rename(new_name)

print(f" {dog.name} is a {dog.age} year old {dog.furColor} {dog.breed} that weighs {dog.weight} lbs.")
from random import randint

name = input("Say your name you idiot, with more than 3 letters or else")

num = randint(1,1383)

List = open("list.txt").readlines()

print(name, "you are a",List[num])

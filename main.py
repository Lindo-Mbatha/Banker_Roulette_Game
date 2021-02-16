import random
print("Banker Roulette")

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random = random.choice(names)

print(random)

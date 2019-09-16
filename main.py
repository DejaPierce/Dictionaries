birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/06/1705",
    "Ada Lovelace": "12/10/1815"
}

lst = birthdays.keys()

print("We know the birthday of:")

for x in lst:
    print(x)

choice = input("Who's birthday do you want to look up?")

if choice in lst:
    print("{}'s birthday is {}.".format(choice, birthdays[choice]))
else:
    print("We don't know {}'s birthday".format(choice))
# String
myName = "Ranjith";
print(myName)

quote1 = "Ranjith!, it's me"
print(quote1)

quote2 = 'Hello! "Good Morning!!"'
print(quote2)

# multiline string
address = """
2nd Street,
Gandhi Nagar,
Chennai,
600078
"""
print(address)

# string concat

firstname = "Ranjith"
lastname = "Sekar"
name = firstname + " " + lastname
print (name)

# convert number to string
age = 34
nameAge = firstname + " " + str(age);
print(nameAge)

print(f"your age: {age}")

animal = "Animal"
animalValue = f"Species is: {animal}"
print(animalValue)

animalValue = "Bird"
print(animalValue)
# to overcome above issue

animal2 = "Elephant"
animalValue2 = "Species is: {}?"  # kidn of template
animalValue21 = animalValue2.format(animal2)
print(animal2)
animal2 = "Tiger"
print(animal2)

greetName = "Bal"
greeting = "How are you: {}?"
greetingVal = greeting.format(greetName)
print(greetingVal)

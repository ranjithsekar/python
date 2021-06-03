myname = "Ranjith"


def display():
    myname = "Ranjith Sekar"
    print(myname)


display()

print(myname)


def display1():
    global greeting
    greeting = "Good Morning"


display1()
print(greeting)

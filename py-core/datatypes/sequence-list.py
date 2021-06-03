fruits = ["mango", "orange", "apple", "apple"]
print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[-3])

print(fruits[2:5])

if "orange" in fruits:
    print("Yes, present!!")

fruits[-3] = "kiwi"
print(fruits)

fruits.insert(3, "banana")
print(fruits)

fruits.append("grapes")
print(fruits)

veg = ["brinjal", "carrot"]
fruits.extend(veg)
print(fruits)
veg.extend(fruits)
print(veg)

for i in fruits:
    print(i)

for i in range(len(fruits)):
    print("test: " + str(i))

### REMOVE
print(veg)
veg.remove("banana")
print(veg)

veg.pop(1)
print(veg)

veg.pop()
print(veg)

veg.pop()
print(veg)

del veg[0]
print(veg)


name = 'Ranjith'
print(len(name))
print(name.count('a'))
print(name.upper())  # original string won't be  modified
print(name.lower())
print(name.find('j'))
print(name.find('H'))  # find returns index
print(name.find('an'))
print(name.replace('ji', 'gi'))
print('jith' in name)  # checks contains
print('jith' not in name)  # checks contains
if 'jith' in name:
    print('Yes, present!!!')
print(len(name))

print("ranjith,sekar".split(","))   # returns array

for i in name:
    print(i)


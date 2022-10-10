# using 'with' is recommended
with open('files/fruits.txt') as myfile:
    content = myfile.read()
    print(content)

# basic writing
with open('files/vegetables.txt', 'w') as myfile:
    myfile.write("Tomato\nOnion\nCucumber")

# append to existing file. '+' is to open for reading and writing
with open('files/vegetables.txt', 'a') as myfile:
    myfile.write('\nOkra')
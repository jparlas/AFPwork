print('Hello world')

name = input('You? ')
age = int(input('Age ? '))

#the comma simply outputs the result
print('Hello ', name, age)

#the + tries to construct a string to display
#and it will only work with int if they are
#converted to string first
print('Hello ' + name + str(age))

print('Hello {0} you are {1} years old'.format(name, age))


file = open("stuff.txt")
for line in file:
    print(line.strip('\n'))
    words = line.strip('\n').split(' ')
    print(words)



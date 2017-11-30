#create a main function that runs when this file is executed
def main():
    print('Hello')
    print('This program will present a variety of converters')
    print('for you to use.')
    print('--------------------------------------------')
    menu()

def menu():
    choice = '0'
    while choice == '0':
        print("1: Fahrenheit to Celcius")
        print("2: Miles to Kilometers")
        print("3: To quit")
        choice = input("Please make a choice: ")
        if choice == "3":
            print("Quitting.. ")
            break
        elif choice == "2":
            #call the m2km function
            print('hi')
            menu()
        elif choice == "1":
            val = int(input('Enter a temperature'))
            cel = ftoc(val)
            print('{0} Fahrenheit = {1:.2f} Celcius'.format(val, cel))
            menu()
        else:
            print("I don't understand your choice.")
            menu()



#create a function to convert fahrenheit to celcius
def ftoc(fah):
    cel = (fah-32) * 5/9
    return cel

main()

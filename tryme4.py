def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():    #this function prints a string and nine lines using "three_lines()" three times.

    three_lines()
    three_lines()
    three_lines()


def clear_screen():  #This function prints a string and twenty five lines using a combination of the functions above.
    print("Printing 25 lines")
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print("Printing 9 lines")
nine_lines() #Calling nine_lines.

clear_screen() #Calling clear_screen.

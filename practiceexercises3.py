# def sum_of_numbers(no1, no2, no3):
#     if no1 == no2 or no1 == no3 or no2 == no3:
#         print("The sum of these numbers is: 0")
#     else:
#         total = no1 + no2 + no3
#         print(f"The sum of these numbers is: {total}")


# no1 = int(input("Enter the first number: "))
# no2 = int(input("Enter the second number: "))
# no3 = int(input("Enter the third number: "))
# sum_of_numbers(no1, no2, no3)

# def sum_of_numbers(no1, no2):
#     total = no1 + no2
#     total_range = range(15, 20)
#     if total in total_range:
#         total = 20
#         print(f"The sum of the numbers is: {total}")
#     else:
#         print(f"The total of the numbers is: {total}")


# no1 = int(input("Enter the first number: "))
# no2 = int(input("Enter the second number: "))
# sum_of_numbers(no1, no2)

# def true_program(int1, int2):
#     add = int1 + int2
#     diff = int1 - int2
#     if int1 == int2 or add == 5 or diff == 5:
#         print("True")
#     elif add != 5:
#         print(f"The sum of the numbers you have entered is: {add}")
#     elif diff != 5:
#         print(f"The difference of the numbers you have entered is: {diff}")
#     else:
#         print("Error.")
# int1 = int(input("Enter your first integer number: "))
# int2 = int(input("Enter your second integer number: "))
# true_program(int1, int2)

# name = input("Name: ")
# age = int(input("Age: "))
# address = input("Address: ")
# print("YOUR DETAILS")
# print(f"Name: {name} \nAge: {age} \nAddress: {address}")

# Program to find compound interest
# import math
# principal = float(input("Enter the principal amount: "))
# interest_rate = float(input("Enter the rate of interest: "))
# time = float(input("Enter the amount of time in years: "))
# compound_interest = principal * pow(1 + interest_rate/100, 7)
# print(f"The compound interest is: {compound_interest}")

# Program to find square of numbers(x,y)
# x = float(input("Enter your first number: "))
# y = float(input("Enter your second number: "))
# square = pow(x + y, 2)
# print(f"The square of the sum of the numbers you've entered is: {square}")

# Program to find whether a file exists in the current directory
# import os.path
# file = input("Enter the name of the file inclusive of its extension: ")
# condition = os.path.exists(file)
# if condition is True:
#     print("The file you have entered exists in the current directory.")
# else:
#     print("The file you have entered does not exist in the current directory.")

# Program to print the calendar of a specific year
# import calendar
# print(calendar.calendar(2022))

# Program to find length of string
# word = input("Enter a word: ")
# length = len(word)
# print(f"The length of the word you have entered is: {length}")

# Program to count frequency of characters in a word
# word = input("Enter a word/phrase/sentence: ")
# for character in word:
#     char_count = character.count(character)
#     print(f"Frequency of each character: {character} -> {char_count}")


# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# final_string = string2 + " " + string1
# print(final_string)

from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press_button(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equal_press():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()





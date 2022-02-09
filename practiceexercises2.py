# Program to print documents of Python built-in functions
# functions = input("Enter function name: ")
# built_in_functions = {
#    "abs()": "abs(number) -> number \n Returns the absolute value of a number.",
#    "print()": "print(any data type) -> any data type \n Displays argument on screen.",
#    "input()": "input(string) -> string \n Allows user to enter data, which is of type string by default, into a program.",
#    "bin()": "bin(int) -> int \n Converts an integer to a binary value",
#    "complex()": "complex(number) -> \n Creates a complex number"
# }
# result = ""
# for function in functions:
#    result += built_in_functions.get(function, "!")
# print(result)

# print(abs.__doc__) - doc magic function shows the purpose of specified function

# Program to check whether a specified value is within a group of values.
# values = [1, 3, 5, 8, 5]
# spec_value = int(input("Enter a number: "))
# if spec_value in values:
#    print("True." + " " + "Here is the list: \n" + str(values))
# else:
#    print("False." + " " + "Here is the list: \n" + str(values))

# Program to find whether a number is even or odd
# number = int(input("Enter a number: "))
# if number / 2 and number % 2 == 0:
#    print("You have entered an even number.")
# else:
#    print("You have entered an odd number.")


# Program to find area of a triangle
# height = float(input("Enter the height of the triangle: "))
# base = float(input("Enter the base of the triangle: "))
# area = 0.5 * base * height
# print(area)

# Program to print the colors which are unique to one set
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print(color_list_1.difference(color_list_2))

# color_list_1 = ["White", "Black", "Red"]
# color_list_2 = ["Red", "Green", "Blue"]
# color = "Red"
# if color in color_list_2 and color_list_1:
#    print(color_list_1[0:2])

# def diff_btwn_number_and_17():
#    if number < 17:
#        print(17 - number)
#    elif number > 17:
#        diff = 17 - number
#        absolute = abs(diff)
#        print(absolute * 2)


# number = int(input("Enter a number here: "))
# diff_btwn_number_and_17()

# def sum_of_three_numbers(no1, no2, no3):
#    if no1 == no2 == no3:
#        total = no1 + no2 + no3
#        print(total * 3)
#    else:
#        total = no1 + no2 + no3
#        print(total)


# no1 = int(input("Enter the first number: "))
# no2 = int(input("Enter the second number: "))
# no3 = int(input("Enter the third number: "))
# sum_of_three_numbers(no1, no2, no3)

# old_string = input("Enter a sentence: ")
# if "is" not in old_string:
#    print("Is " + old_string)
# else:
#    print(old_string)

# Program to print even numbers in list less than 237
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 743, 527
# ]
# for number in numbers:
#     if number % 2 == 0 and number < 237:
#         print(number)

# letter = input("Enter a letter: ")
# vowels = "aeiou"
# if letter in vowels:
#     print("You've entered a vowel.")
# else:
#     print("You've entered a consonant.")

# number_list = list(input("Enter your list: "))
# print(f"Your list: {number_list}")
# if '4' in number_list:
#     count = number_list.count('4')
#     print(f"Number of 4s in your list: {count}")
# else:
#     print("4 is not in your list.")
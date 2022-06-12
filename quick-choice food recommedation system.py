# Import the random function to assist in random generation of food choices.
import random
# Prompt user for their name and say introduce the user to the system.
user_name = input("Please enter your name: ")
print("Hello " + user_name + ". Welcome to Quick-Choice Food Recommendation System :)")
# Whitespace for separation of code.
print(" ")
# Display the available flavors of food.
print("Our food flavors: \n 1. Sweet \n 2. Salty \n 3. Sour")
food_craving = int(input("Please enter the number of the food flavor that best suits you currently from the list given above: "))

print(" ")
# Display levels of hunger for user to choose from.
print("Level of hunger: \n 1. Lightly hungry \n 2. Mildly hungry \n 3. Very hungry")
hunger_level = int(input("Great! Now enter the number that best represents your hunger level from the list given above: "))

print(" ")
# List of sweet foods corresponding to the levels of hunger.
sweet_and_light = ["Dark chocolate", "Granola bar", "Mini yogurt", "Dates", "Medium-sized bottle of sugarcane juice", "Fruit tart", "Cupcake"]
sweet_and_mild = ["Fruit salad", "Cake slice", "Oatmeal pancakes", "Pumpkin pie", "Cinnamon roll", "Cherry tomatoes", "Crepes"]
sweet_and_heavy = ["Fruit smoothie", "Chocolate croissant", "Oatmeal with apple slices", "Sugar and cinnamon toast", "Sandwich with jam", "Sandwich with banana"]
# List of salty foods corresponding to the levels of hunger.
salty_and_light = ["Pumpkin soup", "Lightly salted nuts", "Beef jerky", "Pretzel", "Salted caramel cake slice"]
salty_and_mild = ["Ham sandwich", "Homemade french fries", "Homemade crisps", "Grilled beef with light salad dressing", "Baked beans and toast"]
salty_and_heavy =["Rice and tuna", "Seafood boil with prawns", "Whole grain macaroni and cheese", "Chicken noodle soup", "Black beans in whole grain tortilla wrap"]
# List of sour foods corresponding to the levels of hunger.
sour_and_light = ["Pickles", "Small orange", "Greek yogurt", "Strawberry yogurt", "Blueberry tart"]
sour_and_mild = ["Lemon cheesecake slice", "Bowl of plums", "Cranberry smoothie", "Tamarind pie", "Key lime pie"]
sour_and_heavy = ["Tomato turmeric chicken", "Brown rice with kimchi", "Egg salad drizzled with lime juice", "Vinegar chicken curry", "Lemon and butter fried fish"]
# If statements for each possible combination of inputs that a user can input.
if food_craving == 1 and hunger_level == 1:
    print("The options available for you are: " + str(sweet_and_light))
    print("The food you should eat is: " + random.choice(sweet_and_light))
elif food_craving == 1 and hunger_level == 2:
    print("The options available for you are: " + str(sweet_and_mild))
    print("The food you should eat is: " + random.choice(sweet_and_mild))
elif food_craving == 1 and hunger_level == 3:
    print("The options available for you are: " + str(sweet_and_heavy))
    print("The food you should eat is: " + random.choice(sweet_and_heavy))
elif food_craving == 2 and hunger_level == 1:
    print("The options available for you are: " + str(salty_and_light))
    print("The food you should eat is: " + random.choice(salty_and_light))
elif food_craving == 2 and hunger_level == 2:
    print("The options available for you are: " + str(salty_and_mild))
    print("The food you should eat is: " + random.choice(salty_and_mild))
elif food_craving == 2 and hunger_level == 3:
    print("The options available for you are: " + str(salty_and_heavy))
    print("The food you should eat is: " + random.choice(salty_and_heavy))
elif food_craving == 3 and hunger_level == 1:
    print("The options available for you are: " + str(sour_and_light))
    print("The food you should eat is: " + random.choice(sour_and_light))
elif food_craving == 3 and hunger_level == 2:
    print("The options available for you are: " + str(sour_and_mild))
    print("The food you should eat is: " + random.choice(sour_and_mild))
elif food_craving == 3 and hunger_level == 3:
    print("The options available for you are: " + str(sour_and_heavy))
    print("The food you should eat is: " + random.choice(sour_and_heavy))
else:
    print("You have entered an invalid combination.")

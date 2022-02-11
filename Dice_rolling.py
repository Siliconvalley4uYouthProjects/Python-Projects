#Rolling the dice
import random
roll_dice = input("Roll the dice: ")

if roll_dice == "yes":
   posiblle_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))
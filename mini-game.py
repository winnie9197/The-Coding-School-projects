#Reinforcement for Lesson 4

# 'X' represents a step
# 'o' represents a crap and puke bucket (input())
# 'O' represents a explosive diarrhea (input())
# (Person)XXXXXXXXX o XXXXXXXXX	O O XXXXXXXXX(Exit)

# (Person)XXOOOOOOOOOOOOOOOOOOOOOX(Exit)

# for (each step S): #where S is the next unknown step
# 	if (S == 'X'):
#   	#take one step
#   #any elif statements?
#   elif (S == 'o'):
#   	#jump over it
#   elif (S == 'O'):
#   	#do some action
#   else: 
#   	#IF ANYTHING ELSE, by the rules of this game, print("this isn't in the rules")
import random

class StepsMiniGame():
	def __init__():
		self.launch()
		self.path = self.generatePath()

	def launch():
		#customize obstacles
		customize = input("Would you like to customize the obstacles for this game?")
		if (customize):
			pebble = input("What would you like 'o' to represent?")
			rock = input("What would you like 'O' to represent?")
		else:
			pebble = "pebble"
			rock = "rock"

	def generate_path():
		path_array = []
		path_length = 50
		low = 0
		high = 100
		one_sd = 68
		two_sd = 95

		for index in range(path_length):
			step_int = random.randint(low,high)
			if (step_int <= one_sd):
				path_array.append('X')
			elif (step_int > one_sd and step_int<=two_sd):
				path_array.append('o')
			elif (step_int>=two_sd):
				path_array.append('O')
			else: 
				print("something isn't right")

		path = ''.join(path_array)

		return path

#keydpwn and controls




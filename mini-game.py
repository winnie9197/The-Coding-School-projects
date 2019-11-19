#Reinforcement game for Lesson 4
#Goal: to demonstrate the use of objects, methods, for loops, input() 

# 'X' represents a step
# 'o' represents a _____ (input())
# 'O' represents a _____ (input())
# (Person)XXXXXXXXX o XXXXXXXXX	O O XXXXXXXXX(Exit)
# (Person)XXOOOOOOOOOOOOOOOOOOOOOX(Exit)
# Task: direct the person to exit
# Logic:
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
# Input: 'a' or 'd' indicating L/R
# Dodge the obstacles in time!


import random, signal, getch

class StepsMiniGame():
	def __init__(self):
		self.launch()
		self.path = self.generate_path()
		self.game_start()

	def launch(self):
		#customize obstacles
		print("Would you like to customize the obstacles? [Enter Y/N]")
		customize = getch.getch()
		if (customize == "Y".lower()):
			self.pebble = input("What would you like 'o' to represent?")
			self.rock = input("What would you like 'O' to represent?")
		if (not self.pebble):
			self.pebble = "pebble"
			self.rock = "rock"

	def generate_path(self):
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

	#gets user input
	def game_start(self):
		self.game_start = True
		if (self.path):
			for next_step in self.path:
				print(next_step)

				signal.signal(signal.SIGALRM,self._handle_timeout)
				signal.alarm(2)
				try:
					user_input = getch.getch()
					if (user_input == 'a'):
						if (next_step != 'o' and next_step != 'O'):
							raise ValueError("You've diverted from the right track! You lost!")
					elif (user_input == 'd'):
						if (next_step != 'X'):
							raise ValueError("You hit a %s! You lost!" % (self.pebble if next_step=='o' else self.rock))
					else:
						raise ValueError("Please enter a valid command!")
				except ValueError as e: 
					print(e)
					break
				except Exception:
					print("You're too slow! You lost!")
					break
				
				finally:
					signal.alarm(0)
	
	def _handle_timeout(self, signum, stack):
		raise Exception()


if (__name__ == "__main__"):
	game = StepsMiniGame()







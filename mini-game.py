#Reinforcement for Lesson 4
#Goal: to demonstrate the use of objects, methods, for loops, input() 

# 'X' represents a step
# 'o' represents a _____ (input())
# 'O' represents a _____ (input())
# (Person)XXXXXXXXX o XXXXXXXXX	O O XXXXXXXXX(Exit)
# (Person)XXOOOOOOOOOOOOOOOOOOOOOX(Exit)
# Task: direct the person to exit

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
# import random, keyboard
import random, signal
# import time
# from threading import Thread

class StepsMiniGame():
	def __init__(self):
		self.launch()
		self.path = self.generate_path()
		self.game_start()

	def launch(self):
		#customize obstacles
		customize = input("Would you like to customize the obstacles for this game?")
		if (customize):
			pebble = input("What would you like 'o' to represent?")
			rock = input("What would you like 'O' to represent?")
		else:
			pebble = "pebble"
			rock = "rock"

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


	def game_start(self):
		self.game_start = True
		if (self.path):
			for next_step in self.path:
				print(next_step)
				#timer,		#signal.alarm?
				# self.timeout()
				#on keydown (a,d) [s=dash?]
				# Thread(target = self.keydown).start()
				# user_input = input()
				# user_input = user_input.strip()
				# if (user_input == 'a' and next_step == 'X'):
				# 	print("You've got yourself jammed. You lost the game")
				# 	break
				# if (user_input == 'd' and (next_step == 'o' or next_step == 'O')):
				# 	print("You've stepped on poop!")


				#how to use signall??????
				signal.signal(signal.SIGALRM,self._handle_timeout)
				signal.alarm(2)
				try:
					user_input = input().strip()
					print(user_input)
					if (user_input == 'a'):
						if (next_step != 'o' and next_step != 'O'):
							raise ValueError("You've diverted from the right track! You lost!")
					elif (user_input == 'd'):
						if (next_step != 'X'):
							raise ValueError("You hit an obstacle! You lost!")
					else:
						raise ValueError("Please enter a valid command!")
						# user_input
				except ValueError as e: 
					print(e)
					break
				except Exception:
					# if (user_input != None):
					print("You're too slow! You lost!")
					break
				
				finally:
					signal.alarm(0)
				

	
	def _handle_timeout(self, signum, stack):
		raise Exception()

	def quit_game(self):
		self.game_start = False

		



	# def keydown(self):
	# 	time.sleep(2)
		# key_pressed = self.detect_keydown(next_step) #[keyboard?]
		# if (not key_pressed):
		# 	print("You've lost the game!")


	#filter input, only accept a/d
	# def detect_keydown(self, next_step):
	# 	while True:
	# 		try:
	# 			#duck
	# 			if (keyboard.is_pressed('a')): #and (next_step == 'o' or next_step == 'O')):
	# 				print('pressed a')
	# 			#go
	# 			if (keyboard.is_pressed('d')): #and next_step == 'X'):
	# 				print('pressed d')
	# 		except:
	# 			print("Wrong step!")
	# 			return False
	# 	return True
	# def timeout():


if (__name__ == "__main__"):
	game = StepsMiniGame()


#keydown and controls
#display next obstacle, LR controls, dodge in time




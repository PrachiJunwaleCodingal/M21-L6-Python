#Fruit quiz

import random
class fruitClass:
	def __init__(self):
		self.fruits={'watermelon':'green',
					'banana':'yellow',
                    "grapes":"yellowgreen",
                    "straberry":"pink"
                    }

	def quiz(self):
		while (True):
			fr, col= random.choice(list(self.fruits.items()))
			
			print("What is the color of ",fr)
			user_answer = input()
			
			if(user_answer.lower() == col):
				print("Correct answer")
			else:
				print("Wrong answer")
				
			option = int(input("Write 0 to add new otherwise write 1:"))
			if (option):
				break

print("welcome to fruit quiz ")
obj = fruitClass()
obj.quiz()

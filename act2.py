#Flashcard

class flashcard:
	def __init__(self, wrd, mean):
		self.wrd = wrd
		self.mean = mean
	def __str__(self):
		return self.wrd+ "-"+self.mean
		
flash = []

while(True):
	wrd = input("Write name in flashcard: ")
	mean = input("write its meaning : ")
	
	flash.append(flashcard(wrd, mean))
	option = int(input("Write 0 to add new otherwise write 1: "))
	if(option):
		break
		

print("Your flashcards are:")
for i in flash:
	print("-->", i)

#Make a D&D Character Generator
#Started 6.13.20

from random import randint

#class Stats():
#	'''A class to generate stats'''
#	def __init__(self):
#		self.constitution = str(randint(0,10))
#		self.intellect = str(randint(0,10))
#		self.wisdom = str(randint(0,10))
#		self.strength = str(randint(0,10))
#		self.agility = str(randint(0,10))
#
#		#def generate_stats(self):
#		#	print("constitution : " + self.constitution)

def generate_class():
	"""Generate a class"""
	class_list = ['warrior', 'hunter','mage']
	choice = randint(0,2)
	random_class = class_list[choice]
	print("Race: " + random_class.title())

def generate_race():
	race_list = ['human', 'elf', 'dwarf']
	choice = randint(0,2)
	random_race = race_list[choice]
	print("Class: " + random_race.title())
	

def display_stats():
	stat_list = ['constitution', 'intellect', 'wisdom', 'strength', 'agility']
	
	for stat in stat_list:
		stat_value = str(randint(1,20))
		print(stat.title() + ": " + stat_value) 

#character_0 = Stats()


generate_class()
generate_race()
print("\n")
display_stats()


#idea: make it so you can roll for values and assign them, store information, incorporate classes
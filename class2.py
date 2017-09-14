import os

class Hero(object):
	def __init__(self, name = "Incognito"):
		#set up object to remember its name
		self.name = name
		self.health = 10
		self.power = 5
	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage

class Goblin(object):
	def __init__(self):
		self.name = "Goblin"
		self.health = 6
		self.power = 2
	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage

##the_hero is the object and Hero() is the class
the_hero = Hero() ##instantiate a hero object from class hero
a_goblin = Goblin()

while a_goblin.health > 0 and the_hero.health > 0:
	os.system("clear")
	print "You have %d health and %d power" % (the_hero.health, the_hero.power)
	print "The goblin has %d health and %d power." % (a_goblin.health, a_goblin.power)
	print "What do you want to do?"
	print "1. Fight the goblin"
	print "2. Do nothing"
	print "3. flee"
	print "> ",
	user_input = raw_input()
	if user_input == "1":
		a_goblin.take_damage(the_hero.power)
	elif user_input == "2":
		pass
	elif user_input == "3":
		print "Goodbye"
	else:
		print "Invalid input %d" % user_input

	if a_goblin.health > 0:
		the_hero.take_damage(a_goblin.power)

		print "The goblin hits you for %d damage" % a_goblin.power

	if the_hero.health <= 0:
		print "You have been killed by the goblin"
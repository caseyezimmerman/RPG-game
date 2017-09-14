import os
from random import randint
##3rd part pygame imports


##custom modules (ones that I made)

from Joker import Joker #vampire
from Bane import Bane #goblin
from Batman import Batman #hero


batman = Batman() ##instantiate a hero object from class hero
bane = Bane()
joker = Joker()

monsters = []
##before the game starts ask the hero for his name
print "What is your name?"
batman.name = raw_input("> ")
batman.cheer_for_hero()

print "How many villans are you willing to fight, %s?" % batman.name
number_of_enemies = int(raw_input("> "))

for i in range(0, number_of_enemies):
	rand_num = randint(0,1)
	if (rand_num == 1):
		monsters.append(Bane())
	if (rand_num == 0):
		monsters.append(Joker())


print monsters

##we need to loop through all the monsters
for monster in monsters:
##once you loop with monster must change all a_goblin to monster
	while monster.is_alive() and batman.is_alive():  ##.is_alive comes from is_alive method in goblin class
		os.system('clear')
		print "You have %d health and %d power." % (batman.health, batman.power) 
		print "The villan has %d health and %d power." % (monster.health, monster.power)
		print "What do you want to do?"
		print "1. fight %s" % monster.name
		print "2. do nothing"
		print "3. flee"
		print "> ",
		user_input = raw_input()
		if user_input == "1":
		#user has chosen to attack
		#take away health from the goblin based on hero power
			#a_goblin.health -= the_hero.power
			#THE GOBLIN CLASS SHOULD BE MANAGING THE GOBLINS HEALTH
			#THE HERO IS GOING TO DO THE_HERO.POWER DAMAGE TO THE GOBLIN
			monster.take_damage(batman.power)
		elif user_input == "2":
			#hero stads there and does nothing
			pass
		elif user_input == "3":
			print "Goodbye, coward"
			#call break to end the while loop
			break
		else:
			print "Invalid input %s" % user_input	#
		##goblins turn to attack (only if hes still alive)
		if monster.is_alive():
			##THE HERO SHOULD MANAGE ITS OWN HEALTH, JUST LIKE GOBLIN
			##CALL TAKE DAMAGE TO THE HERO
			#the_hero.health -= a_goblin.power
			batman.take_damage(monster.power)	#
			print "The monster hits you for %d damage" % monster.power
			#goblin has attacked, check to see if hero is still alive
			if batman.health <= 0:
				print "You have been killed by %s" % monster.name#


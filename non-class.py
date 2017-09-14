##this is a rocedural aproach to a text based rpg game
##the hero is going to fight the goblin
##the hero will have the option to:
##1. fight the goblin
##2. do nothing (goblin will still attack hero)
##3. run away
import os

hero_health = 10
hero_power = 10
goblin_health = 6
goblin_power = 2

##run the game as long as both characters have healhs
while goblin_health > 0 and hero_health > 0:
	os.system('clear')
	print "You have %d health and %d power." % (hero_health, hero_power) 
	print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
	print "What do you want to do?"
	print "1. fight goblin"
	print "2. do nothing"
	print "3. flee"
	print "> ",
	user_input = raw_input()
    if user_input = "1":
    #user has chosen to attack
    #take away health from the goblin based on hero power
    	goblin_health -= hero_power
    elif user_input == "2":
		#hero stads there and does nothing
		pass
	elif user_input = "3":
		print "Goodbye, coward"
		#call break to end the while loop
		break
	else:
		print "Invalid input %s" % user_input

	##goblins turn to attack (only if hes still alive)
	if goblin_health > 0:
		hero_health -= goblin_power
		print "The goblin hits you for %d damage" % goblin_power
		#goblin has attacked, check to see if hero is still alive
		if hero_health <= 0:
			print "You have been killed by the goblin"
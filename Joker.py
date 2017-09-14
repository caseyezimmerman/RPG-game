##get the super parent class

from Character import Character

##make goblin subclass of character
class Joker(Character):
	def __init__(self):  ##once you make this a subclass all the variables below are in the super character class
		super(Joker, self). __init__('Joker', 6, 2) ##hard coding name to always be goblin, health = 6 and power = 2
#		self.name = "Goblin"
#		self.health = 6
#		self.power = 2
#	def take_damage(self, amount_of_damage):
#		self.health -= amount_of_damage
#	def get_health(self):
#		return self.health
#	def is_alive(self):
#		return self.health > 0
	def do_a_dance(self):
		print "Goblin has done dance, you are mesmerized but not hurt"
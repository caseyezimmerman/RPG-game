##get the super class
from Character import Character

class Bane(Character):
	def __init__(self):
		super(Bane,self). __init__('Bane', 15, 4)
		#self.name = "Vampire"
#		self.health = 15
#		self.power = 4
#	def take_damage(self, amount_of_damage):
#		self.health -= amount_of_damage
#	def get_health(self):
#		return self.health
#	def is_alive(self):
#		return self.health > 0
	def make_girls_swoon(self):
		print "The vampire makes girls swoon"
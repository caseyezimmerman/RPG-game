from Character import Character

class Batman(Character):
	def __init__(self):
		super(Batman, self). __init__('Batman', 6, 2)

		#set up object to remember its name
		#self.name = name
#		self.health = 10
#		self.power = 5
#	def take_damage(self, amount_of_damage):
#		self.health -= amount_of_damage
	def cheer_for_hero(self):
		print "Fight hard %s" % self.name
#	def is_alive(self):
#		return self.health > 0
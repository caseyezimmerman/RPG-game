##Basics
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []   ##must be a list to append
        self.greeting_count = 0

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
        print self.greeting_count
    
    ##add a method 2 that prints out contact info of desired person
    def print_contact_info(self):
    	print 'My contact info is %s' % self.email, self.phone

    def newfriends(self, new_friends):
    	self.friends.append(new_friends.name)

    def num_friends(self):
    	print len(self.friends)

    def __repr__(self):
    	print '%s, %s, %s' % (self.name, self.email, self.phone)

    	
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)  ##sonny is self.name so it comes second. 
jordan.greet(sonny)  ##jordan is self.name so it comes second.

sonny.print_contact_info()
jordan.print_contact_info()

sonny.newfriends(jordan)
jordan.newfriends(sonny)
#len(person1.friends)

print sonny.friends
print jordan.friends

#print len(person1.friends)
sonny.num_friends()
jordan.num_friends()







##Make your own class
class Vehicle(object):
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	##add a method that prints info
	def print_info(self):
		print self.year, self.make, self.model#
car = Vehicle('Nissan', 'Leaf', 2015)
car.print_info()

      


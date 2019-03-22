# import Animal from Animal

class Animal:
	def __init__(self,name,age,height,weight,color):
		self.age = age
		self.name = name
		self.height = height
		self.weight = weight
		self.color = color

	def __str__(self):
		return "animal:" + str(self.name) + ":" + str(self.age)

	def speak(self):
		return "***ROAR***"

class Person(Animal):
	def __init__(self,name,age,height,weight,color,job,school,university):
		Animal.__init__(self,name,age,height,weight,color)
		self.job = job
		self.school = school
		self.university = university
		self.friends = []

	def speak(self):
		return "***Hello***"

	def get_friends(self):
		return self.friends

	def add_friend(self,fname):
		if fname not in self.friends:
			self.friends.append(fname)

	def age_diff(self,other):

		diff = self.age - other.age
		print(abs(diff), "year difference")


nikhil = Person('nikhil',24,6,80,"brown","engineer","vps","vtu")
vishak = Person('vishak',35,6,80,"brown","engineer","vps","vtu")


print(nikhil.get_friends())
print(Person.speak())
# nikhil.add_friend('vishak')
# print(nikhil.get_friends())
# nikhil.add_friend('vineeth')
# print(nikhil.get_friends())

# nikhil.age_diff(vishak)

# print(nikhil.get_friends()[0])
# print(nikhil.get_friends()[0][0])
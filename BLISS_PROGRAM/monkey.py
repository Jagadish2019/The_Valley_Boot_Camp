from Animal1 import Animal1

class monkey(Animal1):

	def __init__(self,name):
		Animal1.__init__(self,age)
		self.name = name
		# self.tricks = tricks
	def tricks(self):
		return "dance"
from monkey import monkey

class person1(monkey):
	def __init__(self,age,name,language):
		monkey.__init__(self,age,name)
		self.language = language



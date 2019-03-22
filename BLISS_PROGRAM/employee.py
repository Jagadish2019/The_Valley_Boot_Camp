from student import student

class employee(student):
	def __init__(self,age,name,tricks,language,subject,company):
		student.__init(self,age,name,language,subject)
		self.company = company

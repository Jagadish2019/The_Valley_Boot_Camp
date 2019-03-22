
from person1 import person1

class student(person1):
	def __init__(self,name,age,language,subject):
		person1.__init__(age,name,language)
		self.subject = subject

	def __str__(self):

		return f"Hello my name is {self.name} and I'm a student who is {self.age} years old and my langauge is {self.language} and my subject is {self.subject}"

student = student('student',25,'english','mathematics')
print(student)



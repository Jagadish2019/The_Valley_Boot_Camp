
class Square:

	def __init__(self,p1,p2,p3,p4):

		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.p4 = p4

	def area(self):

		side = self.p1.distance(self.p2)
		return side**2

sq = Square(a,b,c,d)

print(sq.area())
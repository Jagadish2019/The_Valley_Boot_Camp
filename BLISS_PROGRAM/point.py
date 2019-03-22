lass point:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def distance(self,other):
		xsq = (self.x - other.x) **2
		ysq = (self.y - other.y) **2
		return (xsq + ysq) **0.5



a = point(0,0)
b = point(0,1)
c = point(1,1)
d = point(1,0)

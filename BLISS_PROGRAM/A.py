# class point:

# 	def __init__(self,x,y):
# 		self.x = x
# 		self.y = y

# 	def __add__(other,self):
# 		return point(self.x + other.x, self.y + other.y)

# 	# def __str__(self):
# 	# 	return f'[{self.x},{self.y}]'

# 	def __str__(self):
# 		print(self.x)
# 		print(self.y)
# 		return f'{self.x},{self.y}'

# 	def distance(self,other):
# 		xsq = (self.x - other.x) **2
# 		ysq = (self.y - other.y) **2
# 		return (xsq + ysq)** 0.5

# 	# def 
# x = point(1,1)
# y = point(2,3)

# print(x)

# print(x.distance(y))


class point:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __add__(other,self):
		return point(self.x + other.x, self.y + other.y)

	# def __str__(self):
	# 	return f'[{self.x},{self.y}]'

	# def __str__(self):
	# 	print(self.x)
	# 	print(self.y)
	# 	return f'{self.x},{self.y}'

	def distance(self,other):
		xsq = {self.x - other.y}**2
		ysq = {self.y - other.y}**2
		return (xsq + ysq)**0.5

	# def 
x = point(1,1)
y = point(2,3)


print(x.distance(y))


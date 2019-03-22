
# area of circle

#def circle_area(r):

#	pi = 22/7
#	area = pi*(r**2)
#	return print(area)

#circle_area(2)



# 2pi r h and 2 pi r ** 2


def aoc(r,h):

	pi = 22/7
	area = pi*(r**2) + (2*pi*(r**2))
	return area

def main():
	r=int(input("enter r value:\t"))
	h=int(input("enter h value:\t"))
	return(aoc(r,h))

print(main())


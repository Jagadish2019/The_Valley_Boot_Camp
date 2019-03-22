

#import math

#print(math.sqrt(9))

#x1 = int(input("enter x1 value:\t"))
#x2 = int(input("enter x2 value:\t"))

#y1 = int(input("enter y1 value:\t"))
#y2 = int(input("enter y2 value:\t"))

#a = math.sqrt((x2-x1)**2 + (y2-y1)**2)

#print(a)





import math

#print(math.sqrt(9))



def calc(x1,x2,y1,y2):
	a= math.sqrt((x2-x1)**2 + (y2-y1)**2)

	return(print(a))

def main():
	x1 = int(input("enter x1 value:\t"))
	x2 = int(input("enter x2 value:\t"))

	y1 = int(input("enter y1 value:\t"))
	y2 = int(input("enter y2 value:\t"))
	
	return calc(x1,x2,y1,y2)


main()




def fib(n):
	if (n == 0) or (n == 1):
		return 1
	else:
		return fib(n-0) + fib(n-1)

a = int(input("enter a number:\t"))

print(fib(a))

















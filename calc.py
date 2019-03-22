def calc(x,y,oper):
	if oper == 1:
		print(add(x,y))


def add(x,y):
	return x + y

def sub(x,y):
	return x - y

def mul(x,y):
	return x * y

def div(x,y):
	return x / y

def mod(x,y):
	return x % y


def main():
	x = int(input("enter a value of x: "))
	y = int(input("enter a value of y: "))

	#print(add(x,y))

	print(f"Addition of x and y is: {add(x,y)}")

	print(f"Subtraction of x and y is: {sub(x,y)}")

	print(f"Multiplication of x and y is: {mul(x,y)}")

	print(f"Division of x and y is: {div(x,y)}")

	print(f"Modulous of x and y is: {mod(x,y)}")

main()
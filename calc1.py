def calc(x,y,oper):
	if oper == 1:
		print(add(x,y))

	if oper == 2:
		print(sub(x,y))

	if oper == 3:
		print(mul(x,y))

	if oper == 4:
		print(div(x,y))

	if oper == 5:
		print(mod(x,y))

def add(x,y):
	return x + y

def sub(x,y):
	return x - y

def mul(x,y):
	return x * y

def div(x,y):
	try:
		return x / y
	except ZeroDivisionError:
		return 'Division by Zero'
	#if x > 0 and y > 0:
	#	return x / y
	#return "Improper values entered"


def mod(x,y):
	if x > 0 and y > 0:
		return x % y
	return "Improper vaues entered"

def main():
	#x = int(input("enter a value of x: "))
	#if x >= 0:
	while True:
		try:
			x = int(input("Please enter x value: "))
			break
		except ValueError:
		    print("Oops!  That was no valid number.  Try again...")

	while True:
		try:
			y = int(input("Please enter y value: "))
			break
		except ValueError:
		    print("Oops!  That was no valid number.  Try again...")

	#y = int(input("enter a value of y: "))
	
	oper = int(input("enter 1 for addition, 2 for Sub, 3 for Multi, 4 for Div, 5 for Mod: "))
	calc(x,y,oper)


	#print(add(x,y))

	#print(f"Addition of x and y is: {add(x,y)}")

	#print(f"Subtraction of x and y is: {sub(x,y)}")

	#print(f"Multiplication of x and y is: {mul(x,y)}")

	#print(f"Division of x and y is: {div(x,y)}")

	#print(f"Modulous of x and y is: {mod(x,y)}")

main()
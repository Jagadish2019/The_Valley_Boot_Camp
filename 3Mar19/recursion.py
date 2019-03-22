def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)

def main():
	n = int(input("Enter a number:\t"))
	print(fact(n))

main()
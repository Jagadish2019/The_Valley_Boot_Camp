def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

a = int(input("enter a number:\t"))

print(fib(a))






def fib_efficient(n,d):
	if n in d:
		retutn d[n]
	else:
		ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
		d[n] = ans
		return ans

d = {1:1,2:1}
a = int(input("enter a number\n"))
print(fib_efficient(a,d))



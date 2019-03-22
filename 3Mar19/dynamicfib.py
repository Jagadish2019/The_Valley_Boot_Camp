def fib_efficient(n,d):
	if n in d:
		return d[n]
	else:
		ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
		d[n] = ans
		return ans

d = {1:1,2:1}
a = int(input("enter a number\t"))
print(fib_efficient(a,d))



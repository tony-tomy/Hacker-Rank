"""
Fibonacci Series Gnarator...
"""
if __name__ == '__main__':
	n = int(input())
	assert n > 0 , "Enter a positive integer."
	fib = [1]

	while(len(fib) < n):
		if len(fib) == 1:
			fib.append(1)
		else:
			fib.append(fib[-1]+fib[-2])

	print(*fib)





"""
if __name__ == '__main__':
	n = int(input())
	fib = []
	if n > 0:
		fib.append(0)
	if n > 1:
		fib.append(1)
	if n > 2 :
		fib.append(1)
	if n > 3:
		for i in range(3,n):
			fib.append(fib[i-2]+fib[i-1])
	print(*fib)

"""
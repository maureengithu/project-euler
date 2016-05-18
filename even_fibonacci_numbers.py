def fibonacci(x):
	a, b = 1, 1
	total = 0
	while a < x:
		if a % 2 == 0:
			total += a
		a, b = b, a + b
	return total
print fibonacci(4000000)

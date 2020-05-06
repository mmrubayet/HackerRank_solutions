def is_prime(n):
	square_root = int(n**0.5)
	for i in range(2, square_root + 1):
		 if n % i is 0:
			return False
	return True

t = int(input())
for _ in range(t):
	n = int(input())
	if n >= 2 and is_prime(n):
		print("Prime")
	else:
		print("Not prime")

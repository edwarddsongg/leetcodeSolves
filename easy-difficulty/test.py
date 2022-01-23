n = 2

def primeCalc(n):
	if(n%2==0 & n!=2):
		return True
	
	for i in range(2, abs(n)):
		if n%i == 0 & n!=i:
			return True
	
	return False

print(primeCalc(2))


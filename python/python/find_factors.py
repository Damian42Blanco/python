#save as find_factors.py

def factors(b):

	for i in range(1, b+1):
		if b % i == 0:
			print(i)
				
if _name_ == '_main_':

	b = input('Your Number Please: ')
	b = float(b)
	   
	if b > 0 and b.is_integer():
		factors(int(b))
	else:
		print('Please enter a positive integer')

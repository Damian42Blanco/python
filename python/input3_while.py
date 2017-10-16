# save file as input3.py
print("INPUT THREE NUMBERS")
A = float(input("\t A : "))
B = float(input("\t B : "))
C = float(input("\t C : "))
x = -5
while True:
	y = A*(x*x) + B*x + C
	print (x,y)
	x = x + 1
	if(x > 5):
		break

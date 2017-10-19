from random import randint
def randlist(r,usedlist,done):
	alpha = ["a","b","c","d","e","f"]
	usedlist[r] = 1
	c = alpha[r]
	sum = 0
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
		
	
	return c, usedlist
	
def main():
	used = [0,0,0,0,0,0]
	done = False
	while True:
		r = randint(0,5)#make a random number
		c = randlist(r,used,done)	
		#print (used)
		#print(c,end="")
main()

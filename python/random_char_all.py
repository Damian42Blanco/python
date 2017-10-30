from random import randint
def randlist (r,usedlist,done):
	alpha = ["A","a","B","b","C","c","D","d","E","e",
			"F","f","G","g","H","h","I","i","J","j",
			"K","k","L","l","M","m","N","n","O","o", 
			"P","p","Q","q","R","r","S","s","T","t",
			"U","u","V","v","W","w","X","x","Y","y",
			"Z","z","1","2","3","4","5","6","7","8",
			"9","0","'","[","]",";",",",".","/","~",
			"!","@","#","$","%","^","&","*","(",")",
			"+","{","}","|",":","<",">","?","\\","`",
			"_","=","-"]
	c = alpha[r]
	print (c)
	usedlist[r] = 1
	sum = 0
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
		if sum == 92:
			done = True
	return c,usedlist,done
	
def main():
	used = [0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0]
	done = False
	while done == False:
		r = randint(0,92)
		if used[r] == 0:
			c,used,done = randlist(r,used,done)
			#print(r,c,used,done)
			#print(c,end='')
main()

import random
import math
s = random.randint(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
x = random.randint(1,6)
y = ((2*x)/3)**3
y = math.floor(y)
o = s*y
print(s)
print(y)
print(o)
p = []
q = []
p.append(o)
def switch():	
	for n in p:		
		if n in q:
			n = o - 1 
			#? if seed repeats, -1...+2...-3.../-2x...
		else:
			q.append(n)	
print(p, q)

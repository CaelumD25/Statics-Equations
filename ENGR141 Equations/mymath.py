import math

def findMag(vector):
	return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

def findUnit(vector):
	unit = []
	mag = findMag(vector)
	if mag == 0:
		return [0,0,0] 
	for a,b in enumerate(vector):
		unit.append(b/mag)
	return unit

def dotProduct(vector1,vector2):
	dot = 0
	for a,b in zip(vector1,vector2):
		dot += a*b
	return dot


# Project vector1 onto vector2
def vectorDotProduct(vector1, vector2):
	unit = findUnit(vector2)
	dp = dotProduct(vector1,unit)
	vectordp = []
	for x in unit:
		vectordp.append(dp*x)
	return vectordp

def angleBetween(vector1, vector2):
	mag1 = findMag(vector1)
	mag2 = findMag(vector2)
	if mag1 == 0 or mag2 == 0:
		return 0
	return math.degrees(math.acos(dotProduct(vector1,vector2)/(mag1*mag2)))


def crossProduct(a,b):
	i = (a[1]*b[2]-a[2]*b[1])
	j = -(a[0]*b[2]-a[2]*b[0])
	k = (a[0]*b[1]-a[1]*b[0])
	return [i,j,k] 


def pV(vector):
	direction = ["i + ","j + ","k "]
	s = []
	for x,b in zip(vector,direction):
		x = format(x, '.4f')
		s.append(x+b)
	return "".join(s)


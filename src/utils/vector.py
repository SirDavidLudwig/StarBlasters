import math

def add_vecs(v1, v2):
	return tuple(i+j for i, j in zip(v1, v2))

def scale_vec(s, v):
	return tuple(s*i for i in v)

def magnitude(v):
	return math.sqrt(sum((i**2 for i in v)))

def unit_vec(v):
	return scale_vec(1/magnitude(v), v)

def normalize(v):
	try:
		return unit_vec(v)
	except ZeroDivisionError:
		return (0.0, 0.0)

def normal(v):
	return (-v[1], v[0])

def dot_product(v1, v2):
	return sum((i*j for i,j in zip(v1, v2)))

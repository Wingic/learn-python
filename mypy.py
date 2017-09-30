import math
import copy
import turtle

class Point:

	def __str__(self):
		return '%.2f, %.2f' % (self.x, self.y)

	def __add__(self, other):
		temp_p = Point()
		temp_p.x = self.x + other.x
		temp_p.y = self.y + other.y
		return temp_p

	def __radd__(self, other):
		return self.__add__(other)

	"""
	Represents a point in 2-D space.
	"""



p1 = Point()
p2 = Point()

p1.x=3.0
p1.y=4.0

p2.x=150.0
p2.y=24.9

def distance_between_points(p1, p2):
	distance = abs(math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2))
	print(distance)
	return distance


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """
box = Rectangle()
box.width = 60.0
box.height = 20.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
	p = Point()
	p.x = rect.corner.x + rect.width/2
	p.y = rect.corner.y + rect.height/2
	return p

def move_retangle(rect, dx, dy):
	rect.corner.x += dx
	rect.corner.y += dy

class Circle():
	"""Represents a circle. 

    attributes: center, radius.
    """

c1 = Circle()

c1.center = Point()
c1.center.x = 150.0
c1.center.y = 100.0
c1.radius = 75.0

def point_in_circle(C, P):
	if distance_between_points(C.center, P) <= C.radius:
		return True
	else:
		return False


#def rect_in_circle(C, R):


#Bob = turtle.Turtle()

def draw_rect(T, R):
	for i in range(2):
		print(i, R.height, R.width)
		T.fd(R.height)
		T.lt(90)
		T.fd(R.width)
		T.lt(90)
	turtle.mainloop()

#draw_rect(Bob, box)

#def draw_circle(T,C):




def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindroe(word):

	if word == word[::-1] :
		return True
	else:
		return False

"""
	tempstr= word

	while tempstr != '':
		if first(tempstr) == last(tempstr):
			tempstr = middle(tempstr)
		else:
			return False

	return True """
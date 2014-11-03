#Geometry
import math
import random


class Point:
	@staticmethod
	def generate_points(number_points, x_min, x_max, y_min, y_max):
		return [Point(random.uniform(x_min, x_max), random.uniform(y_min, y_max)) for x in range(number_points)]

	@staticmethod
	def calculate_polar_angle(base, comp):
		if base == comp:
			return -1
		if base.x == comp.x:
			return math.pi/2 if base.y < comp.y else 3*math.pi/2
		return math.atan((comp.y - base.y)/(1.0 * (comp.x - base.x)))

	def __str__(self):
		return "Point(%s, %s)"%(self.x, self.y)

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def tup(self):
		return (self.x, self.y)

	def __lt__(self, other):
		return self.x < other.x if self.y == other.y else self.y < other.y

	def __gt__(self, other):
		return not self.__lt__(other)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y



class Segment:

	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __str__ (self):
		return "Segment: "+ str(self.start) +" "+ str(self.end)


if __name__ == '__main__':

	point_list = Point.generate_points(100, 0, 1000, 50, 800)
	test_segment = Segment(point_list[0], point_list[1])
	#print str(test_segment)

	assert len(point_list) == 100
	assert point_list[0].__class__.__name__=='Point'

	point1 = Point(1,2)
	point2 = Point(5,6)
	
	assert point1 < point2
	assert point2 > point1

	point1 = Point(1,2)
	point2 = Point(5,2)

	assert point1 < point2
	assert point2 > point1

	point_list2 = [Point(3,5), Point(2,3), Point(3,1), Point(4,5)]

	point_list2.sort()

	#[lambda x: (print str(x)) for x in point_list2]

	assert Point.calculate_polar_angle(Point(2, 2), Point(4, 5)) == math.atan(1.5)

	assert (Point(1,1) == Point(1,1)) == True






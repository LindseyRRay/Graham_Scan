#Geometry
import random


class Point:
	@staticmethod
	def generate_points(number_points, x_min, x_max, y_min, y_max):
		return [Point(random.uniform(x_min, x_max), random.uniform(y_min, y_max)) for x in range(number_points)]

	def __str__(self):
		return "Point(%s, %s)"%(self.x, self.y)

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def tup(self):
		return (self.x, self.y)

class Segment:

	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __str__ (self):
		return "Segment: "+ str(self.start) +" "+ str(self.end)


if __name__ == '__main__':

	point_list = Point.generate_points(100, 0, 1000, 50, 800)
	test_segment = Segment(point_list[0], point_list[1])
	print(str(test_segment))

	assert len(point_list) == 100
	assert point_list[0].__class__.__name__=='Point'




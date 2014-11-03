#test_algorthm
import unittest
from algorithm import Algorithm
from geometry import Point


class test_algorithm(unittest.TestCase):

	def test_min_point(self):
		point_array = [Point(10, 5), Point(3, 2), Point(5, 5), Point(6, 10)]
		algo = Algorithm(point_array)
		
		self.assertEqual(str(algo.min_point()), str(Point(3, 2)))
	
	def test_polar_angle(self):
		point_array = [Point(1, 1), Point(2, 2), Point(2, 3), Point(2, 1)]
		algo = Algorithm(point_array)
		polar_list = algo.polar_angle_sort(Point(1,1))


		self.assertEqual(str(polar_list[0]), str(Point(1, 1)))
		self.assertEqual(str(polar_list[1]), str(Point(2, 1)))
		self.assertEqual(str(polar_list[-1]), str(Point(2, 3)))

if __name__ == '__main__':
	unittest.main()

#test_algorthm
import unittest
from algorithm import Algorithm
from geometry import Point, Segment
import pdb


class test_algorithm(unittest.TestCase):

	def test_min_point(self):
		point_array = [Point(10, 5), Point(3, 2), Point(5, 5), Point(6, 10)]
		algo = Algorithm(point_array)
		p = algo.min_point()
	
		self.assertEqual(str(p), str(Point(3, 2)))
	
	def test_polar_angle(self):
		point_array = [Point(1, 1), Point(2, 2), Point(2, 3), Point(2, 1)]
		algo = Algorithm(point_array)
		polar_list = algo.polar_angle_sort(Point(1,1))


		self.assertEqual(str(polar_list[0]), str(Point(1, 1)))
		self.assertEqual(str(polar_list[1]), str(Point(2, 1)))
		self.assertEqual(str(polar_list[-1]), str(Point(2, 3)))

		point_array = [Point(1, 1), Point(0, 2), Point(2, 3), Point(2, 1)]
		algo = Algorithm(point_array)
		polar_list = algo.polar_angle_sort(Point(1,1))

		self.assertEqual(str(polar_list[-1]), str(Point(0,2)))


	def test_output_polar(self):

		point_array = [
			Point(19.2486849886, 42.0138353124), 
			Point(34.6545353825, 5.95845608147), 
			Point(66.6014654767, 66.0841191785), 
			Point(49.1321252346, 86.6154463314)
		]
		algo = Algorithm(point_array)
		polar_list = algo.polar_angle_sort(Point(34.6545353825, 5.95845608147))

		self.assertEqual(str(polar_list[0]), str(Point(34.6545353825, 5.95845608147)))

	def test_segments(self):
		point_array = [
			Point(19, 42), 
			Point(34, 5), 
			Point(66, 66), 
			Point(49, 86)
		]
		algo = Algorithm(point_array)
		algo.stack = point_array
		seg_list = algo.segments()

		self.assertEqual(str(seg_list[0]), str(Segment(Point(19, 42), Point(34, 5))))


	def test_nonunique_angles(self):
		point_array = [
		Point(2, 4), 
		Point(3, 10), 
		Point(2, 5), 
		Point(0, 0),
		Point(3, 6)
	]
		algo = Algorithm(point_array)
		algo.sort_point_array()
		list_nondups = algo.find_duplicate_angles()

		for n in list_nondups:
			print str(n)

		self.assertEqual(str(algo.minimum_point), str(Point(0, 0)))

if __name__ == '__main__':
	unittest.main()

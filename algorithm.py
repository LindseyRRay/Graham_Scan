#Algorithm
from state_manager import StateManager, State
from geometry import Point, Segment
import sys
import copy
from operator import itemgetter
from collections import Counter, defaultdict

class Algorithm:
	
	def __init__(self, point_array):
		self.point_array = point_array
		self.stack = list()
		self.state_manager = StateManager()
		self.index = 0
		self.minimum_point = self.min_point()

	def increment_state(self):
		self.state_manager.increment_state()

	def segments(self):
		if not self.stack:
			return [] 
		tuple_list = zip(self.stack, self.stack[1:])
		segment_list = map(lambda x: Segment(x[0], x[1]), tuple_list)
		return segment_list

	def min_point(self):
		#return leftmost min point by y coord
		min_point = Point(sys.maxsize, sys.maxsize)
		for i in self.point_array:
			if i < min_point:
				min_point=i
		return min_point

	def polar_angle_sort(self, min_point):
		sort_list = copy.deepcopy(self.point_array)
		sort_list.remove(min_point)
		sort_list.sort(key = lambda point: Point.calculate_polar_angle(min_point, point))
		sort_list.insert(0, min_point)
		return sort_list

	def sort_point_array(self):
		self.point_array = self.polar_angle_sort(self.min_point())

	def find_duplicate_angles(self):
		'''Find points with the same polar angle'''
		counter = Counter([Point.calculate_polar_angle(self.minimum_point, x) for x in self.point_array if x != self.minimum_point])
		non_uniques = [angle for angle, count in counter.items() if count > 1]
		non_unique_points = [(Point.calculate_polar_angle(self.minimum_point, p), p, Point.euclidian_distance(self.minimum_point, p)) for p in self.point_array if Point.calculate_polar_angle(self.minimum_point, p) in non_uniques]
		sorted_non_uniques = sorted(non_unique_points, key = itemgetter(1,2))
		return sorted_non_uniques

	def remove_closest_duplicate(self):
		'''Among points with the same polar angle, calculate euclidean distance'''
		duplicates = self.find_duplicate_angles()
		remove_points = list()
		'''for tuples with same subset, return only longest'''
		d = defaultdict(list)
		for angle, point, dist in duplicates:
			d[angle].append(point)
#NEED TO FIX THIS ERROR
#WIP
		print(type(d))
		for key, items in d.items():
			print(items)
			#remove_points.extend(items[:-1])
		return remove_points

	def init_stack(self):
		self.stack = list()
		self.stack.append(self.point_array[0])
		self.stack.append(self.point_array[1])
		self.stack.append(self.point_array[2])
		self.index = 2
#pseudo code

#	def select_point(self):
#		self.index += 1
#		for self.index in xrange(3, len(point_array)):
#			while angle(self.stack[-2], self.stack[-1], next_point) > nonleftturn:
#				pop(self.stack[-1])
#			push(next_point onto stack)
#		return stack 



	def next_step(self):
		if self.state_manager.current_state == State.not_run:
			self.increment_state()

		elif self.state_manager.current_state == State.initial_point:
			self.sort_point_array()
			self.increment_state()

		elif self.state_manager.current_state == State.init_stack:
			self.init_stack()
			self.increment_state()

		elif self.state_manager.current_state == State.select_point:
			self.select_point()
			self.increment_state()
 
					

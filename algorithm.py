#Algorithm
from state_manager import StateManager, State
from geometry import Point, Segment
import sys
import copy
from operator import itemgetter
from itertools import groupby


class Algorithm:
	
	def __init__(self, point_array):
		
		self.point_array = point_array
		self.stack = list()
		self.state_manager = StateManager()
		self.index = 0
		self.minimum_point = self.min_point()

	def increment_state(self, is_right_turn = False, out_of_points = False):
		self.state_manager.increment_state(is_right_turn = is_right_turn, out_of_points = out_of_points)

	def segments(self):
		if not self.stack:
			return [] 
		tuple_list = zip(self.stack, self.stack[1:])
		segment_list = map(lambda x: Segment(x[0], x[1]), tuple_list)
		if self.state_manager.current_state == State.complete:
			segment_list.append(Segment(self.stack[-1], self.stack[0]))
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


	def init_stack(self):
		self.stack = list()
		self.stack.append(self.point_array[0])
		self.stack.append(self.point_array[1])
		self.stack.append(self.point_array[2])
		self.index = 2

	def is_checking_point(self):
		return self.state_manager.current_state == State.check_angle

	def cross_product(self, v1, v2):
		return (v1.x * v2.y - v1.y * v2.x)

	def is_nonleft_turn(self, p1, p2, p3):
		v1 = Point((p1.x - p2.x), (p1.y - p2.y))
		v2 = Point((p3.x - p2.x), (p3.y - p2.y))
		determinant = self.cross_product(v1, v2)

		return True if determinant > 0 else False 

	def select_point(self):
		self.index += 1

	def check_angle(self):
		return self.is_nonleft_turn(self.stack[-2], self.stack[-1], self.point_array[self.index])

	def pop(self):
		self.stack.pop()

	def is_out_of_points(self):
		return self.index >= len(self.point_array) - 1

	def push(self):
		self.stack.append(self.point_array[self.index])

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

		elif self.state_manager.current_state == State.check_angle:
			self.increment_state(is_right_turn = self.check_angle())

		elif self.state_manager.current_state == State.pop:
			self.pop()
			self.increment_state()

		elif self.state_manager.current_state == State.push:
			self.push()
			self.increment_state(out_of_points = self.is_out_of_points())

		elif self.state_manager.current_state == State.complete:
			pass




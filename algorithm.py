#Algorithm
from state_manager import StateManager, State
from geometry import Point
import sys
import copy

class Algorithm:
	
	def __init__(self, point_array):
		self.point_array = point_array
		self.stack = list()
		self.state_manager = StateManager()



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


	def next_step(self):
		if self.state_manager.current_state == State.not_run:
			self.increment_state()

		elif self.state_manager.current_state == State.initial_point:
			self.sort_point_array()
			self.increment_state()

	def increment_state(self):
		self.state_manager.increment_state()

					

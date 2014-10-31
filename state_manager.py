#state manager
from enum import Enum

class State(Enum):
	not_run = 0
	initial_point = 1
	polar_angle = 2
	init_stack = 3
	select_point = 4
	check_angle = 5
	pop = 6
	push = 7
	complete = 8


class StateManager:
	def __init__(self):
		self.current_state = State.not_run
		
	def increment_state(self, is_right_turn=False, out_of_points=False):
		if self.current_state == State.not_run:
			self.current_state = State.initial_point

		elif self.current_state == State.initial_point:
			self.current_state = State.polar_angle

		elif self.current_state == State.polar_angle:
			self.current_state = State.init_stack

		elif self.current_state == State.init_stack:
			self.current_state = State.select_point

		elif self.current_state == State.select_point:
			self.current_state = State.check_angle

		elif self.current_state == State.check_angle and is_right_turn:
			self.current_state = State.pop

		elif self.current_state == State.check_angle and not is_right_turn:
			self.current_state = State.push

		elif self.current_state == State.pop:
			self.current_state = State.check_angle

		elif self.current_state == State.push and out_of_points:
			self.current_state = State.complete 

		elif self.current_state == State.push and not out_of_points:
			self.current_state = State.select_point

		else:
			raise Exception("Bad State Transition")








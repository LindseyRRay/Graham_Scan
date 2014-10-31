import unittest
from state_manager import StateManager, State



class Test_State_Manager(unittest.TestCase):

	def test_increment_state(self):
		test_state = StateManager()
		self.assertEqual(test_state.current_state, State.not_run)

		test_state.increment_state()
		self.assertEqual(test_state.current_state, State.initial_point)

		test_state.increment_state()
		self.assertEqual(test_state.current_state, State.polar_angle)

		test_state.increment_state()
		self.assertEqual(test_state.current_state, State.init_stack)

		test_state.increment_state()
		self.assertEqual(test_state.current_state, State.select_point)

		test_state.increment_state()
		self.assertEqual(test_state.current_state, State.check_angle)

		test_state.increment_state(is_right_turn = True)
		self.assertEqual(test_state.current_state, State.pop)

		test_state.increment_state()
		self.assertEqual(test_state.current_state, State.check_angle)

		test_state.increment_state(is_right_turn = False)
		self.assertEqual(test_state.current_state, State.push)

		test_state.increment_state()
		self.assertEqual(test_state.current_state, State.select_point)

		test_state.increment_state()
		self.assertEqual(test_state.current_state, State.check_angle)

		test_state.increment_state(is_right_turn = True)
		self.assertEqual(test_state.current_state, State.pop)

		test_state.increment_state()
		self.assertEqual(test_state.current_state, State.check_angle)

		test_state.increment_state(is_right_turn = False)
		self.assertEqual(test_state.current_state, State.push)

		test_state.increment_state(out_of_points = True)
		self.assertEqual(test_state.current_state, State.complete)


if __name__=='__main__':
	unittest.main()
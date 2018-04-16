from bloxorz import *
import unittest

class TestBloxorz(unittest.TestCase):

	def setUp(self):
		self.bloxorz =  create_stage(2)

	def test_is_goal_state(self):
		# Test False
		list_false_goal_state = [
			((0,0),(1,1),(1,1,1,1)),	# 2 block not on GOAL_HOLE
			((1,13),(1,2),(0,0,0,0))	# 1 block not on GOAL_HOLE
		]

		for state in list_false_goal_state:
			self.assertFalse(self.bloxorz.is_goal_state(state))

		# Test True
		list_true_goal_state = [
			((1,13),(1,13),(0,0,0,0))
		]

		for state in list_true_goal_state:
			self.assertTrue(self.bloxorz.is_goal_state(state))

if __name__ == '__main__':
    unittest.main()
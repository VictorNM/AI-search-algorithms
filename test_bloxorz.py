from bloxorz import *
import unittest

class TestBloxorz(unittest.TestCase):

	def setUp(self):
		self.bloxorz =  create_stage(2)

	def test_is_goal_state(self):
		# Test False
		false_list = [
			((0,0),(1,1),(1,1,1,1)),	# 2 block not on GOAL_HOLE
			((1,13),(1,2),(0,0,0,0))	# 1 block not on GOAL_HOLE
		]

		for state in false_list:
			self.assertFalse(self.bloxorz.is_goal_state(state))

		# Test True
		true_list = [
			((1,13),(1,13),(0,0,0,0))
		]

		for state in true_list:
			self.assertTrue(self.bloxorz.is_goal_state(state))

	def test_is_standing(self):
		# Test False
		false_list = [
			((0,0), (0,1)),
			((1,0), (1,1))
		]

		for position in false_list:
			self.assertFalse(self.bloxorz._is_standing(position[0], position[1]))

		# Test True
		true_list = [
			((0,0), (0,0))
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_standing(position[0], position[1]))

	def test_is_lying(self):
		# Test False
		false_list = [
			((0,0), (0,0)),		# standing
			((0,0), (1,1))		# splitting
		]

		for position in false_list:
			self.assertFalse(self.bloxorz._is_lying(position[0], position[1]))

		# Test True
		true_list = [
			((0,0), (0,1)),		# lying X
			((0,0), (1,0))		# lying Y
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_lying(position[0], position[1]))

	def test_is_splitting(self):
		# Test False
		false_list = [
			((0,0), (0,0)),		# standing
			((0,0), (0,1)),		# lying X
			((0,0), (1,0))		# lying Y			
		]

		for position in false_list:
			self.assertFalse(self.bloxorz._is_splitting(position[0], position[1]))

		# Test True
		true_list = [
			((0,0), (1,1)),		# adjacent diagonal
			((0,0), (2,0)), 	# splitting X
			((0,0), (0,2)),		# splitting Y
			((0,0), (5,9))		# far split
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_splitting(position[0], position[1]))


if __name__ == '__main__':
    unittest.main()
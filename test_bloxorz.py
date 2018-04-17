from bloxorz import *
import unittest

class TestBloxorz(unittest.TestCase):

	def setUp(self):
		self.bloxorz =  create_stage(2)

	def test_is_goal_state(self):
		# Test False
		false_list = [
			( ((0,0), (1,1)), (1,1,1,1)),	# 2 block not on GOAL_HOLE
			( ((1,13), (1,2)), (0,0,0,0))	# 1 block not on GOAL_HOLE
		]

		for state in false_list:
			self.assertFalse(self.bloxorz.is_goal_state(state))

		# Test True
		true_list = [
			( ((1,13),(1,13)), (0,0,0,0))
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
			self.assertFalse(self.bloxorz._is_standing(position))

		# Test True
		true_list = [
			((0,0), (0,0))
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_standing(position))

	def test_is_lying_row(self):
		# Test False
		false_list = [
			((0,0), (0,0)),		# standing
			((0,0), (1,0)),		# laying Y
			((0,0), (1,1))		# splitting
		]

		for position in false_list:
			self.assertFalse(self.bloxorz._is_lying_row(position))

		# Test True
		true_list = [
			((0,0), (0,1)),		# lying X
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_lying_row(position))

	def test_is_lying_col(self):
		# Test False
		false_list = [
			((0,0), (0,0)),		# standing
			((0,0), (0,1)),		# laying X
			((0,0), (1,1))		# splitting
		]

		for position in false_list:
			self.assertFalse(self.bloxorz._is_lying_col(position))

		# Test True
		true_list = [
			((0,0), (1,0)),		# lying Y
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_lying_col(position))

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

	def test_is_valid_position(self):
		# Test False
		false_list = [
			((0,0), (0,-1)),		# lying X 1 block out of map
			((-1,0), (0,0)),		# lying Y 1 block out of map
			((0,0), (0,0)), 		# standing on empty
			((0,0), (1,0)),			# lying Y 1 block on empty
			((1,3), (1,4)),			# lying X 1 block on empty
		]

		for position in false_list:
			self.assertFalse(self.bloxorz._is_valid_position(position))

		# Test True
		true_list = [
			((1,0), (1,1)),		# valid lying X
			((1,0), (2,0)),		# valid lying Y
			((1,0), (3,2)),		# valid splitting
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_valid_position(position))

	def test_move_all_up(self):
		testcase_expect_dict = {
			((3,3), (3,3)) : ((1,3), (2,3)),		# standing
			((3,3), (3,4)) : ((2,3), (2,4)),		# lying row
			((3,3), (2,3)) : ((1,3), (1,3)),		# lying col
		}

		for testcase, expect in testcase_expect_dict.items():
			# print(testcase, expect)
			self.assertEqual(self.bloxorz._move_all_up(testcase), expect)

if __name__ == '__main__':
    unittest.main()
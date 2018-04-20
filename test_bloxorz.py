from bloxorz import *
from bloxorz_solver import *
import unittest

class TestBloxorz(unittest.TestCase):

	def setUp(self):
		bloxorz_creator = BloxorzCreator()
		self.bloxorz =  bloxorz_creator.create_stage(2)

	# TEST GOAL

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

	# TEST BLOCK STATUS

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
			self.assertFalse(self.bloxorz._is_splitting(position))

		# Test True
		true_list = [
			((0,0), (1,1)),		# adjacent diagonal
			((0,0), (2,0)), 	# splitting X
			((0,0), (0,2)),		# splitting Y
			((0,0), (5,9))		# far split
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_splitting(position))

	# TEST VALIDITY

	def test_is_valid_block_position(self):
		# Test False
		false_list = [
			((0,0), (0,-1)),		# lying X 1 block out of map
			((-1,0), (0,0)),		# lying Y 1 block out of map
			((0,0), (0,0)), 		# standing on empty
			((0,0), (1,0)),			# lying Y 1 block on empty
			((1,3), (1,4)),			# lying X 1 block on empty
			((3,4), (3,3)),			# lying X 1 block on empty
			((5,5), (5,6)),			# lying X 1 block on empty
		]

		for position in false_list:
			self.assertFalse(self.bloxorz._is_valid_block_position(position))

		# Test True
		true_list = [
			((1,0), (1,1)),		# valid lying X
			((1,0), (2,0)),		# valid lying Y
			((1,0), (3,2)),		# valid splitting
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_valid_block_position(position))

	# TEST MOVEMENTS

	def test_move_single_up(self):
		testcase_expect_dict = {
			(3,3) : (2,3),
		}

		for testcase, expect in testcase_expect_dict.items():
			self.assertEqual(self.bloxorz._move_single_up(testcase), expect)

	def test_move_single_down(self):
		testcase_expect_dict = {
			(3,3) : (4,3),
		}

		for testcase, expect in testcase_expect_dict.items():
			self.assertEqual(self.bloxorz._move_single_down(testcase), expect)

	def test_move_single_left(self):
		testcase_expect_dict = {
			(3,3) : (3,2),
		}

		for testcase, expect in testcase_expect_dict.items():
			self.assertEqual(self.bloxorz._move_single_left(testcase), expect)

	def test_move_single_right(self):
		testcase_expect_dict = {
			(3,3) : (3,4),
		}

		for testcase, expect in testcase_expect_dict.items():
			self.assertEqual(self.bloxorz._move_single_right(testcase), expect)

	def test_do_all_single_moves(self):
		testcase_expect_dict = {
			((3,1), (3,7)) :
				[((2,1), (3,7)), ((3,1), (2,7)),	# up
				 ((4,1), (3,7)), ((3,1), (4,7)),	# down
				 ((3,0), (3,7)), ((3,1), (3,6)),	# left
				 ((3,2), (3,7)), ((3,1), (3,8)),	# right
				]
		}

		for testcase, expect in testcase_expect_dict.items():
			self.assertEqual(self.bloxorz._do_all_single_moves(testcase), expect)

	def test_move_pair_up(self):

		# standing
		testcase_expect_standing_dict = {
			((3,3), (3,3)) : ((1,3), (2,3)),
		}

		for testcase, expect in testcase_expect_standing_dict.items():
			self.assertEqual(self.bloxorz._move_pair_up(testcase), expect)

		# lying row
		testcase_expect_lying_row_dict = {
			((3,3), (3,4)) : ((2,3), (2,4)),
		}

		for testcase, expect in testcase_expect_lying_row_dict.items():
			self.assertEqual(self.bloxorz._move_pair_up(testcase), expect)

		# lying col
		testcase_expect_lying_col_dict = {
			((3,3), (2,3)) : ((1,3), (1,3)),
		}

		for testcase, expect in testcase_expect_lying_col_dict.items():
			self.assertEqual(self.bloxorz._move_pair_up(testcase), expect)

	def test_move_pair_down(self):

		# standing
		testcase_expect_standing_dict = {
			((3,3), (3,3)) : ((5,3), (4,3)),
		}

		for testcase, expect in testcase_expect_standing_dict.items():
			self.assertEqual(self.bloxorz._move_pair_down(testcase), expect)

		# lying row
		testcase_expect_lying_row_dict = {
			((3,3), (3,4)) : ((4,3), (4,4)),
		}

		for testcase, expect in testcase_expect_lying_row_dict.items():
			self.assertEqual(self.bloxorz._move_pair_down(testcase), expect)

		# lying col
		testcase_expect_lying_col_dict = {
			((3,3), (2,3)) : ((4,3), (4,3)),
		}

		for testcase, expect in testcase_expect_lying_col_dict.items():
			self.assertEqual(self.bloxorz._move_pair_down(testcase), expect)

	def test_move_pair_left(self):

		# standing
		testcase_expect_standing_dict = {
			((3,3), (3,3)) : ((3,1), (3,2)),
		}

		for testcase, expect in testcase_expect_standing_dict.items():
			self.assertEqual(self.bloxorz._move_pair_left(testcase), expect)

		# lying row
		testcase_expect_lying_row_dict = {
			((3,3), (3,4)) : ((3,2), (3,2)),
		}

		for testcase, expect in testcase_expect_lying_row_dict.items():
			self.assertEqual(self.bloxorz._move_pair_left(testcase), expect)

		# lying col
		testcase_expect_lying_col_dict = {
			((3,3), (2,3)) : ((3,2), (2,2)),
		}

		for testcase, expect in testcase_expect_lying_col_dict.items():
			self.assertEqual(self.bloxorz._move_pair_left(testcase), expect)

	def test_move_pair_right(self):

		# standing
		testcase_expect_standing_dict = {
			((3,3), (3,3)) : ((3,5), (3,4)),
		}

		for testcase, expect in testcase_expect_standing_dict.items():
			self.assertEqual(self.bloxorz._move_pair_right(testcase), expect)

		# lying row
		testcase_expect_lying_row_dict = {
			((3,3), (3,4)) : ((3,5), (3,5)),
		}

		for testcase, expect in testcase_expect_lying_row_dict.items():
			self.assertEqual(self.bloxorz._move_pair_right(testcase), expect)

		# lying col
		testcase_expect_lying_col_dict = {
			((3,3), (2,3)) : ((3,4), (2,4)),
		}

		for testcase, expect in testcase_expect_lying_col_dict.items():
			self.assertEqual(self.bloxorz._move_pair_right(testcase), expect)

	def test_do_all_pair_moves(self):
		# standing
		testcase_expect_standing_dict = {
			((3,2), (3,2)) :
				[((1,2), (2,2)),	# up
				 ((5,2), (4,2)),	# down
				 ((3,0), (3,1)),	# left
				 ((3,4), (3,3)),	# right
				]
		}

		for testcase, expect in testcase_expect_standing_dict.items():
			self.assertEqual(self.bloxorz._do_all_pair_moves(testcase), expect)

	def test_do_all_valid_moves(self):
		# standing
		testcase_expect_standing_dict = {
			((3,2), (3,2)) :
				[((1,2), (2,2)),	# up
				 ((4,2), (5,2)),	# down
				 ((3,0), (3,1)),	# left
				]
		}

		for testcase, expect in testcase_expect_standing_dict.items():
			self.assertEqual(self.bloxorz._do_all_valid_moves(testcase), expect)

	# TEST CONSEQUENCE
	def test_is_on_soft_switch(self):
		# Test False
		false_list = [
			(0,0),
			(1,8),
		]

		for position in false_list:
			self.assertFalse(self.bloxorz._is_on_soft_switch(position))

		# Test True
		true_list = [
			(2,2)
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_on_soft_switch(position))

	def test_is_on_hard_switch(self):
		# Test False
		false_list = [
			((0,0),(0,1)),		# 0 block on hard switch
			((1,8),(1,9)),		# 1 block on hard switch
		]

		for position in false_list:
			self.assertFalse(self.bloxorz._is_on_hard_switch(position))

		# Test True
		true_list = [
			((1,8),(1,8)),
		]

		for position in true_list:
			self.assertTrue(self.bloxorz._is_on_hard_switch(position))

	def test_change_list_bridge_status(self):
		soft_switch_position = (2,2)
		bridge_status_list = (Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT)
		expect_result = (Square.H_TI,Square.H_TI,Square.EMPT,Square.EMPT)
		real_result = self.bloxorz._change_list_bridge_status(soft_switch_position, bridge_status_list)
		self.assertEqual(real_result, expect_result)

	def test_get_move_consequence(self):
		pass

	# TEST HEURISTIC

	def test_get_distance(self):
		testcase_expect_dict = {
			((0,0), (0,4)) : 4,
			((0,0), (4,0)) : 4,
			((0,0), (4,4)) : 8,
		}

		for pair_position, distance in testcase_expect_dict.items():
			self.assertEqual(self.bloxorz._get_distance(pair_position[0], pair_position[1]), distance)

	def test_get_distance_to_goal(self):
		testcase_expect_dict = {
			((1,13), (1,13)) : 0,
			((1,0), (1,1)) : 25,
			((2,13), (3,13)) : 3,
			((0,0), (0,0)) : 28
		}

		for pair_position, distance in testcase_expect_dict.items():
			self.assertEqual(self.bloxorz._get_distance_to_goal(pair_position), distance)



if __name__ == '__main__':
    unittest.main()
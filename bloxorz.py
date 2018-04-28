from state_space_search import *
from heuristic_search import *
from enum import Enum
import numpy as np 				# for print matrix

class Square(Enum):
	EMPT = 0
	H_TI = 1
	S_TI = 2
	H_SW = 3
	S_SW = 4
	SPLI = 5
	GOAL = 6

	def __int__(self):
		return self.value

class Map(object):
	def __init__(self, stage_map = None):
		if stage_map is not None:
			self._map_matrix = stage_map._map_matrix
			self._bridge_positions = stage_map._bridge_positions
			self._switch_bridge_dict = stage_map._switch_bridge_dict
			self._split_port_dest_dict = stage_map._split_port_dest_dict
			self._goal_position = stage_map._goal_position
		else:
			self._map_matrix = None
			self._bridge_positions = None
			self._switch_bridge_dict = None
			self._split_port_dest_dict = None
			self._goal_position = None
	
	def set_map(self, map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict):
		self._map_matrix = map_matrix
		self._bridge_positions = bridge_positions
		self._switch_bridge_dict = switch_bridge_dict
		self._split_port_dest_dict = split_port_dest_dict
		self._goal_position = self.set_goal()

	def set_goal(self):
		for row in range(len(self._map_matrix)):
			for col in range(len(self._map_matrix[row])):
				if self._map_matrix[row][col] == Square.GOAL.value:
					return (row, col)

	def parse_bridge_status(self, list_bridge_status):
		for index, position in enumerate(self._bridge_positions):
			(row, col) = position
			self._map_matrix[row][col] = list_bridge_status[index]

	def get_map_value(self, position):
		(row, col) = position
		return self._map_matrix[row][col]

	def get_list_bridge_action_of_switch(self, switch_position):
		return self._switch_bridge_dict[switch_position]

	def get_list_split_dest_of_port(self, split_port_position):
		return self._split_port_dest_dict[split_port_position]

	def is_in_map(self, position):
		(row, col) = position
		width = len(self._map_matrix[0])
		heigth = len(self._map_matrix)
		
		if row < 0 or row > heigth - 1: return False
		if col < 0 or col > width - 1: return False
		return True

	def get_goal_position(self):
		return self._goal_position

	def get_switch_position_list(self):
		return self._switch_bridge_dict.keys()

	def get_port_position_list(self):
		return self._split_port_dest_dict.keys()

	def __str__(self):
		value_matrix = [[int(self._map_matrix[row][col])
						for col in range(len(self._map_matrix[row]))]
						for row in range(len(self._map_matrix))]

		return str(np.matrix(value_matrix))

class Bloxorz(Problem):
	def __init__(self, stage_map = None, initial_state = None):
		self._stage_map = None
		self.initial_state = None;

		if stage_map is not None:
			self.set_map(stage_map)

		if initial_state is not None:
			self.set_initial_state(initial_state)

	def get_all_actions_results(self, current_state):
		# print(current_state[0], current_state[1], sep='\t')
		self._parse_state_to_map(current_state)
		return self._do_all_valid_moves(current_state)

	def is_goal_state(self, state):
		self._parse_state_to_map(state)
		(single_block_position_1, single_block_position_2) = state[0]

		return (self._stage_map.get_map_value(single_block_position_1) == Square.GOAL.value and
				self._stage_map.get_map_value(single_block_position_2) == Square.GOAL.value)

	def get_heuristic_rank(self, state):
		return self.get_normal_heuristic_rank(state)
		pair_block_position = state[0]
		bridge_status_list = state[1]
		total_close = sum(1 for bridge_status in bridge_status_list if bridge_status == Square.EMPT.value)
		can_move_to_goal_rank = 0
		if not self._can_move_to_goal(state):
			can_move_to_goal_rank = 1

		min_distance = 1000
		if self._is_splitting(pair_block_position):
			min_distance = self._get_distance_to_nearest_switch(pair_block_position)
		else:
			min_distance = self._get_distance_to_nearest_switch(pair_block_position)
			if min_distance > self._get_distance_to_nearest_split_port(pair_block_position):
				min_distance = self._get_distance_to_nearest_split_port(pair_block_position)

		return (can_move_to_goal_rank, total_close, min_distance, self._get_distance_to_goal(pair_block_position))
		# return self._get_distance_to_goal(pair_block_position)

	def get_normal_heuristic_rank(self, state):
		pair_block_position = state[0]
		bridge_status_list = state[1]
		return self._get_distance_to_goal(pair_block_position)

	def set_initial_state(self, initial_state):
		self.initial_state = initial_state
		self._parse_state_to_map(initial_state)

	def set_map(self, stage_map):
		self._stage_map = stage_map

	def _do_all_valid_moves(self, current_state):
		action_new_state_list = None
		pair_block_position = current_state[0]
		bridge_status_list = current_state[1]
		# move
		if self._is_splitting(pair_block_position):
			action_new_state_list = self._do_all_valid_single_moves(current_state)
		else:
			action_new_state_list = self._do_all_valid_pair_moves(current_state)
		
		# adjust: position_1 always <= position_2
		adjusted_list = []
		for (action, state) in action_new_state_list:
			position = state[0]
			position = self._adjust_block_position_order(position)
			state = (position, state[1])
			adjusted_list.append((action, state))

		action_new_state_list = adjusted_list
		return action_new_state_list

	def _adjust_block_position_order(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		if single_block_position_1 > single_block_position_2:
			return (single_block_position_2, single_block_position_1)
		return pair_block_position

	def _is_standing(self, pair_block_position):
		return pair_block_position[0] == pair_block_position[1]

	def _is_lying_row(self, pair_block_position):
		(row_1, col_1) = pair_block_position[0]
		(row_2, col_2) = pair_block_position[1]

		return (row_1 == row_2) and (abs(col_1 - col_2) == 1)

	def _is_lying_col(self, pair_block_position):
		(row_1, col_1) = pair_block_position[0]
		(row_2, col_2) = pair_block_position[1]

		return (col_1 == col_2) and (abs(row_1 - row_2) == 1)

	def _is_splitting(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		(row_1, col_1) = single_block_position_1
		(row_2, col_2) = single_block_position_2

		return abs(row_1 - row_2) + abs(col_1 - col_2) > 1

	def _do_all_valid_single_moves(self, current_state):
		pair_block_position = current_state[0]
		bridge_status_list = current_state[1]
		action_new_state_list = []
		(single_block_position_1, single_block_position_2) = pair_block_position

		# move up
		new_pair_position_up_1 = (self._move_single_up(single_block_position_1), single_block_position_2)
		new_pair_position_up_2 = (single_block_position_1, self._move_single_up(single_block_position_2))

		new_state_up_1 = self._get_consequence_for_single_move(new_pair_position_up_1, bridge_status_list, 1)
		new_state_up_2 = self._get_consequence_for_single_move(new_pair_position_up_2, bridge_status_list, 2)

		if self._is_valid_state(new_state_up_1):
			action_up_1 = "{position}: UP".format(position=single_block_position_1)
			action_new_state_list.append((action_up_1, new_state_up_1))

		if self._is_valid_state(new_state_up_2):
			action_up_2 = "{position}: UP".format(position=single_block_position_2)
			action_new_state_list.append((action_up_2, new_state_up_2))

		# move down
		new_pair_position_down_1 = (self._move_single_down(single_block_position_1), single_block_position_2)
		new_pair_position_down_2 = (single_block_position_1, self._move_single_down(single_block_position_2))

		new_state_down_1 = self._get_consequence_for_single_move(new_pair_position_down_1, bridge_status_list, 1)
		new_state_down_2 = self._get_consequence_for_single_move(new_pair_position_down_2, bridge_status_list, 2)

		if self._is_valid_state(new_state_down_1):
			action_down_1 = "{position}: DOWN".format(position=single_block_position_1)
			action_new_state_list.append((action_down_1, new_state_down_1))

		if self._is_valid_state(new_state_down_2):
			action_down_2 = "{position}: DOWN".format(position=single_block_position_2)
			action_new_state_list.append((action_down_2, new_state_down_2))

		# move left
		new_pair_position_left_1 = (self._move_single_left(single_block_position_1), single_block_position_2)
		new_pair_position_left_2 = (single_block_position_1, self._move_single_left(single_block_position_2))

		new_state_left_1 = self._get_consequence_for_single_move(new_pair_position_left_1, bridge_status_list, 1)
		new_state_left_2 = self._get_consequence_for_single_move(new_pair_position_left_2, bridge_status_list, 2)

		if self._is_valid_state(new_state_left_1):
			action_left_1 = "{position}: LEFT".format(position=single_block_position_1)
			action_new_state_list.append((action_left_1, new_state_left_1))

		if self._is_valid_state(new_state_left_2):
			action_left_2 = "{position}: LEFT".format(position=single_block_position_2)
			action_new_state_list.append((action_left_2, new_state_left_2))

		# move right
		new_pair_position_right_1 = (self._move_single_right(single_block_position_1), single_block_position_2)
		new_pair_position_right_2 = (single_block_position_1, self._move_single_right(single_block_position_2))

		new_state_right_1 = self._get_consequence_for_single_move(new_pair_position_right_1, bridge_status_list, 1)
		new_state_right_2 = self._get_consequence_for_single_move(new_pair_position_right_2, bridge_status_list, 2)

		if self._is_valid_state(new_state_right_1):
			action_right_1 = "{position}: RIGHT".format(position=single_block_position_1)
			action_new_state_list.append((action_right_1, new_state_right_1))

		if self._is_valid_state(new_state_right_2):
			action_right_2 = "{position}: RIGHT".format(position=single_block_position_2)
			action_new_state_list.append((action_right_2, new_state_right_2))

		return action_new_state_list

	def _do_all_valid_pair_moves(self, current_state):
		pair_block_position = current_state[0]
		bridge_status_list = current_state[1]
		action_new_state_list = []

		# move up
		new_pair_position_up = self._move_pair_up(pair_block_position)
		new_state_up = self._get_consequence_for_pair_move(new_pair_position_up, bridge_status_list)
		if self._is_valid_state(new_state_up):
			action_new_state_list.append(("UP", new_state_up))

		# move down
		new_pair_position_down = self._move_pair_down(pair_block_position)
		new_state_down = self._get_consequence_for_pair_move(new_pair_position_down, bridge_status_list)
		if self._is_valid_state(new_state_down):
			action_new_state_list.append(("DOWN", new_state_down))

		# move left
		new_pair_position_left = self._move_pair_left(pair_block_position)
		new_state_left = self._get_consequence_for_pair_move(new_pair_position_left, bridge_status_list)
		if self._is_valid_state(new_state_left):
			action_new_state_list.append(("LEFT", new_state_left))

		# move right
		new_pair_position_right = self._move_pair_right(pair_block_position)
		new_state_right = self._get_consequence_for_pair_move(new_pair_position_right, bridge_status_list)
		if self._is_valid_state(new_state_right):
			action_new_state_list.append(("RIGHT", new_state_right))

		return action_new_state_list

	def _move_single_up(self, single_block_position):
		(row, col) = single_block_position
		return (row - 1, col)

	def _move_single_down(self, single_block_position):
		(row, col) = single_block_position
		return (row + 1, col)

	def _move_single_left(self, single_block_position):
		(row, col) = single_block_position
		return (row, col - 1)

	def _move_single_right(self, single_block_position):
		(row, col) = single_block_position
		return (row, col + 1)

	def _move_pair_up(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		(row_1, col_1) = single_block_position_1
		(row_2, col_2) = single_block_position_2

		if self._is_standing(pair_block_position):
			row_1 -= 2
			row_2 -= 1
		elif self._is_lying_row(pair_block_position):
			row_1 -= 1
			row_2 -= 1
		elif self._is_lying_col(pair_block_position):
			if row_1 < row_2: row_1 -= 1
			else: row_1 -= 2
			row_2 = row_1

		new_pair_block_position = ((row_1, col_1),(row_2, col_2))
		return new_pair_block_position

	def _move_pair_down(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		(row_1, col_1) = single_block_position_1
		(row_2, col_2) = single_block_position_2

		if self._is_standing(pair_block_position):
			row_1 += 2
			row_2 += 1
		elif self._is_lying_row(pair_block_position):
			row_1 += 1
			row_2 += 1
		elif self._is_lying_col(pair_block_position):
			if row_1 > row_2: row_1 += 1
			else: row_1 += 2
			row_2 = row_1

		new_pair_block_position = ((row_1, col_1),(row_2, col_2))
		return new_pair_block_position

	def _move_pair_left(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		(row_1, col_1) = single_block_position_1
		(row_2, col_2) = single_block_position_2

		if self._is_standing(pair_block_position):
			col_1 -= 2
			col_2 -= 1
		elif self._is_lying_row(pair_block_position):
			if col_1 < col_2: col_1 -= 1
			else: col_1 -= 2
			col_2 = col_1
		elif self._is_lying_col(pair_block_position):
			col_1 -= 1
			col_2 -= 1

		new_pair_block_position = ((row_1, col_1),(row_2, col_2))
		return new_pair_block_position

	def _move_pair_right(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		(row_1, col_1) = single_block_position_1
		(row_2, col_2) = single_block_position_2

		if self._is_standing(pair_block_position):
			col_1 += 2
			col_2 += 1
		elif self._is_lying_row(pair_block_position):
			if col_1 > col_2: col_1 += 1
			else: col_1 += 2
			col_2 = col_1
		elif self._is_lying_col(pair_block_position):
			col_1 += 1
			col_2 += 1

		new_pair_block_position = ((row_1, col_1),(row_2, col_2))
		return new_pair_block_position

	def _is_valid_state(self, state):
		pair_block_position = state[0]
		bridge_status_list = state[1]

		stage_map = Map(self._stage_map)
		stage_map.parse_bridge_status(bridge_status_list)
		return self._is_valid_block_position(pair_block_position, stage_map)

	def _is_valid_block_position(self, pair_block_position, stage_map):
		(single_block_position_1, single_block_position_2) = pair_block_position
		# check with map's dimension
		if (not stage_map.is_in_map(single_block_position_1) or
			not stage_map.is_in_map(single_block_position_2)):
			return False

		# check empty
		if (stage_map.get_map_value(single_block_position_1) == Square.EMPT.value or
			stage_map.get_map_value(single_block_position_2) == Square.EMPT.value):
			return False

		# check solf tile
		if (self._is_standing(pair_block_position) and
			stage_map.get_map_value(single_block_position_1) == Square.S_TI.value):
			return False

		return True

	def _get_consequence_for_pair_move(self, pair_block_position, bridge_status_list):
		if (not self._is_valid_state((pair_block_position, bridge_status_list))):
			return (pair_block_position, bridge_status_list)

		# on soft switch: check all 2 single positions
		if self._is_on_soft_switch(pair_block_position[0]):
			switch_position = pair_block_position[0]
			bridge_status_list = self._change_list_bridge_status(switch_position, bridge_status_list)
		if (pair_block_position[1] != pair_block_position[0] and
			self._is_on_soft_switch(pair_block_position[1])):
			switch_position = pair_block_position[1]
			bridge_status_list = self._change_list_bridge_status(switch_position, bridge_status_list)

		# on hard switch
		if self._is_on_hard_switch(pair_block_position):
			switch_position = pair_block_position[0]
			bridge_status_list = self._change_list_bridge_status(switch_position, bridge_status_list)

		# on split port
		if self._is_on_split_port(pair_block_position):
			split_port_position = pair_block_position[0]
			pair_block_position = self._move_to_split_dest(split_port_position)

		return (pair_block_position, bridge_status_list)

	def _get_consequence_for_single_move(self, pair_block_position, bridge_status_list, moved_block):
		if (not self._is_valid_state((pair_block_position, bridge_status_list))):
			return (pair_block_position, bridge_status_list)

		block_index = moved_block - 1

		# only check for on soft switch

		if not self._is_splitting(pair_block_position):
			# check all 2 single positions
			if self._is_on_soft_switch(pair_block_position[0]):
				switch_position = pair_block_position[0]
				bridge_status_list = self._change_list_bridge_status(switch_position, bridge_status_list)
			if (pair_block_position[1] != pair_block_position[0] and
				self._is_on_soft_switch(pair_block_position[1])):
				switch_position = pair_block_position[1]
				bridge_status_list = self._change_list_bridge_status(switch_position, bridge_status_list)
		else:
			# check 1 single position
			if self._is_on_soft_switch(pair_block_position[block_index]):
				switch_position = pair_block_position[block_index]
				bridge_status_list = self._change_list_bridge_status(switch_position, bridge_status_list)

		return (pair_block_position, bridge_status_list)

	def _is_on_soft_switch(self, single_block_position):
		return self._stage_map.get_map_value(single_block_position) == Square.S_SW.value

	def _is_on_hard_switch(self, pair_block_position):
		(position_1, position_2) = pair_block_position
		if position_1 != position_2:
			return False
		return self._stage_map.get_map_value(position_1) == Square.H_SW.value

	def _is_on_split_port(self, pair_block_position):
		(position_1, position_2) = pair_block_position
		if position_1 != position_2:
			return False
		return self._stage_map.get_map_value(position_1) == Square.SPLI.value

	def _change_list_bridge_status(self, switch_position, bridge_status_list):
		bridge_action_list = self._stage_map.get_list_bridge_action_of_switch(switch_position)
		bridge_status_list = list(bridge_status_list)

		for bridge_action in bridge_action_list:
			bridge_index = bridge_action[0]
			action_code = bridge_action[1]
			if action_code == -1:
				bridge_status_list[bridge_index] = Square.EMPT.value
			elif action_code == 1:
				bridge_status_list[bridge_index] = Square.H_TI.value
			elif action_code == 0:
				if bridge_status_list[bridge_index] == Square.EMPT.value:
					bridge_status_list[bridge_index] = Square.H_TI.value
				else:
					bridge_status_list[bridge_index] = Square.EMPT.value

		return tuple(bridge_status_list)
		
	def _move_to_split_dest(self, split_port_position):
		split_dest_list = self._stage_map.get_list_split_dest_of_port(split_port_position)
		return tuple(split_dest_list)

	def _get_distance_to_goal(self, pair_block_position):
		goal_position = self._stage_map.get_goal_position()
		return self._calculate_distance_to_pair_item(pair_block_position, goal_position)

	def _get_distance_to_nearest_split_port(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		split_port_position_list = self._stage_map.get_port_position_list()
		min_distance = 1000
		for split_port_position in split_port_position_list:
			distance = self._calculate_distance_to_pair_item(pair_block_position, split_port_position)
			if distance < min_distance: min_distance = distance
		return min_distance

	def _get_distance_to_nearest_switch(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		switch_position_list = self._stage_map.get_switch_position_list()
		min_distance = 1000
		for switch_position in switch_position_list:
			if self._stage_map.get_map_value(switch_position) == Square.H_SW.value:
				distance = self._calculate_distance_to_pair_item(pair_block_position, switch_position)
			else:
				distance = self._calculate_distance_to_single_item(pair_block_position, switch_position)
			if distance < min_distance: min_distance = distance
		return min_distance

	# for distance to goal, hard switch, split port
	def _calculate_distance_to_pair_item(self, pair_block_position, destination_position):
		(position_1 , position_2) = pair_block_position
		distance_1 = self._get_distance(position_1, destination_position)
		distance_2 = self._get_distance(position_2, destination_position)

		pair_distance = distance_1 + distance_2

		# for normal distance calculation
		return distance_1 + distance_2

		if pair_distance == 1: return 4
		return pair_distance

	# for distance to soft switch
	def _calculate_distance_to_single_item(self, pair_block_position, destination_position):
		(position_1 , position_2) = pair_block_position
		distance_1 = self._get_distance(position_1, destination_position)
		distance_2 = self._get_distance(position_2, destination_position)

		# for normal distance calculation
		return distance_1 + distance_2

		return 2 * min(distance_1, distance_2)

	def _get_distance(self, position_1, position_2):
		(row_1, col_1) = position_1
		(row_2, col_2) = position_2

		distance = abs(row_1 - row_2) + abs(col_1 - col_2)
		return distance

	def _can_move_to_goal(self, state):
		stage_map = Map(self._stage_map)
		stage_map.parse_bridge_status(state[1])
		(goal_row, goal_col) = self._stage_map.get_goal_position()

		goal_up_pair = ( (goal_row - 1, goal_col), (goal_row - 2, goal_col) )
		if self._is_valid_block_position(goal_up_pair, stage_map):
			return True

		goal_down_pair = ( (goal_row + 1, goal_col), (goal_row + 2, goal_col) )
		if self._is_valid_block_position(goal_down_pair, stage_map):
			return True

		goal_left_pair = ( (goal_row, goal_col - 1), (goal_row, goal_col - 2) )
		if self._is_valid_block_position(goal_left_pair, stage_map):
			return True

		goal_right_pair = ( (goal_row, goal_col + 1), (goal_row, goal_col + 2) )
		if self._is_valid_block_position(goal_right_pair, stage_map):
			return True

	def _parse_state_to_map(self, state):
		list_bridge_status = state[1]
		self._stage_map.parse_bridge_status(list_bridge_status)

	def draw_map(self):
		print(self._stage_map)
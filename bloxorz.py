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
	def __init__(self):
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
		# find goal position
		for row in range(len(self._map_matrix)):
			for col in range(len(self._map_matrix[row])):
				if self._map_matrix[row][col] == Square.GOAL.value:
					self._goal_position = (row, col)

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

	def generate_next_states(self, current_state):
		self._parse_state_to_map(current_state)
		pair_block_position = current_state[0]
		bridge_status_list = current_state[1]

		next_states = []
		new_pair_block_position_list = self._do_all_valid_moves(pair_block_position)
		for pair_block_position in new_pair_block_position_list:
			state = self._get_move_consequence(pair_block_position, bridge_status_list)
			next_states.append(state)

		return next_states

	def is_goal_state(self, state):
		self._parse_state_to_map(state)
		(single_block_position_1, single_block_position_2) = state[0]

		return (self._stage_map.get_map_value(single_block_position_1) == Square.GOAL.value and
				self._stage_map.get_map_value(single_block_position_2) == Square.GOAL.value)

	def get_heuristic_rank(self, state):
		pair_block_position = state[0]
		bridge_status_list = state[1]
		total_open = sum(1 for bridge_status in bridge_status_list if bridge_status == Square.H_TI.value)
		# return (total_open, self._get_distance_to_goal(pair_block_position))
		# return (self._get_distance_to_goal(pair_block_position), total_open)
		return self._get_distance_to_goal(pair_block_position)

	def set_initial_state(self, initial_state):
		self.initial_state = initial_state
		self._parse_state_to_map(initial_state)

	def set_map(self, stage_map):
		self._stage_map = stage_map

	def _do_all_valid_moves(self, pair_block_position):
		new_pair_block_position_list = None
		if self._is_splitting(pair_block_position):
			new_pair_block_position_list = [pair_block_position
							 for pair_block_position in self._do_all_single_moves(pair_block_position)
							 if self._is_valid_block_position(pair_block_position)]
		else:
			new_pair_block_position_list = [pair_block_position
							 for pair_block_position in self._do_all_pair_moves(pair_block_position)
							 if self._is_valid_block_position(pair_block_position)]

		new_pair_block_position_list = self._adjust_block_position_order(new_pair_block_position_list)
		return new_pair_block_position_list

	# make sure (3,1) (3,2) is always (3,1) (3,2)
	# not (3,2) (3,1)
	def _adjust_block_position_order(self, pair_block_position_list):
		adjusted_list = []
		for pair_block_position in pair_block_position_list:
			(single_block_position_1, single_block_position_2) = pair_block_position
			if single_block_position_1 > single_block_position_2:
				adjusted_list.append((single_block_position_2, single_block_position_1))
			else:
				adjusted_list.append(pair_block_position)
		return adjusted_list

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

	def _do_all_single_moves(self, pair_block_position):
		new_pair_block_position_list = []
		(single_block_position_1, single_block_position_2) = pair_block_position

		# move up
		new_pair_position_up_1 = (self._move_single_up(single_block_position_1), single_block_position_2)
		new_pair_position_up_2 = (single_block_position_1, self._move_single_up(single_block_position_2))

		new_pair_block_position_list.append(new_pair_position_up_1)
		new_pair_block_position_list.append(new_pair_position_up_2)

		# move down
		new_pair_position_down_1 = (self._move_single_down(single_block_position_1), single_block_position_2)
		new_pair_position_down_2 = (single_block_position_1, self._move_single_down(single_block_position_2))

		new_pair_block_position_list.append(new_pair_position_down_1)
		new_pair_block_position_list.append(new_pair_position_down_2)

		# move left
		new_pair_position_left_1 = (self._move_single_left(single_block_position_1), single_block_position_2)
		new_pair_position_left_2 = (single_block_position_1, self._move_single_left(single_block_position_2))

		new_pair_block_position_list.append(new_pair_position_left_1)
		new_pair_block_position_list.append(new_pair_position_left_2)

		# move right
		new_pair_position_right_1 = (self._move_single_right(single_block_position_1), single_block_position_2)
		new_pair_position_right_2 = (single_block_position_1, self._move_single_right(single_block_position_2))

		new_pair_block_position_list.append(new_pair_position_right_1)
		new_pair_block_position_list.append(new_pair_position_right_2)

		return new_pair_block_position_list

	def _do_all_pair_moves(self, pair_block_position):
		new_pair_block_position_list = []

		# move up and check validity
		new_pair_position_up = self._move_pair_up(pair_block_position)
		new_pair_block_position_list.append(new_pair_position_up)

		# move down
		new_pair_position_down = self._move_pair_down(pair_block_position)
		new_pair_block_position_list.append(new_pair_position_down)

		# move left
		new_pair_position_left = self._move_pair_left(pair_block_position)
		new_pair_block_position_list.append(new_pair_position_left)

		# move right
		new_pair_position_right = self._move_pair_right(pair_block_position)
		new_pair_block_position_list.append(new_pair_position_right)


		return new_pair_block_position_list

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

	def _is_valid_block_position(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		# check with map's dimension
		if (not self._stage_map.is_in_map(single_block_position_1) or
			not self._stage_map.is_in_map(single_block_position_2)):
			return False
		# check empty
		if (self._stage_map.get_map_value(single_block_position_1) == Square.EMPT.value or
			self._stage_map.get_map_value(single_block_position_2) == Square.EMPT.value):
			return False

		# check solf tile
		if (self._is_standing(pair_block_position) and
			self._stage_map.get_map_value(single_block_position_1) == Square.S_TI.value):
			return False

		return True

	def _get_move_consequence(self, pair_block_position, bridge_status_list):
		# check on soft switch: check all 2 single positions
		if self._is_on_soft_switch(pair_block_position[0]):
			switch_position = pair_block_position[0]
			bridge_status_list = self._change_list_bridge_status(switch_position, bridge_status_list)
		if (pair_block_position[1] != pair_block_position[0] and
			self._is_on_soft_switch(pair_block_position[1])):
			switch_position = pair_block_position[1]
			bridge_status_list = self._change_list_bridge_status(switch_position, bridge_status_list)

		# check on hard switch
		if self._is_on_hard_switch(pair_block_position):
			switch_position = pair_block_position[0]
			bridge_status_list = self._change_list_bridge_status(switch_position, bridge_status_list)

		# check on split port
		if self._is_on_split_port(pair_block_position):
			split_port_position = pair_block_position[0]
			pair_block_position = self._move_to_split_dest(split_port_position)

		return (pair_block_position, bridge_status_list)

	def _is_on_soft_switch(self, single_block_position):
		return self._stage_map.get_map_value(single_block_position) == Square.S_SW.value

	def _is_on_hard_switch(self, pair_block_position):
		(position_1, position_2) = pair_block_position
		return (self._stage_map.get_map_value(position_1) == Square.H_SW.value and
				self._stage_map.get_map_value(position_2) == Square.H_SW.value)

	def _is_on_split_port(self, pair_block_position):
		# uncomment after write test
		(position_1, position_2) = pair_block_position
		return (self._stage_map.get_map_value(position_1) == Square.SPLI.value and
				self._stage_map.get_map_value(position_2) == Square.SPLI.value)

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

	def _change_bridge_status(self, bridge_index, action_code):
		pass

	def _move_to_split_dest(self, split_port_position):
		split_dest_list = self._stage_map.get_list_split_dest_of_port(split_port_position)
		return tuple(split_dest_list)

	def _get_distance_to_goal(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position
		goal_position = self._stage_map.get_goal_position()
		distance_1 = self._get_distance(single_block_position_1, goal_position)
		distance_2 = self._get_distance(single_block_position_2, goal_position)
		return distance_1 + distance_2

	def _get_distance(self, position_1, position_2):
		# move by row or col only
		(row_1, col_1) = position_1
		(row_2, col_2) = position_2

		return abs(row_1 - row_2) + abs(col_1 - col_2)

	def _parse_state_to_map(self, state):
		list_bridge_status = state[1]
		self._stage_map.parse_bridge_status(list_bridge_status)

	def draw_map(self):
		print(self._stage_map)

	def print_movement(self, state_path):
		for i in range(1, len(state_path)):			
			pair_position_prev = state_path[i-1][0]
			pair_position_now = state_path[i][0]

			if (not self._is_splitting(pair_position_prev) and
				not self._is_splitting(pair_position_now)):
				(row_prev, col_prev) = pair_position_prev[0]
				(row_now, col_now) = pair_position_now[0]

				if row_now < row_prev: print('[UP]', end=' ')
				elif row_now > row_prev: print('[DOWN]', end=' ')
				elif col_now < col_prev: print('[LEFT]', end=' ')
				elif col_now > col_prev: print('[RIGHT]', end=' ')

			elif (not self._is_splitting(pair_position_prev) and
					self._is_splitting(pair_position_now)):
				print('[move to split port]', end=' ')

			else:
				(row_prev_1, col_prev_1) = pair_position_prev[0]
				(row_prev_2, col_prev_2) = pair_position_prev[1]
				(row_now_1, col_now_1) = pair_position_now[0]
				(row_now_2, col_now_2) = pair_position_now[1]

				if pair_position_prev[0] != pair_position_now[0]:
					print('[', pair_position_prev[0], end=': ')
					if row_now_1 < row_prev_1: print('UP]', end=' ')
					elif row_now_1 > row_prev_1: print('DOWN]', end=' ')
					elif col_now_1 < col_prev_1: print('LEFT]', end=' ')
					elif col_now_1 > col_prev_1: print('RIGHT]', end=' ')
				else:
					print('[', pair_position_prev[1], end=': ')
					if row_now_2 < row_prev_2: print('UP]', end=' ')
					elif row_now_2 > row_prev_2: print('DOWN]', end=' ')
					elif col_now_2 < col_prev_2: print('LEFT]', end=' ')
					elif col_now_2 > col_prev_2: print('RIGHT]', end=' ')

		print()
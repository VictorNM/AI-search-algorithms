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
	
	def set_map(self, map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict):
		self._map_matrix = map_matrix
		self._bridge_positions = bridge_positions
		self._switch_bridge_dict = switch_bridge_dict
		self._split_port_dest_dict = split_port_dest_dict

	def parse_bridge_status(self, list_bridge_status):
		for index, position in enumerate(self._bridge_positions):
			row = position[0]
			col = position[1]
			self._map_matrix[row][col] = list_bridge_status[index]

	def get_map_value(self, position):
		(row, col) = position
		return self._map_matrix[row][col]

	def is_in_map(self, position):
		(row, col) = position
		width = len(self._map_matrix[0])
		heigth = len(self._map_matrix)
		
		if row < 0 or row > heigth: return False
		if col < 0 or col > width: return False
		return True

	def __str__(self):
		value_matrix = [[int(self._map_matrix[row][col])
						for y in range(len(self._map_matrix[x]))]
						for x in range(len(self._map_matrix))]

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

		return (self._stage_map.get_map_value(single_block_position_1) == Square.GOAL and
				self._stage_map.get_map_value(single_block_position_2) == Square.GOAL)

	def get_heuristic_rank(self, state):
		pass

	def set_initial_state(self, initial_state):
		self.initial_state = initial_state
		self._parse_state_to_map(initial_state)

	def set_map(self, stage_map):
		self._stage_map = stage_map

	def _do_all_valid_moves(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position

		new_pair_block_position_list = None
		if self._is_splitting:
			new_pair_block_position_list = [pair_block_position
							 for pair_block_position in self._move_single(pair_block_position)
							 if self._is_valid_position(pair_block_position)]
		else:
			new_pair_block_position_list = [pair_block_position
							 for pair_block_position in self._move_pair(pair_block_position)
							 if self._is_valid_position(pair_block_position)]


		return new_pair_block_position_list

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

	def _is_splitting(self, single_block_position_1, single_block_position_2):
		(row_1, col_1) = single_block_position_1
		(row_2, col_2) = single_block_position_2

		return abs(row_1 - row_2) + abs(col_1 - col_2) > 1

	def _move_single(self, pair_block_position):
		new_pair_block_position_list_list = []
		(single_block_position_1, single_block_position_2) = pair_block_position

		# move up
		new_pair_position_up_1 = (self._move_single_up(single_block_position_1), single_block_position_2)
		if self._is_valid_position(position_up_1):
			new_pair_block_position_list.append(new_pair_position_up_1)

		new_pair_position_up_2 = (single_block_position_1, self._move_single_up(single_block_position_2))
		if self._is_valid_position(position_up_2):
			new_pair_block_position_list.append(new_pair_position_up_2)

		# move down	

	def _move_pair(self, pair_block_position):
		new_pair_block_position_list_list = []

		# move up
		new_pair_position_up = self._move_pair_up(pair_block_position)
		if self._is_valid_position(new_pair_position_up):
			new_pair_block_position_list.append(new_pair_position_up)

		# move down
		new_pair_position_down = self._move_pair_down(pair_block_position)
		if self._is_valid_position(new_pair_position_down):
			new_pair_block_position_list.append(new_pair_position_down)

		# move left

		# move right

		return new_pair_block_position_list_list

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


	def _is_valid_position(self, pair_block_position):
		(single_block_position_1, single_block_position_2) = pair_block_position

		# check with map's dimension
		if (not self._stage_map.is_in_map(single_block_position_1) or
			not self._stage_map.is_in_map(single_block_position_2)):
			# print('out of map')
			return False

		# check empty
		if (self._stage_map.get_map_value(single_block_position_1) == Square.EMPT or
			self._stage_map.get_map_value(single_block_position_2) == Square.EMPT):
			# print('on empty')
			return False

		# check solf tile
		if (self._is_standing(pair_block_position) and
			self._stage_map.get_map_value(single_block_position_1) == Square.S_TI):
			# print('stand on solf tile')
			return False

		return True

	def _get_move_consequence(self, pair_block_position, bridge_status_list):
		pass

	def _is_valid_state(self, state):
		self._parse_state_to_map(state)

	def _get_distance_to_goal(self, single_block_position_1, single_block_position_2):
		pass

	def _parse_state_to_map(self, state):
		list_bridge_status = state[1]
		self._stage_map.parse_bridge_status(list_bridge_status)

	def draw_map(self, state = None):
		if state is not None:
			self._parse_state_to_map(state)
			print(self._stage_map)
		elif self.initial_state is not None:
			self.draw_map(self.initial_state)
		else:
			print('Error: need initial state or input state')

####################################
# CREATE STAGES
####################################
def create_stage_2():
	stage_2_map_matrix =   [[Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI],  
							[Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_SW, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.GOAL, Square.H_TI],  
							[Square.H_TI, Square.H_TI, Square.S_SW, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI],  
							[Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI],  
							[Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI],  
							[Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT]]

	stage_2_bridge_positions = [
		(4,4), (4,5), (4,10), (4,11)]

	stage_2_switch_bridge_dict = {
		(2,2) : [(0,0), (1,0)],
	 	(1,8) : [(2,0), (3,0)]}

	stage_2_split_port_dest_dict = None;

	stage_2_map = Map()
	stage_2_map.set_map(stage_2_map_matrix, stage_2_bridge_positions, stage_2_switch_bridge_dict, stage_2_split_port_dest_dict)

	stage_2_problem = Bloxorz(stage_2_map)
	stage_2_initial_state = ( ((4,1), (4,1)), (0,0,0,0) )
	stage_2_problem.set_initial_state(stage_2_initial_state)

	return stage_2_problem

def create_stage(stage_number):
	return {
		2 : create_stage_2
	}[stage_number]()

####################################
# MAIN
####################################
def main():
	stage_2 = create_stage(2)

if __name__ == '__main__':
	main()
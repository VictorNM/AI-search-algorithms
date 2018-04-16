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
			x = position[0]
			y = position[1]
			self._map_matrix[x][y] = list_bridge_status[index]

	def __str__(self):
		value_matrix = [[int(self._map_matrix[x][y])
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
		pass

	def is_goal_state(self, state):
		pass

	def get_heuristic_rank(self, state):
		pass

	def set_initial_state(self, initial_state):
		self.initial_state = initial_state
		self._parse_state_to_map(initial_state)

	def set_map(self, stage_map):
		self._stage_map = stage_map

	def _is_valid_state(self, state):
		self._parse_state_to_map(state)		

	def _set_bridge_positions(self, positions):
		pass

	def _set_switch_bridge_dict(self, switch_bridge_dict):
		pass

	def _set_split_port_dest_dict(self, split_port_dest_dict):
		pass

	def _get_distance_to_goal(self, position_1, position_2):
		pass

	def _parse_state_to_map(self, state):
		list_bridge_status = state[2]
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
	stage_2_initial_state = ((4,1), (4,1), (0,0,0,0))
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
	stage_2.draw_map()
	state = ((0,0),(0,0),(1,1,1,1))
	stage_2.draw_map(state)
	
if __name__ == '__main__':
	main()
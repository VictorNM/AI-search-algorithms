from bloxorz import *
import time

####################################
# CREATE STAGES
####################################
class BloxorzCreator(object):
	
	def create_stage(self, stage_number):
		return {
			1	: self.create_stage_1,
			2 	: self.create_stage_2,
			3 	: self.create_stage_3,
			4	: self.create_stage_4,
			5 	: self.create_stage_5,
			6 	: self.create_stage_6,
			7 	: self.create_stage_7,
			8 	: self.create_stage_8,
			9 	: self.create_stage_9,
			10	: self.create_stage_10,
			11	: self.create_stage_11,
			12	: self.create_stage_12,
			13	: self.create_stage_13,
			14	: self.create_stage_14,
			15	: self.create_stage_15,
			16	: self.create_stage_16,
			17	: self.create_stage_17,
			18	: self.create_stage_18,
			19	: self.create_stage_19,
			20	: self.create_stage_20,
			21	: self.create_stage_21,
			22	: self.create_stage_22,
			23	: self.create_stage_23,
			24	: self.create_stage_24,
			29	: self.create_stage_29,
			30	: self.create_stage_30,
			31	: self.create_stage_31,
			32	: self.create_stage_32,
			33	: self.create_stage_33,
		}[stage_number]()

	def create_stage_1(self):
		map_matrix = [
			[1,1,1,0,0,0,0,0,0,0],
			[1,1,1,1,1,1,0,0,0,0],
			[1,1,1,1,1,1,1,1,1,0],
			[0,1,1,1,1,1,1,1,1,1],
			[0,0,0,0,0,1,1,6,1,1],
			[0,0,0,0,0,0,1,1,1,0],
		]

		bridge_positions = []
		switch_bridge_dict = {}
		split_port_dest_dict = {}
		start_position = ((1,1), (1,1))
		start_bridge_status = ()

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_2(self):
		stage_2_map_matrix =   [
			[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],  
			[1, 1, 1, 1, 0, 0, 1, 1, 3, 1, 0, 0, 1, 6, 1],  
			[1, 1, 4, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],  
			[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],  
			[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],  
			[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
		]

		stage_2_bridge_positions = [
			(4,4), (4,5), (4,10), (4,11)]

		stage_2_switch_bridge_dict = {
			(2,2) : [(0,0), (1,0)],
		 	(1,8) : [(2,0), (3,0)]}

		stage_2_split_port_dest_dict = {};

		start_position = ( (4,1), (4,1) )
		start_bridge_status = (0,0,0,0)

		stage_2_map = Map()
		stage_2_map.set_map(stage_2_map_matrix, stage_2_bridge_positions, stage_2_switch_bridge_dict, stage_2_split_port_dest_dict)

		stage_2_problem = Bloxorz(stage_2_map)
		stage_2_initial_state = ( start_position, start_bridge_status )
		stage_2_problem.set_initial_state(stage_2_initial_state)

		return stage_2_problem

	def create_stage_3(self):
		map_matrix = [
			[0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],  
			[1,1,1,1,0,0,1,1,1,0,0,1,1,0,0],  
			[1,1,1,1,1,1,1,1,1,0,0,1,1,1,1],  
			[1,1,1,1,0,0,0,0,0,0,0,1,1,6,1],  
			[1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],  
			[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],  
			]

		bridge_positions = []
		switch_bridge_dict = {}
		split_port_dest_dict = {}

		start_position = ( (3,1),(3,1) )
		start_bridge_status = ()

		stage_3_map = Map()
		stage_3_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_3_problem = Bloxorz(stage_3_map)
		initial_state = (start_position, start_bridge_status)
		stage_3_problem.set_initial_state(initial_state)

		return stage_3_problem

	def create_stage_4(self):
		map_matrix = [
			[0,0,0,2,2,2,2,2,2,2,0,0,0,0],
			[0,0,0,2,2,2,2,2,2,2,0,0,0,0],
			[1,1,1,1,0,0,0,0,0,1,1,1,0,0],
			[1,1,1,0,0,0,0,0,0,0,1,1,0,0],
			[1,1,1,0,0,0,0,0,0,0,1,1,0,0],
			[1,1,1,0,0,1,1,1,1,2,2,2,2,2],
			[1,1,1,0,0,1,1,1,1,2,2,2,2,2],
			[0,0,0,0,0,1,6,1,0,0,2,2,1,2],
			[0,0,0,0,0,1,1,1,0,0,2,2,2,2],
		]
		bridge_positions = []
		switch_bridge_dict = {}
		split_port_dest_dict = {}
		start_position = ((5,1), (5,1))
		start_bridge_status = ()

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_5(self):
		map_matrix = [	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
						[0, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1],
						[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
						[0, 1, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						[0, 0, 0, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 0, 0],
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 4],
						[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
						[1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
						[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

		bridge_positions = [(1,5),(1,6),(5,8),(5,9),(8,5),(8,6)]
		switch_bridge_dict = {
				(1,8) : [ (0,0), (1,0) ],
				(3,3) : [ (4,1), (5,1) ],
				(5,6) : [ (4,-1), (5,-1) ],
				(6,14): [ (4,0), (5,0) ]
		}
		split_port_dest_dict = {}
		start_position = ((1,13), (1,13))
		start_bridge_status = (1,1,1,1,1,1)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_6(self):
		map_matrix = [
			[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
			[0,0,0,0,0,1,0,0,1,1,1,0,0,0,0],
			[0,0,0,0,0,1,0,0,1,1,1,1,1,0,0],
			[1,1,1,1,1,1,0,0,0,0,0,1,1,1,1],
			[0,0,0,0,1,1,1,0,0,0,0,1,1,6,1],
			[0,0,0,0,1,1,1,0,0,0,0,0,1,1,1],
			[0,0,0,0,0,0,1,0,0,1,1,0,0,0,0],
			[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
			[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
			[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0],
		]
		bridge_positions = []
		switch_bridge_dict = {}
		split_port_dest_dict = {}
		start_position = ((3,0), (3,0))
		start_bridge_status = ()

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_7(self):
		map_matrix = [
			[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0],
			[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0],
			[1,1,1,0,0,0,0,0,1,0,0,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,0,0,0,1,6,1],
			[1,1,1,0,0,0,0,1,1,3,0,0,1,1,1],
			[1,1,1,0,0,0,0,1,1,1,0,0,1,1,1],
			[0,1,1,0,0,0,0,1,0,0,0,0,0,0,0],
			[0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
		]
		bridge_positions = [(6,3)]
		switch_bridge_dict = {
			(4,9)	: [(0,0)],
		}
		split_port_dest_dict = {}
		start_position = ((3,1), (3,1))
		start_bridge_status = tuple([0])

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_8(self):
		map_matrix = [
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
			[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
			[1, 1, 1, 1, 5, 1, 0, 0, 0, 1, 1, 1, 1, 6, 1],
			[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
		]

		bridge_positions = []
		switch_bridge_dict = {}
		split_port_dest_dict = {
			(4,4) : [ (1,10), (7,10) ]
		}
		start_position = ( (4,1), (4,1) )
		start_bridge_status = ()

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_9(self):
		map_matrix = [
			[1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
			[1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 5, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[0, 0, 0, 0, 0, 0, 1, 6, 1, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		]

		bridge_positions = []
		switch_bridge_dict = {}
		split_port_dest_dict = {
			(1,13) : [ (1,2), (1,12) ]
		}
		start_position = ( (1,1), (1,1) )
		start_bridge_status = ()

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_10(self):
		map_matrix = [
			[1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
			[1, 6, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 5, 1],
			[1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
			[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
			[0, 0, 0, 0, 1, 4, 0, 0, 1, 1, 1, 3, 1, 0],
		]

		bridge_positions = [ (1,3), (1,4), (1,6), (1,7), (2,12), (3,12) ]
		switch_bridge_dict = {
			(9,5) 	: [ (0,0), (1,0) ],
			(9,11) 	: [ (2,0), (3,0), (4,0), (5,0) ]
		}
		split_port_dest_dict = {
			(1,12) : [ (1,9), (1,12) ]
		}
		start_position = ( (1,9), (1,9) )
		start_bridge_status = (0, 0, 0, 0, 0, 0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_11(self):
		map_matrix = [
			[0,1,1,1,1,0,0,0,0,0,0,0],
			[0,1,6,1,1,0,0,0,0,0,0,0],
			[0,1,1,1,0,0,0,0,0,0,0,0],
			[0,1,0,0,0,1,1,1,1,1,1,0],
			[0,1,0,0,0,1,1,0,0,1,1,0],
			[1,1,1,1,1,1,1,0,0,1,1,1],
			[0,0,0,0,0,1,4,0,0,0,0,1],
			[0,0,0,0,0,1,1,1,1,0,0,1],
			[0,0,0,0,0,1,1,1,1,1,1,1],
			[0,0,0,0,0,0,0,0,1,1,1,0],
		]

		bridge_positions = [ (0,4), (1,4) ]
		switch_bridge_dict = {
			(6,6) 	: [ (0,-1), (1,-1) ],
		}
		split_port_dest_dict = {}
		start_position = ( (5,0), (5,0) )
		start_bridge_status = (1,1)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_12(self):
		map_matrix = [
			[0,0,0,0,0,0,0,0,0,0,0,0,3],
			[0,0,0,0,0,1,1,1,0,0,1,1,1],
			[0,0,0,0,0,1,3,1,1,1,1,1,0],
			[0,0,0,1,1,1,1,1,0,0,1,1,0],
			[0,0,0,1,6,1,0,0,0,0,1,1,0],
			[0,1,1,1,1,1,0,0,0,1,1,1,1],
			[1,1,1,1,0,0,0,0,0,1,1,1,1],
			[1,1,1,1,0,0,1,1,1,1,1,0,0],
			[0,0,0,0,0,1,1,1,0,0,0,0,0],
			[0,0,0,0,0,1,1,1,0,0,0,0,0],
		]

		bridge_positions = [ (2,12), (4,6) ]
		switch_bridge_dict = {
			(2,6) 	: [ (0,0) ],
			(0,12)	: [ (1,0) ]
		}
		split_port_dest_dict = {}
		start_position = ( (6,2), (6,2) )
		start_bridge_status = (0,0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_13(self):
		map_matrix = [
			[1,1,1,2,1,1,1,1,2,1,1,1,1,0],
			[1,1,0,0,0,0,0,0,0,0,0,1,1,0],
			[1,1,0,0,0,0,0,0,0,0,0,1,1,1],
			[1,1,1,0,0,0,1,1,1,0,0,1,1,1],
			[1,1,1,2,2,2,1,6,1,0,0,1,1,1],
			[1,1,1,0,0,2,1,1,1,0,0,1,0,0],
			[0,0,1,0,0,2,2,2,2,2,1,1,0,0],
			[0,0,1,1,1,2,2,1,2,2,2,0,0,0],
			[0,0,0,1,1,2,2,2,2,2,2,0,0,0],
			[0,0,0,1,1,1,0,0,1,1,0,0,0,0]
		]

		bridge_positions = []
		switch_bridge_dict = {}
		split_port_dest_dict = {}
		start_position = ( (3,12), (3,12) )
		start_bridge_status = ()

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_14(self):
		map_matrix = [
			[0,0,0,0,0,0,0,0,1,1,1,0,0,0],
			[0,0,0,1,1,1,0,0,1,1,1,0,0,0],
			[1,0,0,1,1,1,1,1,1,1,1,1,1,1],
			[1,0,0,1,1,1,0,0,0,0,0,0,3,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,1,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,1,1],
			[1,0,0,0,0,0,0,0,1,1,1,1,1,1],
			[1,1,1,1,1,0,0,0,1,1,1,0,0,0],
			[0,1,1,6,1,0,0,0,1,1,1,0,0,0],
			[0,0,1,1,1,0,0,0,1,1,1,1,1,3],
		]

		bridge_positions = [ (2,1), (2,2), (3,1), (3,2) ]
		switch_bridge_dict = {
			(3,12) 	: [ (0,0), (1,0) ],
			(9,13)	: [ (2,0), (3,0) ]
		}
		split_port_dest_dict = {}
		start_position = ( (2,4), (2,4) )
		start_bridge_status = (0,0,0,0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_15(self):
		map_matrix = [
			[0,0,0,0,0,0,0,1,1,1,0,0,1,1,1],
			[0,0,0,0,1,1,1,1,1,1,0,0,3,1,1],
			[1,1,0,0,1,0,0,1,1,1,0,0,1,1,1],
			[1,1,1,1,1,0,0,0,4,0,0,0,0,0,0],
			[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,5,0,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
			[1,1,1,0,0,0,1,1,1,0,0,4,1,1,0],
			[1,1,1,1,1,1,1,1,1,1,1,1,6,1,0],
			[1,1,1,0,0,0,1,1,1,0,0,4,1,1,0],
		]

		bridge_positions = [ (1,5), (1,6), (1,10), (1,11), (8,9), (8,10), (2,2), (2,3) ]
		switch_bridge_dict = {
			(3,8) 	: [ (0,0), (1,0), (2,0), (3,0) ],
			(1,12)	: [ (0,0), (1,0), (6,0), (7,0) ],
			(7,11)	: [ (4,-1), (5,-1) ],
			(9,11)	: [ (4,-1), (5,-1) ],
		}
		split_port_dest_dict = {
			(5,7)	: [ (1,13), (8,1) ],
		}
		start_position = ( (8,1), (8,1) )
		start_bridge_status = (1,1,0,0,1,1,0,0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_16(self):
		map_matrix = [
			[0,5,0,0,0,0,0,0,0,0,1,1,1],
			[5,1,5,0,0,3,3,1,0,0,1,6,1],
			[0,5,0,0,0,0,0,0,0,0,1,1,1],
			[0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,1,1,1,0,0,0,1,1,1,0,0],
			[0,0,1,1,1,1,1,1,1,5,1,0,0],
			[0,0,1,1,1,0,0,0,1,1,1,0,0],
		]

		bridge_positions = [ (1,3), (1,4), (1,8), (1,9) ]
		switch_bridge_dict = {
			(1,5) 	: [ (0,1), (1,1) ],
			(1,6)	: [ (2,1), (3,1) ],
		}
		split_port_dest_dict = {
			(1,0)	: [ (0,1), (1,2) ],
			(0,1)	: [ (1,5), (1,7) ],
			(2,1)	: [ (1,0), (2,1) ],
			(1,2)	: [ (1,0), (1,2) ],
			(6,9)	: [ (1,0), (0,1) ],
		}
		start_position = ( (6,3), (6,3) )
		start_bridge_status = (0,0,0,0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_17(self):
		map_matrix = [
			[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
			[1,1,1,1,1,1,1,1,1,0,0,0,1,1,1],
			[1,1,1,0,0,0,0,0,1,1,1,1,1,6,1],
			[1,1,1,0,0,0,0,0,0,0,0,0,3,3,1],
			[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
			[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
			[1,1,1,0,0,0,0,1,1,1,1,1,3,0,0],
			[1,1,1,1,1,1,1,1,0,0,0,1,1,0,0],
			[1,4,1,0,0,0,0,0,0,0,0,1,1,0,0],
			[1,1,1,0,0,0,0,0,0,0,0,1,3,0,0],
		]

		bridge_positions = [(7,8), (2, 7), (1, 9),(6,6)]
		switch_bridge_dict = {
			(8, 1) 	: [(0,0)],
			(6, 12)	: [(1,1)],
			(9, 12)	: [(0,-1),(2,1)],
			(3,12):[(3,-1)],
			(3,13):[(3,1)]
		}
		split_port_dest_dict = {}
		start_position = ((1, 1), (1, 1))
		start_bridge_status = (0, 0, 0, 0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions,
		                  switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem
	def create_stage_18(self):
		map_matrix = [
			[0,0,0,0,0,0,0,4,0,0,0,0,0,0,0],
			[1,1,4,1,0,0,0,1,0,0,0,0,0,0,0],
			[1,1,1,1,1,0,0,1,0,0,0,0,0,0,0],
			[1,4,1,1,1,1,1,1,0,0,1,1,0,0,1],
			[1,1,1,1,1,0,0,0,1,0,0,0,1,0,0],
			[1,1,4,1,0,0,0,0,1,0,0,0,1,0,0],
			[1,0,0,0,0,0,0,0,4,0,0,1,1,1,0],
			[1,0,0,0,0,0,0,0,0,0,1,1,6,1,0],
			[1,0,0,3,0,0,0,0,0,0,1,1,1,1,0],
		]

		bridge_positions = [(3,8), (3, 9), (8,1),(8,2), (3,12),(3,13),(4,5) ]
		switch_bridge_dict = {
			(3,1) 	: [(0,-1),(1,-1)],#
			(1,2)	: [(2,-1),(3,-1),(4,-1),(5,-1)],
			(5,2)	: [(2,-1),(3,-1),(4,-1),(5,-1)],
			(0,7)	: [(0,1),(1,1)],#
			(6,8)	: [(2,1),(3,1),(4,1),(5,1)],#
			(8,3)	: [(6,0)]#

		}
		split_port_dest_dict = {}
		start_position = ((3, 2), (3, 2))
		start_bridge_status = (0, 0, 0, 0, 0, 0, 0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions,
		                  switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_19(self):
		map_matrix = [
			[0,1,1,1,1,1,1,1,1,1,4,1,1,1,1],
			[0,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
			[0,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
			[1,1,1,0,0,1,1,0,0,1,4,1,1,1,1],
			[1,6,1,0,0,1,1,0,0,0,0,0,0,0,0],
			[1,1,1,0,0,1,1,0,0,0,0,0,0,0,0],
			[0,1,1,0,0,1,1,0,0,0,0,0,0,0,0],
			[0,1,1,1,1,1,1,1,1,1,4,1,1,1,0]
		]

		bridge_positions = [(5,7), (5, 8), (9,3),(9,4)]
		switch_bridge_dict = {
			(0, 10) 	: [(0,0),(1,0)],
			(5,10)	: [(2,-1),(3,-1)],
			(9,10)	:[(2,1),(3,1)]
		}
		split_port_dest_dict = {}
		start_position = ((0, 1), (0, 1))
		start_bridge_status = (0, 0, 1, 1)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions,
		                  switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_20(self):
		map_matrix = [
			[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1],
			[0,	0,	1,	1,	1,	0,	0,	1,	1,	1,	0,	0,	1,	1,	1],
			[0,	0,	1,	1,	1,	0,	0,	4,	1,	1,	0,	0,	1,	1,	1],
			[0,	0,	1,	1,	1,	0,	0,	1,	1,	1,	0,	0,	0,	0,	0],
			[0,	0,	1,	4,	1,	0,	0,	5,	1,	4,	0,	0,	0,	0,	0],
			[0,	0,	1,	1,	1,	0,	0,	1,	1,	1,	0,	0,	0,	0,	0],
			[1,	1,	1,	1,	0,	0,	0,	1,	1,	1,	0,	0,	4,	1,	1],
			[1,	4,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1],
			[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	6,	1],
			[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1]
		]

		bridge_positions = [
			(1,5),(1,6),(1,10),(1,11),(6,10),(6,11)]

		switch_bridge_dict = {
			(4,3) : [(0,-1), (1,-1)],
			(4,9) : [(0,-1), (1,-1)],
			(2,7) : [(0,-1), (1,-1)],
		 	(7,1) : [(2,0), (3,0)],
		 	(6,12) : [(4,0), (5,0)]}

		split_port_dest_dict = {
			(4,7) : [ (1,13), (7,13) ]
		};

		start_position = ( (2,8), (2,8) )
		start_bridge_status = (1,1,0,0,0,0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_21(self):
		map_matrix = [
			[0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	0],
			[0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	0,	0,	0,	0,	0],
			[1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
			[1,	1,	1,	1,	1,	1,	0,	0,	1,	0,	0,	0,	0,	0,	0],
			[1,	1,	1,	1,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0],
			[0,	1,	1,	0,	0,	0,	0,	0,	3,	1,	0,	0,	1,	1,	1],
			[0,	0,	1,	0,	0,	0,	0,	0,	3,	1,	1,	1,	1,	6,	1],
			[0,	0,	1,	1,	1,	0,	0,	0,	1,	1,	0,	0,	1,	1,	1],
			[0,	0,	0,	1,	1,	1,	0,	0,	1,	1,	0,	0,	0,	0,	0],
			[0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0]
		]

		bridge_positions = [
			(9,3),(7,5)]

		switch_bridge_dict = {
			(5,8) : [(0,0)],
			(6,8) : [(1,0)]}

		split_port_dest_dict = {};

		start_position = ( (3,1), (3,1) )
		start_bridge_status = (0,0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem


	def create_stage_22(self):
		map_matrix = [
			[0,	0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	1,	1,	1],
			[0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	6,	1],
			[1,	1,	1,	1,	1,	1,	4,	1,	1,	1,	1,	1,	1,	1],
			[1,	1,	1,	1,	4,	0,	0,	1,	1,	1,	1,	1,	0,	0],
			[1,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	1,	0,	0],
			[0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0],
			[0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0],
			[0,	1,	0,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0,	0],
			[0,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0,	0],
			[0,	0,	3,	0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0]
		]

		bridge_positions = [
			(7,2),(3,12),(7,9)]

		switch_bridge_dict = {
			(2,6) : [(0,-1),(1,-1)],
			(3,4) : [(0,-1),(1,-1)],
			(9,9) : [(0,0)],
			(9,2) : [(1,0)]}

		split_port_dest_dict = {};

		start_position = ( (3,1), (3,1) )
		start_bridge_status = (0,0,1)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_23(self):
		map_matrix = [
			[0,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1],
			[0,	1,	3,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	4,	1],
			[0,	1,	1,	1,	0,	0,	0,	1,	1,	1,	0,	0,	1,	1,	1],
			[0,	1,	1,	1,	0,	0,	0,	1,	6,	1,	0,	0,	1,	1,	4],
			[1,	0,	0,	0,	1,	0,	0,	1,	1,	1,	0,	0,	0,	0,	1],
			[4,	0,	0,	0,	1,	0,	0,	2,	2,	2,	0,	0,	0,	0,	1],
			[1,	0,	0,	1,	1,	1,	2,	2,	2,	2,	2,	1,	1,	1,	0],
			[0,	0,	0,	1,	1,	1,	2,	2,	2,	2,	2,	1,	5,	1,	0],
			[0,	0,	0,	1,	1,	1,	2,	2,	2,	2,	2,	1,	1,	1,	0],
			[0,	0,	0,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0]
		]

		bridge_positions = [
			(3,4),(3,0),(2,10),(2,11),(6,14),(6,1),(6,2),(9,8)]

		switch_bridge_dict = {
			(1,2) : [(0,1)],
			(5,0) : [(1,1),(5,-1),(6,-1)],
			(3,14) : [(2,-1),(3,-1),(4,-1)],
			(1,13) : [(5,1),(6,1),(7,0)]}

		split_port_dest_dict = {
			(7,12) : [ (7,12), (2,2) ]
		}
		start_position = ( (7,4),(7,4) )
		start_bridge_status = (0,0,1,1,1,0,0,0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_24(self):
		map_matrix = [
			[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1],
			[0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	3,	1,	5],
			[0,	1,	0,	0,	1,	3,	1,	0,	0,	0,	1,	1,	1,	1],
			[3,	1,	0,	0,	1,	1,	0,	0,	0,	0,	0,	0,	1,	0],
			[1,	1,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	1,	0],
			[1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	1,	1,	1,	0],
			[1,	1,	1,	0,	0,	1,	1,	1,	0,	0,	1,	6,	1,	0],
			[0,	0,	0,	0,	0,	3,	1,	0,	0,	0,	1,	1,	1,	0]
		]

		bridge_positions = [
			(2,2),(2,3),(1,3),(7,7),(6,8),(6,9)]

		switch_bridge_dict = {
			(1,11) : [(0,1),(1,1)],
			(3,0) : [(2,1)],
			(2,5) : [(3,1)],
			(7,5) : [(4,1),(5,1)]}

		split_port_dest_dict = {
			(1,13) : [ (6,5), (6,7) ]
		}
		start_position = ( (2,1),(2,1) )
		start_bridge_status = (0,0,0,0,0,0)

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (start_position, start_bridge_status)
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_29(self):
		stage_29_map_matrix = [
			[0, 0, 4, 1, 1, 1, 0, 0, 0, 1, 0, 0, 3, 0, 0],
			[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
			[3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3],
			[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 4, 0, 0],
			[1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
			[1, 6, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 0, 0],
		]

		stage_29_bridge_positions = [ (0,3), (0,4), (0,10), (0,11), (3,1), (3,2), (3,12), (3,13), (5,5), (6,5), 
								(6,10), (6,11), (8,3), (8,4), (9,3),(9,10), (9,11)  ]

		stage_29_switch_bridge_dict = {
			(0,2) : [(2,1), (3,1) ,(10,-1), (11,-1)],
			(0,12): [(8,1), (9,1)],
			(3,0) : [(12,1), (13,1) ,(15,-1), (16,-1)],
			(3,14): [(14,1)],
			(6,12): [(4,1), (5,1)],
			(9,12): [(0,-1), (1,-1) ,(2,-1), (3,-1), (6,1), (7,1), (10,-1), (11,-1)]}

		stage_29_split_port_dest_dict = {}

		start_position = ( (3,7), (3,7) )
		start_bridge_status = (1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1)

		stage_29_map = Map()
		stage_29_map.set_map(stage_29_map_matrix, stage_29_bridge_positions, stage_29_switch_bridge_dict, stage_29_split_port_dest_dict)

		stage_29_problem = Bloxorz(stage_29_map)
		stage_29_initial_state = ( start_position, start_bridge_status )
		stage_29_problem.set_initial_state(stage_29_initial_state)

		return stage_29_problem

	def create_stage_30(self):
		stage_30_map_matrix = [
			[0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0],
			[0, 0, 0, 1, 6, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0],
			[0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1, 3],
			[0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1],
			[0, 0, 1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
			[0, 3, 1, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
			[2, 2, 2, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
			[2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 0, 0, 3, 1, 0],
			[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
			[0, 2, 1, 2, 2, 2, 0, 0, 2, 2, 2, 2, 1, 0, 0],
		]

		stage_30_bridge_positions = [ (3,10), (3,11), (6,9), (6,12), (7,14) ]

		stage_30_switch_bridge_dict = {
			(2,14) : [(0,-1), (1,-1) ,(2,1), (3,1)],
			(5,1)  : [(0,1), (1,1)],
			(7,12) : [(4,0)]
		}

		stage_30_split_port_dest_dict = {}

		start_position = ( (4,2), (4,2) )
		start_bridge_status = (1,1,0,0,0)

		stage_30_map = Map()
		stage_30_map.set_map(stage_30_map_matrix, stage_30_bridge_positions, stage_30_switch_bridge_dict, stage_30_split_port_dest_dict)

		stage_30_problem = Bloxorz(stage_30_map)
		stage_30_initial_state = ( start_position, start_bridge_status )
		stage_30_problem.set_initial_state(stage_30_initial_state)

		return stage_30_problem

	def create_stage_31(self):
		stage_31_map_matrix = [
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
			[0, 1, 1, 1, 0, 0, 0, 0, 3, 0, 0, 1, 6, 1, 0],
			[0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
			[0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
			[0, 2, 2, 2, 0, 0, 4, 1, 1, 0, 0, 0, 2, 0, 0],
			[0, 0, 2, 0, 0, 0, 1, 1, 1, 0, 0, 2, 2, 2, 0],
			[0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
			[1, 1, 1, 1, 0, 0, 1, 4, 1, 1, 1, 1, 1, 1, 0],
			[1, 1, 3, 1, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1, 0],
			[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		]

		stage_31_bridge_positions = [ (0,14), (1,14), (2,14), (2,4), (2,5), (2,9), (2,10), 
									(7,0), (8,0), (9,0), (7,4), (7,5), (7,9), (7,10) ]

		stage_31_switch_bridge_dict = {
			(1,8) : [ (5,0), (6,0) ],
			(4,6) : [ (3,-1), (4,-1), (5,-1), (6,-1), (10,-1), (11,-1), (12,-1) ,(13,-1) ],
			(7,7) : [ (3,-1), (4,-1) ,(5,-1), (6,-1), (10,-1), (11,-1), (12,-1) ,(13,-1) ],
			(8,2) : [ (0,1), (1,1), (2,1), (3,-1), (4,-1) ],
			(8,6) : [ (10,0), (11,0) ]
		}

		stage_31_split_port_dest_dict = {}

		start_position = ( (7,12), (7,12) )
		start_bridge_status = (0,0,0,1,1,0,0,1,1,1,0,0,1,1)

		stage_31_map = Map()
		stage_31_map.set_map(stage_31_map_matrix, stage_31_bridge_positions, stage_31_switch_bridge_dict, stage_31_split_port_dest_dict)

		stage_31_problem = Bloxorz(stage_31_map)
		stage_31_initial_state = ( start_position, start_bridge_status )
		stage_31_problem.set_initial_state(stage_31_initial_state)

		return stage_31_problem

	def create_stage_32(self):
		stage_32_map_matrix = [
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],
			[0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
			[0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 3, 1, 1],
			[0, 1, 6, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
			[0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
			[1, 1, 0, 0, 1, 3, 1, 0, 0, 1, 1, 0, 0, 0],
			[1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
		]

		stage_32_bridge_positions = [ (1,4), (1,5), (2,4), (2,5), (7,2), (7,3), (8,2), (8,3)]

		stage_32_switch_bridge_dict = {
			(0,13) : [(0,0), (1,0), (4,0), (5,0)],
			(2,11) : [(6,0), (7,0)],
			(7,5) : [(2,0), (3,0)]}

		stage_32_split_port_dest_dict = {}

		start_position = ( (6,10), (6,10) )
		start_bridge_status = (1,1,0,0,0,0,0,0)

		stage_32_map = Map()
		stage_32_map.set_map(stage_32_map_matrix, stage_32_bridge_positions, stage_32_switch_bridge_dict, stage_32_split_port_dest_dict)

		stage_32_problem = Bloxorz(stage_32_map)
		stage_32_initial_state = ( start_position, start_bridge_status )
		stage_32_problem.set_initial_state(stage_32_initial_state)

		return stage_32_problem

	def create_stage_33(self):
		stage_33_map_matrix = [
			[0, 0, 0, 0, 0, 1, 1, 4, 1, 1, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
			[1, 1, 1, 0, 0, 4, 1, 1, 4, 1, 1, 1, 1, 1, 0],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 4, 0],
			[0, 0, 0, 0, 0, 1, 1, 4, 1, 1, 4, 1, 1, 1, 0],
			[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 4, 1, 1, 0],
			[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1],
			[1, 6, 1, 1, 1, 1, 4, 1, 0, 0, 1, 1, 1, 4, 3],
			[1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
		]

		stage_33_bridge_positions = [ (1,11), (3,3), (3,4), (7,3), (7,4)]

		stage_33_switch_bridge_dict = {
			(0,7)   : [(3,-1), (4,-1)],
			(2,5)   : [(3,-1), (4,-1)],
			(2,8)   : [(3,-1), (4,-1)],
			(3,9)   : [(3,-1), (4,-1)],
			(3,10)  : [(3,-1), (4,-1)],
			(3,13)  : [(3,-1), (4,-1)],
			(4,7)   : [(3,-1), (4,-1)],
			(4,10)  : [(3,-1), (4,-1)],
			(5,11)  : [(3,-1), (4,-1)],
			(6,11)  : [(3,-1), (4,-1)],
			(7,6)   : [(3,-1), (4,-1)],
			(7,13)  : [(3,-1), (4,-1)],
			(7,14)  : [(0,1)]}

		stage_33_split_port_dest_dict = {}

		start_position = ( (3,1), (3,1) )
		start_bridge_status = (0,1,1,1,1)

		stage_33_map = Map()
		stage_33_map.set_map(stage_33_map_matrix, stage_33_bridge_positions, stage_33_switch_bridge_dict, stage_33_split_port_dest_dict)

		stage_33_problem = Bloxorz(stage_33_map)
		stage_33_initial_state = ( start_position, start_bridge_status )
		stage_33_problem.set_initial_state(stage_33_initial_state)

		return stage_33_problem

def print_list(list_item):
	for i in range(len(list_item)):
		item = list_item[i]
		print(str(i+1).rjust(3), end='. ')
		if i % 5 == 4: print(item)
		else: print(item.ljust(20), end='')

def print_result(solver, goal_node, running_time):
	if goal_node is None:
		print("Can't solve")
	else:
		actions_list = solver.get_actions_to_goal(goal_node)
		print_list(actions_list)
		print("\n\nNum steps:", len(actions_list))

	print("Visited: ", solver.num_visited_nodes, "node(s)")
	print("Running time:", running_time)

def solve_by_DFS(stage, max_node = 0):
	print('\n####################################')
	print('Depth First Search:')
	print('####################################\n')

	dfs_solver = DepthFirstSearchSolver(stage)
	dfs_solver.set_max_visited_node(max_node)
	start_time = time.time()
	goal_node = dfs_solver.solve()
	finish_time = time.time()
	running_time = finish_time - start_time
	print_result(dfs_solver, goal_node, running_time)

def solve_by_BrFS(stage, max_node = 0):
	print('\n####################################')
	print('Breadth First Search:')
	print('####################################\n')

	brfs_solver = BreadthFirstSearchSolver(stage)
	brfs_solver.set_max_visited_node(max_node)
	start_time = time.time()
	goal_node = brfs_solver.solve()
	finish_time = time.time()
	running_time = finish_time - start_time
	print_result(brfs_solver, goal_node, running_time)

def solve_by_BFS(stage, max_node = 0):
	print('\n####################################')
	print('Best First Search:')
	print('####################################\n')
	bfs_solver = BestFirstSearchSolver(stage)
	bfs_solver.set_max_visited_node(max_node)
	start_time = time.time()
	goal_node = bfs_solver.solve()
	finish_time = time.time()
	running_time = finish_time - start_time
	print_result(bfs_solver, goal_node, running_time)

####################################
# MAIN
####################################
def main():

	num_stage = int(input("Enter stage: "))
	max_node = 700000

	bloxorz_creator = BloxorzCreator()
	stage = bloxorz_creator.create_stage(num_stage)
	stage.draw_map()
	
	# solve_by_DFS(stage, max_node)
	# solve_by_BrFS(stage, max_node)
	solve_by_BFS(stage, max_node)

if __name__ == '__main__':
	main()
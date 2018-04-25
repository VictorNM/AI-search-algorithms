from bloxorz import *

####################################
# CREATE STAGES
####################################
class BloxorzCreator(object):
	
	def create_stage(self, stage_number):
		return {
			2 	: self.create_stage_2,
			3 	: self.create_stage_3,
			5 	: self.create_stage_5,
			8 	: self.create_stage_8,
			9 	: self.create_stage_9,
			10	: self.create_stage_10,
			11	: self.create_stage_11,

			20	: self.create_stage_20,
			21	: self.create_stage_21,
			22	: self.create_stage_22,
			23	: self.create_stage_23,
			24	: self.create_stage_24
		}[stage_number]()

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
			[0,0,0,0,0,1,2,0,0,0,0,1],
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
			(4,3) : [(0,1), (1,1)],
			(4,9) : [(0,1), (1,1)],
			(2,7) : [(0,1), (1,1)],
		 	(7,1) : [(2,0), (3,0)],
		 	(6,12) : [(4,0), (5,0)]}

		split_port_dest_dict = {};

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
			(7,2),(3,12)]

		switch_bridge_dict = {
			(2,6) : [(0,1),(1,1)],
			(3,4) : [(0,1),(1,1)],
			(9,9) : [(0,0)],
			(9,2) : [(1,0)]}

		split_port_dest_dict = {};

		start_position = ( (3,1), (3,1) )
		start_bridge_status = (0,0)

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
			(3,4),(3,0),(2,10),(2,11),(8,14),(6,1),(6,2),(9,8)]

		switch_bridge_dict = {
			(1,2) : [(0,-1)],
			(5,0) : [(1,-1),(5,1),(6,1)],
			(3,14) : [(2,1),(3,1),(4,1)],
			(1,13) : [(5,-1),(6,-1),(7,0)]}

		split_port_dest_dict = {
			(7,12) : [ (7,12), (2,2) ]
		}
		start_position = ( (7,4),(7,4) )
		start_bridge_status = (0,0,0,0,0,0,0,0)

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
			(1,11) : [(0,-1),(1,-1)],
			(3,0) : [(2,-1)],
			(2,5) : [(3,-1)],
			(7,5) : [(4,-1),(5,-1)]}

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

####################################
# MAIN
####################################
def main():

	num_stage = int(input("Enter stage: "))
	max_node = 0


	bloxorz_creator = BloxorzCreator()
	stage = bloxorz_creator.create_stage(num_stage)
	stage.draw_map()
	# stage_2 = bloxorz_creator.create_stage(2)
	# stage_3 = bloxorz_creator.create_stage(3)
	# stage_5 = bloxorz_creator.create_stage(5)

	print('\n####################################')
	print('Depth First Search:')
	print('####################################\n')
	dfs_solver = DepthFirstSearchSolver(stage)
	dfs_solver.set_max_visited_node(max_node)
	goal_node = dfs_solver.solve()
	solution_path = dfs_solver.trace_back(goal_node)
	# # stage.print_movement(solution_path)
	print("Visited: ", dfs_solver.num_visited_nodes, "node(s)")
	print("Num steps: ", len(solution_path) - 1)

	# print('\n####################################')
	# print('Breadth First Search:')
	# print('####################################\n')
	# brfs_solver = BreadthFirstSearchSolver(stage)
	# brfs_solver.set_max_visited_node(max_node)
	# goal_node = brfs_solver.solve()
	# solution_path = brfs_solver.trace_back(goal_node)
	# # # print(solution_path)
	# # stage.print_movement(solution_path)
	# print("Visited: ", brfs_solver.num_visited_nodes, "node(s)")
	# print("Num steps: ", len(solution_path) - 1)

	print('\n####################################')
	print('Best First Search:')
	print('####################################\n')
	bfs_solver = BestFirstSearchSolver(stage)
	bfs_solver.set_max_visited_node(max_node)
	goal_node = bfs_solver.solve()
	solution_path = bfs_solver.trace_back(goal_node)
	# print(solution_path)
	stage.print_movement(solution_path)
	for step in solution_path:
		print(step[0])
	print("Visited: ", bfs_solver.num_visited_nodes, "node(s)")
	if solution_path is not None:
		print("Num steps: ", len(solution_path) - 1)
	else:
		print('Cannot solve')

	# print('\n####################################')
	# print('Simulated Annealing:')
	# print('####################################\n')
	# sa_solver = SimulatedAnnealing(stage)
	# sa_solver.set_max_visited_node(max_node)
	# goal_node = sa_solver.solve()
	# solution_path = sa_solver.trace_back(goal_node)
	# # print(solution_path)
	# # stage.print_movement(solution_path)
	# # for step in solution_path:
	# # 	print(step[0])
	# print("Visited: ", sa_solver.num_visited_nodes, "node(s)")
	# if solution_path is not None:
	# 	print("Num steps: ", len(solution_path) - 1)
	# else:
	# 	print('Cannot solve')

if __name__ == '__main__':
	main()
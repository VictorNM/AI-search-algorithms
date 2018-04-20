from bloxorz import *

####################################
# CREATE STAGES
####################################
class BloxorzCreator(object):
	
	def create_stage(self, stage_number):
		return {
			2 : self.create_stage_2,
			3 : self.create_stage_3,
			5 : self.create_stage_5,
			8 : self.create_stage_8,
		}[stage_number]()

	def create_stage_2(self):
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

		stage_2_split_port_dest_dict = {};

		stage_2_map = Map()
		stage_2_map.set_map(stage_2_map_matrix, stage_2_bridge_positions, stage_2_switch_bridge_dict, stage_2_split_port_dest_dict)

		stage_2_problem = Bloxorz(stage_2_map)
		stage_2_initial_state = ( ((4,1), (4,1)), (Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT) )
		stage_2_problem.set_initial_state(stage_2_initial_state)

		return stage_2_problem

	def create_stage_3(self):
		map_matrix = [
			[Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.EMPT,Square.EMPT],  
			[Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.EMPT,Square.EMPT,Square.H_TI,Square.H_TI,Square.H_TI,Square.EMPT,Square.EMPT,Square.H_TI,Square.H_TI,Square.EMPT,Square.EMPT],  
			[Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.EMPT,Square.EMPT,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI],  
			[Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.H_TI,Square.H_TI,Square.GOAL,Square.H_TI],  
			[Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI],  
			[Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.EMPT,Square.H_TI,Square.H_TI,Square.H_TI],  
			]

		bridge_positions = []
		switch_bridge_dict = {}
		split_port_dest_dict = {}

		stage_3_map = Map()
		stage_3_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_3_problem = Bloxorz(stage_3_map)
		initial_state = (((3,1),(3,1)),())
		stage_3_problem.set_initial_state(initial_state)

		return stage_3_problem

	def create_stage_5(self):
		map_matrix = [	[Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI],
						[Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.S_SW, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI],
						[Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI],
						[Square.EMPT, Square.H_TI, Square.H_TI, Square.S_SW, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT],
						[Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT],
						[Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.S_SW, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT],
						[Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.S_SW],
						[Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI],
						[Square.H_TI, Square.GOAL, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT],
						[Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT]]

		bridge_positions = [(1,5),(1,6),(5,8),(5,9),(8,5),(8,6)]
		switch_bridge_dict = {
				(1,8) : [(0,0), (1,0)],
				(3,3) : [(4,1), (5,1)],
				(5,6) : [(4,-1), (5,-1)],
				(6,14): [(4,0), (5,0)]}
		split_port_dest_dict = {}

		stage_map = Map()
		stage_map.set_map(map_matrix, bridge_positions, switch_bridge_dict, split_port_dest_dict)

		stage_problem = Bloxorz(stage_map)
		initial_state = (
			((1,13),(1,13)),
			(Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI,Square.H_TI))
		stage_problem.set_initial_state(initial_state)

		return stage_problem

	def create_stage_8(self):
		map_matrix = [	[Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT],
						[Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT],
						[Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT],
						[Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI],
						[Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.SPLI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.GOAL, Square.H_TI],
						[Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI, Square.H_TI],
						[Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT],
						[Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT],
						[Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.EMPT, Square.H_TI, Square.H_TI, Square.H_TI, Square.EMPT, Square.EMPT, Square.EMPT]]

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

####################################
# MAIN
####################################
def main():

	num_stage = int(input("Enter stage: "))

	bloxorz_creator = BloxorzCreator()
	stage = bloxorz_creator.create_stage(num_stage)
	# stage_2 = bloxorz_creator.create_stage(2)
	# stage_3 = bloxorz_creator.create_stage(3)
	# stage_5 = bloxorz_creator.create_stage(5)

	# print('\n####################################')
	# print('Depth First Search:')
	# print('####################################\n')
	# dfs_solver = DepthFirstSearchSolver(stage)
	# goal_node = dfs_solver.solve()
	# # print(dfs_solver.trace_back(goal_node))
	# solution_path = dfs_solver.trace_back(goal_node)
	# # print_movement(solution_path)
	# print("Visited: ", dfs_solver.num_visited_nodes, "node(s)")
	# print("Num steps: ", len(solution_path) - 1)

	# print('\n####################################')
	# print('Breadth First Search:')
	# print('####################################\n')
	# brfs_solver = BreadthFirstSearchSolver(stage)
	# goal_node = brfs_solver.solve()
	# solution_path = brfs_solver.trace_back(goal_node)
	# # print(solution_path)
	# # print_movement(solution_path)
	# print("Visited: ", brfs_solver.num_visited_nodes, "node(s)")
	# print("Num steps: ", len(solution_path) - 1)

	print('\n####################################')
	print('Best First Search:')
	print('####################################\n')
	bfs_solver = BestFirstSearchSolver(stage)
	goal_node = bfs_solver.solve()
	solution_path = bfs_solver.trace_back(goal_node)
	# print(solution_path)
	stage.print_movement(solution_path)
	print("Visited: ", bfs_solver.num_visited_nodes, "node(s)")
	print("Num steps: ", len(solution_path) - 1)

if __name__ == '__main__':
	main()
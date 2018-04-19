from bloxorz import *

####################################
# CREATE STAGES
####################################
class BloxorzCreator(object):
	
	def create_stage(self, stage_number):
		return {
			2 : self.create_stage_2,
			3 : self.create_stage_3,
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
		stage_2_initial_state = ( ((4,1), (4,1)), (0,0,0,0) )
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

def print_movement(state_path):
	for i in range(1, len(state_path)):
		pair_position_prev = state_path[i-1][0]
		pair_position_now = state_path[i][0]
		(row_prev, col_prev) = pair_position_prev[0]
		(row_now, col_now) = pair_position_now[0]

		if row_now < row_prev: print('UP')
		elif row_now > row_prev: print('DOWN')
		elif col_now < col_prev: print('LEFT')
		elif col_now > col_prev: print('RIGHT')

####################################
# MAIN
####################################
def main():

	bloxorz_creator = BloxorzCreator()
	stage_2 = bloxorz_creator.create_stage(2)
	stage_3 = bloxorz_creator.create_stage(3)

	print('DFS:')
	dfs_solver = DepthFirstSearchSolver(stage_3)
	goal_node = dfs_solver.solve()
	# print(dfs_solver.trace_back(goal_node))
	solution_path = dfs_solver.trace_back(goal_node)
	print_movement(solution_path)
	print("Visited: ", dfs_solver.num_visited_nodes, "node(s)")

	print('BrFS:')
	brfs_solver = BreadthFirstSearchSolver(stage_3)
	goal_node = brfs_solver.solve()
	# print(brfs_solver.trace_back(goal_node))
	solution_path = brfs_solver.trace_back(goal_node)
	print_movement(solution_path)
	print("Visited: ", brfs_solver.num_visited_nodes, "node(s)")

	print('BFS:')
	bfs_solver = BestFirstSearchSolver(stage_3)
	goal_node = bfs_solver.solve()
	solution_path = bfs_solver.trace_back(goal_node)
	print_movement(solution_path)
	print("Visited: ", bfs_solver.num_visited_nodes, "node(s)")

if __name__ == '__main__':
	main()
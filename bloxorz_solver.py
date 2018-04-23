from bloxorz import *
import time

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
			12	: self.create_stage_12,
			14	: self.create_stage_14,
			15	: self.create_stage_15,
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

def print_list(list_item):
	for i in range(len(list_item)):
		item = list_item[i]
		print(str(i+1).rjust(3), end='. ')
		if i % 5 == 4: print(item)
		else: print(item.ljust(20), end='')

def solve_by_DFS(stage, max_node = 0):
	print('\n####################################')
	print('Depth First Search:')
	print('####################################\n')

	dfs_solver = DepthFirstSearchSolver(stage)
	dfs_solver.set_max_visited_node(max_node)
	start_time = time.time()
	goal_node = dfs_solver.solve()
	finish_time = time.time()
	actions_list = dfs_solver.get_actions_to_goal(goal_node)
	
	print(actions_list)
	print("Visited: ", dfs_solver.num_visited_nodes, "node(s)")
	print("Running time:", finish_time - start_time)
	print("Num steps: ", len(actions_list))

def solve_by_BrFS(stage, max_node = 0):
	print('\n####################################')
	print('Breadth First Search:')
	print('####################################\n')

	brfs_solver = BreadthFirstSearchSolver(stage)
	brfs_solver.set_max_visited_node(max_node)
	start_time = time.time()
	goal_node = brfs_solver.solve()
	finish_time = time.time()
	actions_list = brfs_solver.get_actions_to_goal(goal_node)

	print_list(actions_list)
	print("Visited: ", brfs_solver.num_visited_nodes, "node(s)")
	print("Running time:", finish_time - start_time)
	print("Num steps: ", len(actions_list))

def solve_by_BFS(stage, max_node = 0):
	print('\n####################################')
	print('Best First Search:')
	print('####################################\n')
	bfs_solver = BestFirstSearchSolver(stage)
	bfs_solver.set_max_visited_node(max_node)
	start_time = time.time()
	goal_node = bfs_solver.solve()
	finish_time = time.time()
	actions_list = bfs_solver.get_actions_to_goal(goal_node)

	# print_list(actions_list)
	print_list(actions_list)
	print()
	print("Visited: ", bfs_solver.num_visited_nodes, "node(s)")
	print("Running time:", finish_time - start_time)
	print("Num steps: ", len(actions_list))

####################################
# MAIN
####################################
def main():

	num_stage = int(input("Enter stage: "))
	max_node = 0

	bloxorz_creator = BloxorzCreator()
	stage = bloxorz_creator.create_stage(num_stage)
	stage.draw_map()
	
	# solve_by_DFS(stage, max_node)
	# solve_by_BrFS(stage, max_node)
	solve_by_BFS(stage, max_node)

if __name__ == '__main__':
	main()
###############################
# CREATED BY: NGUYEN MAU VINH
# STUDENT ID: 1627058
###############################

# === CLASS PROBLEM ===
class Problem:
	"""root class for any problem"""
	def __init__(self, initial_state = None):
		self.initial_state = initial_state

	def set_initial_state(self, initial_state):
		self.initial_state = initial_state

	def is_goal_state(self, state):
		pass

	def get_all_actions_results(self, current_state):
		action_result_list = []
		return action_result_list

	def generate_next_states(self, current_state):
		next_states = []
		return next_states

	def get_heuristic_rank(self, state):
		return 0

# === CLASS NODE ===
class Node:
	def __init__(self, state = None, parent = None, children = None, depth = None, action = None, path_cost = None):
		self.state = state
		self.parent = parent
		self.action = ''

		if children is not None: self.children = children
		else: self.children = []

		if depth is not None: self.depth = depth
		else: self.depth = 0

		if action is not None: self.action = action
		else: action = ''

		self.path_cost = path_cost

	def add_child(self, child):
		child.parent = self
		child.depth = self.depth + 1
		self.children.append(child)

	def __str__(self):
		return str(self.state)

	def __lt__(self, other):
		return True

# === CLASS SOLVER ===
class Solver:
	def __init__(self, problem = None):
		self._problem = problem
		self._current_node = None
		self.num_visited_nodes = 0
		self._max_visited_node = 0

	def set_problem(self, problem):
		self._problem = problem

	def set_max_visited_node(self, max_visited_node):
		self._max_visited_node = max_visited_node

	def solve(self):
		if self._has_set_initial_state():
			print("Oops, you forgot to set initial state")
			return None
		return self._process()

	def _process(self):
		pass

	def _has_set_initial_state(self):
		return self._problem.initial_state is None

	def _is_solution(self, node):
		return self._problem.is_goal_state(node.state)

class SearchSolver(Solver):
	def __init__(self, problem):
		super(SearchSolver, self).__init__(problem)
		self._open_list = None
		self._closed_set = set()
		
	def _process(self):
		return self._search_tree()

	def _search_tree(self):
		initial_node = Node(state = self._problem.initial_state)
		self._put_to_open_list(initial_node)

		while not self._is_empty_open_list():
			self._current_node = self._get_from_open_list()
			self._put_to_closed_set(self._current_node.state)
			self.num_visited_nodes += 1
			if self.num_visited_nodes > 350000 and self.num_visited_nodes % 10000 == 0:
				print(self.num_visited_nodes)
			
			if self._is_solution(self._current_node):
				return self._current_node

			# reach the limit
			if self.num_visited_nodes == self._max_visited_node:
				return None

			children_nodes = self.expand_children_of_current_node()
			# get nodes that satisfy the algorithm
			satisfying_nodes = self._get_satisfying_nodes(children_nodes)
			for node in satisfying_nodes:
				self._put_to_open_list(node)

		return None

	def expand_children_of_current_node(self):
		action_result_list = self._problem.get_all_actions_results(self._current_node.state)

		for (action, result) in action_result_list:
			new_node = Node(state = result, action = action)
			self._current_node.add_child(new_node)

		# next_states = self._problem.generate_next_states(self._current_node.state)

		# for state in next_states:
		# 	new_node = Node(state = state)
		# 	self._current_node.add_child(new_node)

		return self._current_node.children

	def _put_to_open_list(self, node):
		pass

	def _is_empty_open_list(self):
		pass

	def _get_from_open_list(self):
		pass

	def _put_to_closed_set(self, state):
		self._closed_set.add(state)

	def _get_satisfying_nodes(self, list_of_nodes):
		return list_of_nodes

	def trace_back(self, node):
		if node is None: return None

		solution_path = []
		current_node = node
		solution_path.append(current_node)

		while current_node.parent is not None:
			current_node = current_node.parent
			solution_path.insert(0, current_node)

		return solution_path

	def get_solution_path(self, node):
		solution_path = []
		for node in self.trace_back(node):
			if node.action != '':
				solution_path.append(node.state)
		return solution_path

	def get_actions_to_goal(self, node):
		action_list = []
		for node in self.trace_back(node):
			if node.action != '':
				# print(node.action, '\t:', node.state)
				action_list.append(node.action)
		return action_list

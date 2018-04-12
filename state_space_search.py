###############################
# CREATED BY: NGUYEN MAU VINH
# STUDENT ID: 1627058
###############################

from solver import *

class DepthFirstSearchSolver(SearchSolver):
	def __init__(self, problem):
		super(DepthFirstSearchSolver, self).__init__(problem)
		self._open_list = []
		self._closed_set = set()
		
	def _put_to_open_list(self, node):
		self._open_list.append(node)

	def _is_empty_open_list(self):
		return len(self._open_list) == 0

	def _get_from_open_list(self):
		return self._open_list.pop()

	# check if node was processed, avoid infinite loop
	def _get_satisfying_nodes(self, list_of_nodes):	
		satisfying_nodes = [node
							for node in list_of_nodes
							if node.state not in self._closed_set]

		return satisfying_nodes


class BreadthFirstSearchSolver(SearchSolver):
	def __init__(self, problem):
		super(BreadthFirstSearchSolver, self).__init__(problem)
		self._open_list = []
		self._closed_set = set()

	def _put_to_open_list(self, node):
		self._open_list.append(node)

	def _is_empty_open_list(self):
		return len(self._open_list) == 0

	def _get_from_open_list(self):
		return self._open_list.pop(0)

	# similar to DFS, but not for avoid inifite loop, it is used to search faster
	# def _get_satisfying_nodes(self, list_of_nodes):	
	# 	satisfying_nodes = [node
	# 						for node in list_of_nodes
	# 						if node.state not in self._closed_set]

	# 	return satisfying_nodes
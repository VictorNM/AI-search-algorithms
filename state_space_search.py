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
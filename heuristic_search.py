###############################
# CREATED BY: NGUYEN MAU VINH
# STUDENT ID: 1627058
###############################

from solver import *
from queue import PriorityQueue
import time
import random
import math

class BestFirstSearchSolver(SearchSolver):
	def __init__(self, problem):
		super(BestFirstSearchSolver, self).__init__(problem)
		self._open_list = PriorityQueue()
		self._closed_set = set()

	def _put_to_open_list(self, node):
		priority = self._problem.get_heuristic_rank(node.state)
		self._open_list.put((priority, -time.time(), node))

	def _is_empty_open_list(self):
		return self._open_list.qsize() == 0

	def _get_from_open_list(self):
		return self._open_list.get()[2]


class HillClimbingSolver(SearchSolver):
	def __init__(self, problem):
		super(HillClimbingSolver, self).__init__(problem)
		self._open_list = []
		self._closed_set = set()

	def _put_to_open_list(self, node):
		self._open_list.append(node)

	def _is_empty_open_list(self):
		return len(self._open_list) == 0

	def _get_from_open_list(self):
		return self._open_list.pop(0)

	def _get_satisfying_nodes(self, list_of_nodes):	
		satisfying_nodes = []

		current_rank = self._problem.get_heuristic_rank(self._current_node.state)
		for node in list_of_nodes:			
			new_rank = self._problem.get_heuristic_rank(node.state)
			if new_rank < current_rank:
				satisfying_nodes.append(node)
				break;

		return satisfying_nodes
						

class SteepestAscentHillClimbingSolver(HillClimbingSolver):
	def __init__(self, problem):
		super(SteepestAscentHillClimbingSolver, self).__init__(problem)

	def _get_satisfying_nodes(self, list_of_nodes):	
		satisfying_nodes = []
		current_rank = self._problem.get_heuristic_rank(self._current_node.state)
		best_node = self._current_node
		best_rank = current_rank
		for node in list_of_nodes:
			new_rank = self._problem.get_heuristic_rank(node.state)
			if new_rank < best_rank:
				best_node = node
				best_rank = new_rank

		if best_rank < current_rank:
			satisfying_nodes.append(best_node)
		return satisfying_nodes


class SimulatedAnnealing(HillClimbingSolver):
	def __init__(self, problem):
		super(SimulatedAnnealing, self).__init__(problem)

	def _get_satisfying_nodes(self, list_of_nodes):
		if self._max_visited_node <= 0:
			print('Error: you must set limit node to use this algorimth')
			return []

		satisfying_nodes = []

		new_node = random.choice(list_of_nodes)
		current_rank = self._problem.get_heuristic_rank(self._current_node.state)
		new_rank = self._problem.get_heuristic_rank(new_node.state)
		
		delta_E = new_rank - current_rank
		if delta_E < 0:	# new_rank is better
			satisfying_nodes.append(new_node)
		else:
			T = self._max_visited_node - self.num_visited_nodes
			p = math.exp(-delta_E / T)
			print(p)
			if random.random() < p: satisfying_nodes.append(new_node)
			else: satisfying_nodes.append(self._current_node)

		return satisfying_nodes
		



class Graph:


	def __init__( self ):

		self.edges = {}


	def breadth_first_search( self, a, b ):

		discovered = [a]

		trace = { a : [a] }

		frontier = [a]

		cost = 0

		while frontier:

			cost += 1

			new_frontier = []

			for node in frontier:

				for neighbor in self.edges[ node ]:

					if neighbor not in new_frontier and neighbor not in discovered:

						trace[neighbor] = trace[node] + [neighbor]

						new_frontier.append( neighbor )
						discovered.append( neighbor )

					if neighbor == b:

						return trace[ b ]

			frontier = new_frontier


if __name__ == '__main__':
	
	g = Graph()

	g.edges = { 0 : [3], 1 : [4], 3 :[1,2] }

	print g.breadth_first_search( 0, 4 )





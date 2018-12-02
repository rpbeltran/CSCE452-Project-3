

from point  import Point
from line   import Line
from region import Region
from graph  import Graph


class Cell_Field:

	def __init__( self, w, h ):

		self.w = w
		self.h = h

		self.obstacles = []


	def determine_regions( self ):

		# -- Begin with one large region

		self.regions = [ 
			Region( 
				Point(0,0), 
				Point( self.w, self.h) 
			) 
		]
		
		# -- Determine critical lines

		critical_lines = []

		for obstacle in self.obstacles:

			corners = obstacle.corners

			critical_lines.append( Line( corners[0], corners[1] ) )
			critical_lines.append( Line( corners[2], corners[3] ) )

			critical_lines.append( Line( corners[0], corners[2] ) )
			critical_lines.append( Line( corners[1], corners[3] ) )
			

		# -- Divide regions along critical lines

		for line in critical_lines:

			new_regions = []

			for region in self.regions:

				new_regions.extend( region.bisect( line ) )

			self.regions = new_regions


		# -- Mark obstacles regions

		for region in self.regions:

			center = region.center

			for obs in self.obstacles:

				if center in obs:

					region.obstacle = True

					break


	def construct_graph( self ):

		self.nav_graph = Graph() 

		for u in range( len( self.regions ) ):

			for v in range( len( self.regions ) ):

				if not self.regions[v].obstacle:

					if self.regions[u].shares_edge( self.regions[v] ):

						if u not in self.nav_graph.edges:

							self.nav_graph.edges[u] = []

						self.nav_graph.edges[u].append( v )


	def navigate( self, a, b ):

		for i in range(len(self.regions)):

			if a in self.regions[i]:

				reg_a = i

			if b in self.regions[i]:

				reg_b = i

		nav_path = self.nav_graph.breadth_first_search( reg_a, reg_b )

		point_path = [ a ]

		for reg in nav_path[1:-1]:

			point_path.append( self.regions[reg].center )

		point_path.append( b )

		return point_path






if __name__ == '__main__':

	# Create a cell field
	c = Cell_Field( 300, 300 ) # Cell_Field( w, h )

	# Add an obstacle
	c.obstacles.append( Region( 100, 100, 100, 100 ) ) # Region( x, y, w, h )

	# Modify an obstacle by direct access
	# c.obstacles[0] = ...

	# Call these two again if you move an obstacle
	c.determine_regions()
	c.construct_graph()

	# Returns a list of points which take you from a to b without crossing an obstacle
	print c.navigate( Point(20,150), Point(270,150) )








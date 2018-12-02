
class Point:

	""" Sortable Point class """

	def __init__( self, x, y ):

		self.x = x
		self.y = y


	# Comparison

	def __eq__( self, b ):

		return ( self.x == b.x ) and ( self.y == b.y )

	def __gt__( self, b ):

		return self.y > b.y if self.y != b.y else self.x > b.x


	# Point string cast

	def __str__( self ):

		return "({x},{y})".format( x = self.x, y = self.y )

	__repr__ = __str__


	# Hashing

	def __hash__( self ):

		return int( 1e8 * self.y + self.x )

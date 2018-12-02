
class Line:

	""" Line through a and b """

	def __init__( self, *args ):

		args = sorted( args )

		self.a = args[0]
		self.b = args[1]

		self.dx = self.b.x - self.a.x
		self.dy = self.b.y - self.a.y


	# Determine y from given x
	
	def y ( self, x ):

		dx = x - self.b.x

		if not self.dx:

			return None

		return self.b.y + ( dx * self.dy / self.dx )
	

	# Determine x from given y

	def x ( self, y ):

		dy = y - self.b.y

		if not self.dy:

			return None

		return self.b.x + ( dy * self.dx / self.dy )


	# String conversion
	
	def __str__( self ):

		return "Line: {p1}, {p2}".format( p1=a, p2=b )

	__repr__ = __str__

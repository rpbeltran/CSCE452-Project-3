
from point import Point
from line  import Line



class Region:

	""" Region Class """

	def __init__ ( self, *args, **kwargs ):

		if len( args ) == 2:

			args = sorted( args)

			self.x = args[0].x
			self.y = args[0].y
			self.w = args[1].x - args[0].x
			self.h = args[1].y - args[0].y

		elif len( args ) == 4:

			self.x = args[0]
			self.y = args[1]
			self.w = args[2]
			self.h = args[3]

		self.obstacle = kwargs['obstacle'] if 'obstacle' in kwargs else False


	# Calculate Corner points

	@property
	def corners( self ):

		return (
			Point( self.x,          self.y          ),
			Point( self.x + self.w, self.y          ),
			Point( self.x,          self.y + self.h ),
			Point( self.x + self.w, self.y + self.h )
		)

	# Calculate center point

	@property
	def center( self ):

		return Point( self.x + self.w / 2, self.y + self.h / 2 )


	# Check if point is within given region

	def contains( self, arg ):

		if isinstance( arg, Point ): 
			
			return (
				self.x <= arg.x <= self.x + self.w and
				self.y <= arg.y <= self.y + self.h
			)
		
		if isinstance( arg, Line ): 

			return ( 
				self.y <= arg.y( self.x          ) <= self.y + self.h or
				self.y <= arg.y( self.x + self.w ) <= self.y + self.h or
				self.x <= arg.x( self.y          ) <= self.x + self.w or
				self.x <= arg.x( self.y + self.h ) <= self.x + self.w
			)


	# Determine Bisections

	def bisect( self, line ):

		horizontal = self.y <= line.y( self.x ) <= self.y + self.h
		vertical   = self.x <= line.x( self.y ) <= self.x + self.w

		if horizontal and not vertical:

			return ( 
				Region( Point(self.x,self.y),         Point( self.x+self.w, line.y(self.x) ) ),
				Region( Point(self.x,line.y(self.x)), Point( self.x+self.w, self.y+self.h  ) )
			)


		elif vertical and not horizontal:

			return (
				Region( Point(self.x, self.y),         Point(line.x(self.y), self.y+self.h ) ),
				Region( Point(line.x(self.y), self.y), Point(self.x+self.w,  self.y+self.h ) )
			)

		else:

			return tuple( [ self ] )


	# Determine if two regions share an edge

	def shares_edge( self, region ):

		# Note: This is actually kinda cool

		corners_1 = set(  self.corners  )
		corners_2 = set( region.corners )

		return len( corners_1.intersection( corners_2 ) ) > 1


	# Support "point in region" syntax

	__contains__ = contains


	# Equality

	def __eq__( self, b ):

		return ( 
			self.x == b.x and 
			self.y == b.y and 
			self.x == b.x and 
			self.y == b.y 
		)


	# String conversion

	def __str__( self ):

		corners = self.corners

		return "Region: {a}, {b}".format(a=corners[0], b=corners[3])

	__repr__ = __str__




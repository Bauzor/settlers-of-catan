class Player:
	'''
	Implementation Notes:
	- players start with 13 roads since 2 roads are placed during the initialization phase of the game
	- likewise for settlements
	- players must have a colour upon initialization
	'''
	def __init__(
		self,
		colour,
		roads = 13,
		settlements = 3,
		cities = 4,
		resources = {
			"brick":0,
			"wool":0,
			"ore":0,
			"grain":0,
			"lumber":0
		},
		maritime_trade_owned = [],
		points = 0,
		hidden_points = 0,
		dev_card = []
	):
		self.colour = colour
		self.roads = roads
		self.settlements = settlements
		self.cities = cities
		self.resources = resources
		self.maritime_trade_owned = maritime_trade_owned
		self.points = points
		self.hidden_points = hidden_points
		self.dev_cards = dev_cards
	
	def getColour(self):
		return self.colour
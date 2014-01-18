class Element(object):
	""" Main class of elements on board """
	def __init__(self, posX, posY, sizeX, sizeY):
		super(Element, self).__init__()
		self.pos = (posX, posY)
		self.size = (sizeX, sizeY)
		self.state = Idle()


#SubClass
class Creature(Element):
	def __init__(self, lp):
		super(Creature, self).__init__()
		this.lifePoint = lp
		this.angle = 0;

class StillObject(Element):
	def __init__(self):
		super(StillObject, self).__init__()

#SubSubClass
class Character(Creature):
	def __init__(self, name):
		super(Character, self).__init__()
		self.name = name

class Castle(Creature):
	def __init__(self):
		super(Castle,self).__init__()
		
class Monster(Creature):
	def __init__(self, arg):
		super(Monster, self).__init__()

class Chest(StillObject):
	def __init__(self):
		super(Chest,self).__init__()
		# TODO : define what is in the chest
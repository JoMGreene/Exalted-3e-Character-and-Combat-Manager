import sys


class Character:
	def __init__(self):
		self.Name = ' '
		
		self.Attributes = []
		
		self.Abilities = []
		
		self.MartialArts = []
		
		self.Crafts = []
		
		self.EssenceRating = 1
		self.PersonalMotes = 13
		self.PeripheralMotes = 33
		self.ExaltType = 'Solar'
		
		self.CharmsTreeList = []
		
	def addCharmTree(self):
		bcharmtree = CharmTree()
		self.CharmsTreeList.append(bcharmtree)
		
	def addAbility(self):
		bability = Ability()
		self.Abilities.append(bability)
		
	def addMartialArt(self):
		bmarart = Ability()
		self.MartialArts.append(bmarart)
		
	def addCraft(self):
		bcraft = Ability()
		self.Crafts.append(bcraft)
	
class CharmTree:
	def __init__(self):
		self.CTName = ' '
		self.CharmsList = []
	
	def addCharm(self):
		bcharm = Charm()
		self.CharmsList.append(bcharm)

class Charm:
	def __init__(self):
		self.CmName = ' '
		self.CmCategory = ' '
		self.Cost = [0, 0, 0]
		self.CmDuration = ' '
		self.CmDurType = 'Rounds'
		self.CmType = ' '
		self.CmTags = ' '
		self.CmDesc = ' '	
	
	def __repr__(self):
		return "Charm Name: {}, Charm Category: {}, Charm Cost: {}, Charm Duration: {}, Charm Type: {}, Charm Description: {}".format(self.CmName, self.CmCategory, self.CmCost, self.CmDuration, self.CmType, self.CmDesc)
		
class Ability:
	def __init__(self):
		self.AbName = ' '
		self.AbRating = 0
		self.AbFavored = False
		self.AbSpecialties = []
		
class AbilitiesList:
	def __init__(self):
		self.AbArray = []
		
	def addAbility(self):
		self.AbArray.append(Ability())

class Attribute:
	def __init__(self):
		self.AtName = ' '
		self.AtRating = 1
		self.Favored = False
		

#x = Character()

#x.addCharmTree()

#x.CharmsTreeList[0].CTName = 'First Tree'
#x.CharmsTreeList[0].addCharm()

#x.CharmsTreeList[0].CharmsList[0].CmName = 'First Charm'
#x.CharmsTreeList[0].CharmsList[0].CmCategory = 'Athletics'
#x.CharmsTreeList[0].CharmsList[0].CmCost = [3, 1, 0]
#x.CharmsTreeList[0].CharmsList[0].CmDuration = 1
#x.CharmsTreeList[0].CharmsList[0].CmType = 'Simple'
#x.CharmsTreeList[0].CharmsList[0].CmDesc = 'Sample First Charm Desc'


#print(x.CharmsTreeList[0].CharmsList[0])
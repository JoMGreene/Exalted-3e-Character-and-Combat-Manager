import sys

from newdice import die_roller

from qttilesetup import AbilityBox, AbilityArray, AttributeArray, Charm, CharmTree, CharmTreeTab, WeaponTree, Weapon, ArmorTree, Armor

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
	QApplication,
	QLabel,
	QMainWindow,
	QPushButton,
	QTabWidget,
	QLineEdit,
	QWidget,
	QVBoxLayout,
	QCheckBox,
	QHBoxLayout,
	QSpinBox,
	QTreeView,
	QComboBox,
)

class Main(QMainWindow):
	def __init__(self):
		super().__init__()
		
		#Set Title
		self.setWindowTitle("Exalted 3rd Edition Character Manager")
		
		self.chartabs = QTabWidget()
		self.statstab = QWidget()
		self.charmstab = QWidget()
		self.combattab = QWidget()
		
		self.chartabs.addTab(self.statstab,"Char")
		self.chartabs.addTab(self.charmstab,"Charms")
		self.chartabs.addTab(self.combattab,"Combat")
		
		self.dicepool = 0
		self.abil_dicepool = 0
		self.att_dicepool = 0
		
		#Character Main Tab Info
		
		self.abilRollBox = QComboBox()
		self.abilRollBox.currentIndexChanged.connect(self.change_abil_dicepool)
		self.attRollBox = QComboBox()
		self.attRollBox.addItems(["Strength", "Dexterity", "Stamina", "Charisma", "Manipulation", "Appearance", "Perception", "Intelligence", "Wits"])
		self.attRollBox.currentIndexChanged.connect(self.change_att_dicepool)
		
		
		
		self.diebox = QSpinBox()
		self.diebox.valueChanged.connect(self.dice_pool_update)
		
		self.dieresult = QLabel(" ")
		self.diearrayfinal = QLabel(" ")
		
		
		self.AbilArray = []
		self.addAbilButton = QPushButton('+')
		self.addAbilButton.clicked.connect(self.add_ability_box)
		
		self.abillayout = QVBoxLayout()
		self.abillayout2 = QVBoxLayout()
		self.abillayout.addLayout(self.abillayout2)
		self.abillayout.addWidget(self.addAbilButton)

		
		self.AttArray = AttributeArray()
		
		for iii in range(9):
			self.AttArray.attRatings[iii].valueChanged.connect(self.change_att_dicepool)
		
		self.button = QPushButton("Roll The Dice")
		self.button.clicked.connect(self.roll_button_click)
		
		self.double10 = QCheckBox("Double 10s")
		self.double10limit = QCheckBox("Limit")
		self.double10num = QSpinBox()
		
		self.double9 = QCheckBox("Double 9s")
		self.double9limit = QCheckBox("Limit")
		self.double9num = QSpinBox()
		
		self.double8 = QCheckBox("Double 8s")
		self.double8limit = QCheckBox("Limit")
		self.double8num = QSpinBox()
		
		self.double7 = QCheckBox("Double 7s")
		self.double7limit = QCheckBox("Limit")
		self.double7num = QSpinBox()
		
		self.roll1 = QCheckBox("Reroll 1s")
		self.roll1num = QSpinBox()
		
		self.roll2 = QCheckBox("Reroll 2s")
		self.roll2num = QSpinBox()
		
		self.roll3 = QCheckBox("Reroll 3s")
		self.roll3num = QSpinBox()
		
		self.roll4 = QCheckBox("Reroll 4s")
		self.roll4num = QSpinBox()
		
		self.roll5 = QCheckBox("Reroll 5s")
		self.roll5num = QSpinBox()
		
		self.roll6 = QCheckBox("Reroll 6s")
		self.roll6num = QSpinBox()
		
		self.rollfails = QCheckBox("Reroll Failures")
		self.rollfailsnum = QSpinBox()
		
		#For Print Debug
		#self.printAbil = QPushButton('print')
		#self.printAbil.clicked.connect(self.print_abils)
		
		#Character Main Tab Layout
		
		self.rollerLayout = QHBoxLayout()
		self.rollerLayout.addWidget(self.abilRollBox)
		self.rollerLayout.addWidget(self.attRollBox)
		self.rollerLayout.addWidget(self.diebox)
		self.rollerLayout.addWidget(self.button)
		
		self.statstab.layout2 = QHBoxLayout()
		self.statstab.layout2.addWidget(self.double10)
		self.statstab.layout2.addWidget(self.double10limit)
		self.statstab.layout2.addWidget(self.double10num)
		self.statstab.layout2.addWidget(self.double9)
		self.statstab.layout2.addWidget(self.double9limit)
		self.statstab.layout2.addWidget(self.double9num)
		self.statstab.layout2.addWidget(self.double8)
		self.statstab.layout2.addWidget(self.double8limit)
		self.statstab.layout2.addWidget(self.double8num)
		self.statstab.layout2.addWidget(self.double7)
		self.statstab.layout2.addWidget(self.double7limit)
		self.statstab.layout2.addWidget(self.double7num)
		
		self.statstab.layout1 = QHBoxLayout()
		self.statstab.layout1.addWidget(self.roll1)
		self.statstab.layout1.addWidget(self.roll1num)
		self.statstab.layout1.addWidget(self.roll2)
		self.statstab.layout1.addWidget(self.roll2num)
		self.statstab.layout1.addWidget(self.roll3)
		self.statstab.layout1.addWidget(self.roll3num)
		self.statstab.layout1.addWidget(self.roll4)
		self.statstab.layout1.addWidget(self.roll4num)
		self.statstab.layout1.addWidget(self.roll5)
		self.statstab.layout1.addWidget(self.roll5num)
		self.statstab.layout1.addWidget(self.roll6)
		self.statstab.layout1.addWidget(self.roll6num)
		self.statstab.layout1.addWidget(self.rollfails)
		self.statstab.layout1.addWidget(self.rollfailsnum)
		
		self.statstab.layoutAbilities = QVBoxLayout()
		self.statstab.layoutAbilities.addLayout(self.abillayout)
		
		self.statstab.layout = QVBoxLayout()
		self.statstab.layout.addLayout(self.rollerLayout)
		self.statstab.layout.addWidget(self.dieresult)
		self.statstab.layout.addWidget(self.diearrayfinal)
		self.statstab.layout.addLayout(self.statstab.layout2)
		self.statstab.layout.addLayout(self.statstab.layout1)
		self.statstab.layout.addWidget(self.AttArray)
		self.statstab.layout.addLayout(self.statstab.layoutAbilities)
		
		self.statstab.setLayout(self.statstab.layout)
		
		#Charms Tab Content
		self.charmstreefull = CharmTreeTab()
		self.charmstab.layout = QVBoxLayout()
		self.charmstab.layout.addWidget(self.charmstreefull)
		
		#Charms Tab Layout
		self.charmstab.setLayout(self.charmstab.layout)
		
		#Combat Tab Content
		self.weaponsTree = WeaponTree()
		self.armorTree = ArmorTree()
		
		#Combat Tab Layout
		self.combattab.layout = QVBoxLayout()
		self.combattab.layout.addWidget(self.weaponsTree)
		self.combattab.layout.addWidget(self.armorTree)
		self.combattab.setLayout(self.combattab.layout)
		
		#Main App Layout
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.chartabs)
		
		container = QWidget()
		container.setLayout(self.layout)
		self.setCentralWidget(container)
	
	#Dice Roller function call on Roll Button click
	def roll_button_click(self):
		rerolltypearr = [self.roll1.isChecked(), self.roll2.isChecked(), self.roll3.isChecked(), self.roll4.isChecked(), self.roll5.isChecked(), self.roll6.isChecked(), self.rollfails.isChecked()]
		rerollnumarr = [int(self.roll1num.text()), int(self.roll2num.text()), int(self.roll3num.text()), int(self.roll4num.text()), int(self.roll6num.text()), int(self.roll6num.text()), int(self.rollfailsnum.text())] 
		doubletypes = [self.double10.isChecked(), self.double9.isChecked(), self.double8.isChecked(), self.double7.isChecked()]
		doublelimits = [self.double10limit.isChecked(), self.double9limit.isChecked(), self.double8limit.isChecked(), self.double7limit.isChecked()]
		doublenums = [int(self.double10num.text()), int(self.double9num.text()), int(self.double8num.text()), int(self.double7num.text())]
		diearray, numsuc, succtext, throw1, throw2 = die_roller(self.dicepool, rerolltypearr, rerollnumarr, doubletypes, doublelimits, doublenums)
		tempdie = str(numsuc)
		tempdie += " " + str(succtext)
		self.dieresult.setText(tempdie)
		diearrayfuse = ', '.join(str(e) for e in diearray)
		self.diearrayfinal.setText(diearrayfuse)
	
#	def add_ability_box(self):
#		self.testAbil = AbilityBox()
#		self.layoutAbilities.addWidget(self.testAbil)
	#Debug Help	
	def print_abils(self):
		print(self.layoutAbilities.itemAt(0).widget)
		print(self.layoutAbilities.itemAt(1).widget)
		
	def add_ability_box(self):
		self.AbilArray.append(AbilityBox())
		self.abillayout2.addWidget(self.AbilArray[-1])
		self.abilRollBox.addItem(self.AbilArray[-1].AbilName.text())
		self.AbilArray[-1].AbilName.textEdited.connect(lambda:self.change_abil_combo_name())
		self.AbilArray[-1].AbilRating.valueChanged.connect(self.change_abil_dicepool)
	
	def change_abil_combo_name(self):
		thisAbil = self.sender()
		for jj in range(len(self.AbilArray)):
			if self.AbilArray[jj].AbilName == thisAbil:
				theAbil = jj
		
		self.abilRollBox.setItemText(theAbil, self.AbilArray[theAbil].AbilName.text())
	
	def change_abil_dicepool(self):
		self.abil_dicepool = self.AbilArray[self.abilRollBox.currentIndex()].AbilRating.value()
		self.dice_pool_update()
		
	def change_att_dicepool(self):
		self.att_dicepool = self.AttArray.attRatings[self.attRollBox.currentIndex()].value()
		self.dice_pool_update()
		
	def dice_pool_update(self):
		self.dicepool = self.abil_dicepool + self.att_dicepool + self.diebox.value()
	
if __name__ == "__main__":	
	app = QApplication(sys.argv)

	window = Main()
	window.show()

	app.exec()
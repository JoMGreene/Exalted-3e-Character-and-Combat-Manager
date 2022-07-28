import sys

from newdice import die_roller

from qttilesetup import AbilityBox, AbilityArray, AttributeArray, WeaponTree, Weapon, ArmorTree, Armor

from qttilesetup2 import Charm, CharmTree, CharmTreeTab

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import (
	QApplication,
	QLabel,
	QMainWindow,
	QPushButton,
	QTabWidget,
	QFileDialog,
	QLineEdit,
	QWidget,
	QVBoxLayout,
	QCheckBox,
	QHBoxLayout,
	QSpinBox,
	QTreeView,
	QComboBox,
	QScrollArea
)

class Main(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setAcceptDrops(True)
		#Set Title
		self.setWindowTitle("Exalted 3rd Edition Character Manager")

		self.resize(1200,800)
		self.setFixedSize(1200,800)

		windowrect = self.frameGeometry()
		screencenter = self.screen().availableGeometry().center()
		windowrect.moveCenter(screencenter)
		self.move(windowrect.topLeft())

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
		
		self.doubles = []
		self.doublenums = []
		self.doublelimit = []
		for i in range(4):
			self.doubles.append(QCheckBox("Double " + str(10 - i) + "s"))
			self.doublelimit.append(QCheckBox("Limit"))
			self.doublenums.append(QSpinBox())
			
		#self.double10 = QCheckBox("Double 10s")
		#self.double10limit = QCheckBox("Limit")
		#self.double10num = QSpinBox()
		
		#self.double9 = QCheckBox("Double 9s")
		#self.double9limit = QCheckBox("Limit")
		#self.double9num = QSpinBox()
		
		#self.double8 = QCheckBox("Double 8s")
		#self.double8limit = QCheckBox("Limit")
		#self.double8num = QSpinBox()
		
		#self.double7 = QCheckBox("Double 7s")
		#self.double7limit = QCheckBox("Limit")
		#self.double7num = QSpinBox()

		self.rolls = []
		self.rollnums = []
		for j in range(6):
			self.rolls.append(QCheckBox("Reroll " + str(j + 1) +"s"))
			self.rollnums.append(QSpinBox())
		print(self.rolls)
		
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
		for i in range(4):
			self.statstab.layout2.addWidget(self.doubles[i])
			self.statstab.layout2.addWidget(self.doublelimit[i])
			self.statstab.layout2.addWidget(self.doublenums[i])
		
		self.statstab.layout1 = QHBoxLayout()
		for j in range(6):
			self.statstab.layout1.addWidget(self.rolls[j])
			self.statstab.layout1.addWidget(self.rollnums[j])
		self.statstab.layout1.addWidget(self.rollfails)
		self.statstab.layout1.addWidget(self.rollfailsnum)
		
		self.statstab.layoutAbilities = QVBoxLayout()
		self.statstab.layoutAbilities.addLayout(self.abillayout)

		self.openfilebutton = QPushButton("Load Character")
		self.openfilebutton.clicked.connect(self.open_char_file)
		
		self.statstab.layout = QVBoxLayout()
		self.statstab.layout.addLayout(self.rollerLayout)
		self.statstab.layout.addWidget(self.dieresult)
		self.statstab.layout.addWidget(self.diearrayfinal)
		self.statstab.layout.addLayout(self.statstab.layout2)
		self.statstab.layout.addLayout(self.statstab.layout1)
		self.statstab.layout.addWidget(self.AttArray)
		self.statstab.layout.addLayout(self.statstab.layoutAbilities)
		self.statstab.layout.addWidget(self.openfilebutton)
		
		self.statstab.setLayout(self.statstab.layout)
		


		#Charms Tab Content
		self.charmTreeArray = CharmTreeTab()


		self.charmTreeScroll = QScrollArea()
		self.charmTreeScroll.setWidget(self.charmTreeArray)

		self.charmstab.layout = QVBoxLayout()
		self.charmstab.layout.addWidget(self.charmTreeScroll)

		
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
		rerolltypearr = []
		rerollnumarr = []
		for k in range(6):
			rerollnumarr.append(int(self.rollnums[k].text()))
			rerolltypearr.append(self.rolls[k].isChecked())
		rerolltypearr.append(self.rollfails.isChecked())
		rerollnumarr.append(int(self.rollfailsnum.text()))
		doubletypes = []
		doublelimits = []
		doublenums = []
		for k in range(4):
			doubletypes.append(self.doubles[k].isChecked())
			doublelimits.append(self.doublelimit[k].isChecked())
			doublenums.append(int(self.doublenums[k].text()))
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


	def add_charm_tree(self):
		self.CharmTreeArray.append(CharmTree())
		
		self.charmstabTree.addWidget(self.CharmTreeArray[-1])

	def open_char_file(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', 'F:\Projects\PyQt projects\Own\Exalted-3e-Character-and-Combat-Manager')
		self.filenames = []
		if fname[0]:
			self.filename = fname[0]
		with open(self.filename) as f:
			chardata = f.readlines()
		readatts = chardata[0].split(",")
		for i in range(9):
			self.AttArray.attRatings[i].setValue(int(readatts[i]))
		readabils = chardata[1].split(",")
		readabilratings = chardata[2].split(",")
		while len(self.AbilArray) < len(readabils):
			self.add_ability_box()
		for i in range(len(readabils)):
			self.AbilArray[i].AbilName.setText(str(readabils[i]))
			self.AbilArray[i].AbilRating.setValue(int(readabilratings[i]))
		readcharmtrees = chardata[3].split("[Tree]")
		while len(self.charmTreeArray.CharmTreeArray) < len(readcharmtrees):
				self.charmTreeArray.add_charm_tree()
		for i in range(len(readcharmtrees)):
			readcharms = readcharmtrees[i].split(":")
			self.charmTreeArray.CharmTreeArray[i].CharmTreeName.setText(readcharms[0])
			while len(self.charmTreeArray.CharmTreeArray[i].CharmArray) < len(readcharms) - 1:
				self.charmTreeArray.CharmTreeArray[i].add_charm_single()
			for j in range(1,len(readcharms)):
				readsingle = readcharms[j].split(",")
				self.charmTreeArray.CharmTreeArray[i].CharmArray[j-1].CharmName.setText(readsingle[0])

	
	def dragEnterEvent(self, e):
		e.accept()
	
	def dropEvent(self, e):
		pos = e.position()
		widget = e.source()


		for n in range(self.charmstabTree.count()):
            # Get the widget at each index in turn.
			w = self.charmstabTree.itemAt(n).widget()
			if pos.y() < w.y() + w.size().height() and pos.y() > w.y():
                # We didn't drag past this widget.
                # insert to the left of it.
				self.charmstabTree.insertWidget(n, widget)
				break

		e.accept()
	
if __name__ == "__main__":	
	app = QApplication([])

	window = Main()
	window.show()

	app.exec()
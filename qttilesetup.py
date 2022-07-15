import sys

import characterclass as charcl

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
	QApplication,
	QLabel,
	QMainWindow,
	QPushButton,
	QTabWidget,
	QLineEdit,
	QTextEdit,
	QWidget,
	QVBoxLayout,
	QCheckBox,
	QHBoxLayout,
	QSpinBox,
	QComboBox,
)

class AttributeArray(QWidget):
	def __init__(self):
		super().__init__()
		
		self.attNames = []
		self.attFavs = []
		self.attRatings = []
		
		self.attNames.append(QLabel('Strength:'))
		self.attNames.append(QLabel('Dexterity:'))		
		self.attNames.append(QLabel('Stamina:'))	
		self.attNames.append(QLabel('Charisma:'))		
		self.attNames.append(QLabel('Manipulation:'))		
		self.attNames.append(QLabel('Appearance:'))		
		self.attNames.append(QLabel('Perception:'))		
		self.attNames.append(QLabel('Intelligence:'))		
		self.attNames.append(QLabel('Wits:'))
	
		for i in range(9):
			self.attFavs.append(QCheckBox())
			self.attRatings.append(QSpinBox())
		
		
		self.layoutStr = QHBoxLayout()
		self.layoutStr.addWidget(self.attNames[0])
		self.layoutStr.addWidget(self.attFavs[0])
		self.layoutStr.addWidget(self.attRatings[0])
		
		self.layoutDex = QHBoxLayout()
		self.layoutDex.addWidget(self.attNames[1])
		self.layoutDex.addWidget(self.attFavs[1])
		self.layoutDex.addWidget(self.attRatings[1])
		
		self.layoutSta = QHBoxLayout()
		self.layoutSta.addWidget(self.attNames[2])
		self.layoutSta.addWidget(self.attFavs[2])
		self.layoutSta.addWidget(self.attRatings[2])
		
		self.layoutCha = QHBoxLayout()
		self.layoutCha.addWidget(self.attNames[3])
		self.layoutCha.addWidget(self.attFavs[3])
		self.layoutCha.addWidget(self.attRatings[3])
		
		self.layoutMan = QHBoxLayout()
		self.layoutMan.addWidget(self.attNames[4])
		self.layoutMan.addWidget(self.attFavs[4])
		self.layoutMan.addWidget(self.attRatings[4])
		
		self.layoutApp = QHBoxLayout()
		self.layoutApp.addWidget(self.attNames[5])
		self.layoutApp.addWidget(self.attFavs[5])
		self.layoutApp.addWidget(self.attRatings[5])
		
		self.layoutPer = QHBoxLayout()
		self.layoutPer.addWidget(self.attNames[6])
		self.layoutPer.addWidget(self.attFavs[6])
		self.layoutPer.addWidget(self.attRatings[6])
		
		self.layoutInt = QHBoxLayout()
		self.layoutInt.addWidget(self.attNames[7])
		self.layoutInt.addWidget(self.attFavs[7])
		self.layoutInt.addWidget(self.attRatings[7])
		
		self.layoutWit = QHBoxLayout()
		self.layoutWit.addWidget(self.attNames[8])
		self.layoutWit.addWidget(self.attFavs[8])
		self.layoutWit.addWidget(self.attRatings[8])
		
		self.layoutPhys = QVBoxLayout()
		self.layoutPhys.addLayout(self.layoutStr)
		self.layoutPhys.addLayout(self.layoutDex)
		self.layoutPhys.addLayout(self.layoutSta)
		
		self.layoutSoc = QVBoxLayout()
		self.layoutSoc.addLayout(self.layoutCha)
		self.layoutSoc.addLayout(self.layoutMan)
		self.layoutSoc.addLayout(self.layoutApp)
		
		self.layoutMent = QVBoxLayout()
		self.layoutMent.addLayout(self.layoutPer)
		self.layoutMent.addLayout(self.layoutInt)
		self.layoutMent.addLayout(self.layoutWit)
		
		self.layout = QHBoxLayout()
		self.layout.addLayout(self.layoutPhys)
		self.layout.addLayout(self.layoutSoc)
		self.layout.addLayout(self.layoutMent)
		
		self.setLayout(self.layout)
		
		

class AbilityBox(QWidget):
	def __init__(self):
		super().__init__()
		self.Abil = charcl.Ability()
		
		self.AbilName = QLineEdit()
		self.AbilName.setFixedWidth(100)
		self.AbilName.textEdited.connect(self.change_abil_name)
		
		self.ShowAbilName = QLabel(' ')
		
		self.AbilRating = QSpinBox()
		self.AbilRating.setFixedWidth(50)
		
		self.AbilFavored = QCheckBox()
		
		self.AbilSpecialties = QLineEdit()
		
		
		layout = QHBoxLayout()
		layout.addWidget(self.AbilName)
		layout.addWidget(self.ShowAbilName)
		layout.addWidget(self.AbilRating)
		layout.addWidget(self.AbilFavored)
		layout.addWidget(self.AbilSpecialties)
		
		self.setLayout(layout)
	
		
	def change_abil_name(self):
		self.Abil.AbName = self.AbilName.text()
		self.ShowAbilName.setText(self.Abil.AbName)
		
	
	
		
class AbilityArray(QWidget):
	def __init__(self):
		super().__init__()
		self.AbilArray = charcl.AbilitiesList()
		
		self.AbilArrayWidget = []
		
		self.layout = QVBoxLayout()
		self.layout2 = QVBoxLayout()
		self.layout.addLayout(self.layout2)
		self.layout.addWidget(self.addButton)
		
		self.setLayout(self.layout)
		
	def add_ability_box(self):
		self.AbilArray.addAbility()
		self.AbilArrayWidget.append(AbilityBox())
		

		self.layout2.addWidget(self.AbilArrayWidget[-1])






class CharmTreeTab(QWidget):
	def __init__(self):
		super().__init__()
		
		self.CharmTreeArray = []
		
		self.addButton = QPushButton('+')
		self.addButton.clicked.connect(self.add_charm_tree)
		
		self.layout = QVBoxLayout()
		self.layout2 = QVBoxLayout()
		self.layout.addLayout(self.layout2)
		self.layout.addWidget(self.addButton)
		
		self.setLayout(self.layout)
		self.add_charm_tree()
	
	def add_charm_tree(self):
		self.CharmTreeArray.append(CharmTree())
		
		self.layout2.addWidget(self.CharmTreeArray[-1])
		
		
	

class CharmTree(QWidget):
	def __init__(self):
		super().__init__()
		
		self.CharmArray = []
		
		self.CharmTreeName = QLineEdit('Charm Tree Name')
		
		self.upButtonArray = []
		self.downButtonArray = []
		
		self.addButton = QPushButton('+')
		self.addButton.clicked.connect(self.add_charm_single)
		
		self.mainlayout = QVBoxLayout()
		self.layout = QHBoxLayout()
		self.layout3 = QVBoxLayout()
		self.layout2 = QVBoxLayout()
		
		self.mainlayout.addWidget(self.CharmTreeName)
		self.layout.addLayout(self.layout3)
		self.layout.addLayout(self.layout2)
		self.mainlayout.addLayout(self.layout)
		self.mainlayout.addWidget(self.addButton)
		
		self.setLayout(self.mainlayout)
		
		self.add_charm_single()
	
	def add_charm_single(self):
		self.CharmArray.append(Charm())
		
		self.newUpButton = QPushButton('↑')
		
		self.newDownButton = QPushButton('↓')
		
		
		self.upButtonArray.append(self.newUpButton)
		self.upButtonArray[-1].clicked.connect(lambda:self.move_charm_up())
		
		self.downButtonArray.append(self.newDownButton)
		self.downButtonArray[-1].clicked.connect(lambda:self.move_charm_down())
		
		layout31 = QVBoxLayout()
		
		layout31.addWidget(self.upButtonArray[-1])
		layout31.addWidget(self.downButtonArray[-1])
		self.layout3.addLayout(layout31)
		self.layout2.addWidget(self.CharmArray[-1])
	
		
		
	def move_charm_up(self):
		thisbutton = self.sender()
		
		for j in range(len(self.upButtonArray)):
			if self.upButtonArray[j] == thisbutton:
				b = j
		if b != 0:
		
			self.CharmArray[b], self.CharmArray[(b -1)] = self.CharmArray[(b -1)], self.CharmArray[b]
			self.layout2.removeWidget(self.CharmArray[b])
			self.layout2.removeWidget(self.CharmArray[(b -1)])
			self.layout2.insertWidget(b - 1, self.CharmArray[b - 1])
			self.layout2.insertWidget(b, self.CharmArray[b])
			
	def move_charm_down(self):
		thisbutton = self.sender()
		
		for k in range(len(self.downButtonArray)):
			if self.downButtonArray[k] == thisbutton:
				b = k
		if b != (len(self.downButtonArray) - 1):
			
			self.CharmArray[b], self.CharmArray[(b + 1)] = self.CharmArray[(b + 1)], self.CharmArray[b]
			self.layout2.removeWidget(self.CharmArray[b])
			self.layout2.removeWidget(self.CharmArray[(b + 1)])
			self.layout2.insertWidget(b, self.CharmArray[b + 1])
			self.layout2.insertWidget(b, self.CharmArray[b])
			
		
	

class Charm(QWidget):
	def __init__(self):
		super().__init__()
		
		self.Charm = charcl.Charm()
		
		self.CharmName = QLineEdit()
		self.CharmName.setFixedWidth(100)
		
		self.ShowCharmName = QLabel(' ')
		
		self.CharmCategory = QLineEdit()
		self.CharmCategory.setFixedWidth(100)
		
		self.CharmDuration = QSpinBox()
		self.CharmDurationType = QComboBox()
		self.CharmDurationType.addItem('Rounds')
		self.CharmDurationType.addItem('Scenes')
		
		
		self.CharmType = QComboBox()
		self.CharmType.addItem('Reflexive')
		self.CharmType.addItem('Supplemental')
		self.CharmType.addItem('Simple')
		self.CharmType.addItem('Permanent')
		
		self.CharmTags = QLineEdit()
		self.CharmTags.setFixedWidth(100)
		
		self.CharmDesc = QTextEdit()
		
		
		layout = QHBoxLayout()
		layout.addWidget(self.CharmName)
		layout.addWidget(self.CharmCategory)
		layout.addWidget(self.CharmDuration)
		layout.addWidget(self.CharmType)
		layout.addWidget(self.CharmTags)
		layout.addWidget(self.CharmDesc)
		
		self.setLayout(layout)



class Weapon(QWidget):
	def __init__(self):
		super().__init__()
		
		self.weaponName = QLineEdit()
		
		self.weaponAcc = QSpinBox()
		self.weaponDam = QSpinBox()
		self.weaponDef = QSpinBox()
		self.weaponOvr = QSpinBox()
		self.weaponTags = QLineEdit()
		
		self.layout = QHBoxLayout()
		self.layout2 = QVBoxLayout()
		self.layout.addWidget(self.weaponName)
		self.layout.addWidget(self.weaponAcc)
		self.layout.addWidget(self.weaponDam)
		self.layout.addWidget(self.weaponDef)
		self.layout.addWidget(self.weaponOvr)
		self.layout2.addLayout(self.layout)
		self.layout2.addWidget(self.weaponTags)
		
		self.setLayout(self.layout2)


class WeaponTree(QWidget):
	def __init__(self):
		super().__init__()
		
		self.weaponArray = []
		
		self.weaponTopLabel = QLabel('Weapons')
		
		self.addWepButton = QPushButton()
		self.addWepButton.clicked.connect(self.add_weapon_single)
		
		self.layout = QVBoxLayout()
		self.layout2 = QVBoxLayout()
		
		self.layout.addWidget(self.weaponTopLabel)
		self.layout.addLayout(self.layout2)
		self.layout.addWidget(self.addWepButton)
		
		self.add_weapon_single()
		
		self.setLayout(self.layout)
		
		
	def add_weapon_single(self):
		self.weaponArray.append(Weapon())
		
		self.layout2.addWidget(self.weaponArray[-1])

class Armor(QWidget):
	def __init__(self):
		super().__init__()
		
		self.armorName = QLineEdit()
		
		self.armorSoak = QSpinBox()
		self.armorMob = QSpinBox()
		self.armorHard = QSpinBox()

		self.armorTags = QLineEdit()
		
		self.layout = QHBoxLayout()
		self.layout2 = QVBoxLayout()
		self.layout.addWidget(self.armorName)
		self.layout.addWidget(self.armorSoak)
		self.layout.addWidget(self.armorMob)
		self.layout.addWidget(self.armorHard)
		self.layout2.addLayout(self.layout)
		self.layout2.addWidget(self.armorTags)
		
		self.setLayout(self.layout2)
		
class ArmorTree(QWidget):
	def __init__(self):
		super().__init__()
		
		self.armorArray = []
		
		self.armorTopLabel = QLabel('Armor')
		
		self.addArmButton = QPushButton()
		self.addArmButton.clicked.connect(self.add_armor_single)
		
		self.layout = QVBoxLayout()
		self.layout2 = QVBoxLayout()
		
		self.layout.addWidget(self.armorTopLabel)
		self.layout.addLayout(self.layout2)
		self.layout.addWidget(self.addArmButton)
		
		self.add_armor_single()
		
		self.setLayout(self.layout)
		
		
	def add_armor_single(self):
		self.armorArray.append(Armor())
		
		self.layout2.addWidget(self.armorArray[-1])
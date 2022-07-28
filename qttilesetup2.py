from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QLabel, QSpinBox, QComboBox, QTextEdit, QLayout, QSizePolicy
from PyQt6.QtGui import QDrag, QPixmap, QPainter, QColor
from PyQt6.QtCore import QMimeData, Qt, QEvent, QSize


class CharmTreeTab(QWidget):
	def __init__(self):
		super().__init__()
		self.setAcceptDrops(True)
		self.CharmTreeArray = []
		self.setSizePolicy(
			QSizePolicy.Policy.MinimumExpanding,
			QSizePolicy.Policy.MinimumExpanding
		)
		self.addButton = QPushButton('+')
		self.addButton.clicked.connect(self.add_charm_tree)
		
		self.layoutmain = QVBoxLayout()
		self.layout2 = QVBoxLayout()
		self.layoutmain.addLayout(self.layout2)
		self.layoutmain.addWidget(self.addButton)
		
		self.layoutmain.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
		self.setLayout(self.layoutmain)
		self.add_charm_tree()

	def add_charm_tree(self):
		self.CharmTreeArray.append(CharmTree())
		
		self.layout2.addWidget(self.CharmTreeArray[-1])
		totheight = 0
		for i in range(len(self.CharmTreeArray)):
			totheight += self.CharmTreeArray[i].minimumHeight()
		self.setMinimumHeight(500 + totheight)
		self.updateGeometry()

	def dragEnterEvent(self, e):
		e.accept()

	def dropEvent(self, e):
		pos = e.position()
		widget = e.source()


		for n in range(self.layout2.count()):
			# Get the widget at each index in turn.
			w = self.layout2.itemAt(n).widget()
			if pos.y() < w.y() + w.size().height() and pos.y() > w.y():
				# We didn't drag past this widget.
				# insert to the left of it.
				self.layout2.insertWidget(n, widget)
				break

		e.accept()

	def sizeHint(self):
		return QSize(1000, 700)






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
		self.layoutf1 = QHBoxLayout()
		self.layout3 = QVBoxLayout()
		self.layout2 = QVBoxLayout()
		
		self.mainlayout.addWidget(self.CharmTreeName)
		self.layoutf1.addLayout(self.layout3)
		self.layoutf1.addLayout(self.layout2)
		self.mainlayout.addLayout(self.layoutf1)
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

	def mouseMoveEvent(self, e):
		if e.buttons() != Qt.MouseButton.LeftButton:
			return

		drag = QDrag(self)
		mime = QMimeData()
		drag.setMimeData(mime)


		pixmap = QPixmap(350, 250)
		self.render(pixmap)
		painter = QPainter(pixmap)
		painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_DestinationIn)
		painter.fillRect(pixmap.rect(), QColor(0, 0, 0, 150))
		painter.end()
		drag.setPixmap(pixmap)

		dropAction = drag.exec(Qt.DropAction.MoveAction)

class Charm(QWidget):
	def __init__(self):
		super().__init__()
		
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
import sys

import random
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
)

def die_roller(dice, doubles, reroll1s, numreroll1s, reroll2s, numreroll2s, reroll3s, numreroll3s, reroll4s, numreroll4s, reroll5s, numreroll5s, reroll6s, numreroll6s, rerollfail, numrerollfail):
	numdice = int(dice)
	dicearr = []
	successes = 0
	successtext = " "
	reroll1sleft = int(numreroll1s)
	reroll2sleft = int(numreroll2s)
	reroll3sleft = int(numreroll3s)
	reroll4sleft = int(numreroll4s)
	reroll5sleft = int(numreroll5s)
	reroll6sleft = int(numreroll6s)
	rerollfailsleft = int(numrerollfail)
	for i in range(0, numdice):
		die = random.randint(1,10)
		if die >=7 and die < doubles:
			successes += 1
		elif die >= doubles:
			successes += 2
		elif die == 1 and reroll1s and reroll1sleft > 0:
			rerollnum, rerollsucc, throwtext, r1left, r2left, r3left, r4left, r5left, r6left, rfleft = die_roller(1,doubles, reroll1s, reroll1sleft - 1, reroll2s, reroll2sleft, reroll3s, reroll3sleft, reroll4s, reroll4sleft, reroll5s, reroll5sleft, reroll6s, reroll6sleft, rerollfail, rerollfailsleft)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			reroll1sleft = r1left
			reroll2sleft = r2left
			reroll3sleft = r3left
			reroll4sleft = r4left
			reroll5sleft = r5left
			reroll6sleft = r6left
			rerollfailsleft = rfleft
		elif die == 2 and reroll2s and reroll2sleft > 0:
			rerollnum, rerollsucc, throwtext, r1left, r2left, r3left, r4left, r5left, r6left, rfleft = die_roller(1,doubles, reroll1s, reroll1sleft, reroll2s, reroll2sleft - 1, reroll3s, reroll3sleft, reroll4s, reroll4sleft, reroll5s, reroll5sleft, reroll6s, reroll6sleft, rerollfail, rerollfailsleft)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			reroll1sleft = r1left
			reroll2sleft = r2left
			reroll3sleft = r3left
			reroll4sleft = r4left
			reroll5sleft = r5left
			reroll6sleft = r6left
			rerollfailssleft = rfleft
		elif die == 3 and reroll3s and reroll3sleft > 0:
			rerollnum, rerollsucc, throwtext, r1left, r2left, r3left, r4left, r5left, r6left, rfleft = die_roller(1,doubles, reroll1s, reroll1sleft, reroll2s, reroll2sleft, reroll3s, reroll3sleft - 1, reroll4s, reroll4sleft, reroll5s, reroll5sleft, reroll6s, reroll6sleft, rerollfail, rerollfailsleft)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			reroll1sleft = r1left
			reroll2sleft = r2left
			reroll3sleft = r3left
			reroll4sleft = r4left
			reroll5sleft = r5left
			reroll6sleft = r6left
			rerollfailsleft = rfleft
		elif die == 4 and reroll4s and reroll4sleft > 0:
			rerollnum, rerollsucc, throwtext, r1left, r2left, r3left, r4left, r5left, r6left, rfleft = die_roller(1,doubles, reroll1s, reroll1sleft, reroll2s, reroll2sleft, reroll3s, reroll3sleft, reroll4s, reroll4sleft - 1, reroll5s, reroll5sleft, reroll6s, reroll6sleft, rerollfail, rerollfailsleft)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			reroll1sleft = r1left
			reroll2sleft = r2left
			reroll3sleft = r3left
			reroll4sleft = r4left
			reroll5sleft = r5left
			reroll6sleft = r6left
			rerollfailsleft = rfleft
		elif die == 5 and reroll5s and reroll5sleft > 0:
			rerollnum, rerollsucc, throwtext, r1left, r2left, r3left, r4left, r5left, r6left, rfleft = die_roller(1,doubles, reroll1s, reroll1sleft, reroll2s, reroll2sleft, reroll3s, reroll3sleft, reroll4s, reroll4sleft, reroll5s, reroll5sleft - 1, reroll6s, reroll6sleft, rerollfail, rerollfailsleft)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			reroll1sleft = r1left
			reroll2sleft = r2left
			reroll3sleft = r3left
			reroll4sleft = r4left
			reroll5sleft = r5left
			reroll6sleft = r6left
			rerollfailsleft = rfleft
		elif die == 6 and reroll6s and reroll6sleft > 0:
			rerollnum, rerollsucc, throwtext, r1left, r2left, r3left, r4left, r5left, r6left, rfleft = die_roller(1,doubles, reroll1s, reroll1sleft, reroll2s, reroll2sleft, reroll3s, reroll3sleft, reroll4s, reroll4sleft, reroll5s, reroll5sleft, reroll6s, reroll6sleft - 1, rerollfail, rerollfailsleft)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			reroll1sleft = r1left
			reroll2sleft = r2left
			reroll3sleft = r3left
			reroll4sleft = r4left
			reroll5sleft = r5left
			reroll6sleft = r6left
			rerollfailsleft = rfleft
		elif die <= 6 and rerollfail and rerollfailsleft > 0:
			rerollnum, rerollsucc, throwtext, r1left, r2left, r3left, r4left, r5left, r6left, rfleft = die_roller(1,doubles, reroll1s, reroll1sleft, reroll2s, reroll2sleft, reroll3s, reroll3sleft, reroll4s, reroll4sleft, reroll5s, reroll5sleft, reroll6s, reroll6sleft, rerollfail, rerollfailsleft - 1)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			reroll1sleft = r1left
			reroll2sleft = r2left
			reroll3sleft = r3left
			reroll4sleft = r4left
			reroll5sleft = r5left
			reroll6sleft = r6left
			rerollfailsleft = rfleft
		dicearr.append(die)
	if successes != 1:
		successtext = "Successes"
	else:
		successtext = "Success"
	return dicearr, successes, successtext, reroll1sleft, reroll2sleft, reroll3sleft, reroll4sleft, reroll5sleft, reroll6sleft, rerollfailsleft

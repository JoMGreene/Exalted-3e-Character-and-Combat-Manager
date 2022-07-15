import sys

import random

def die_roller(dice, rerollarr, rerollleftarr, doubles, doublelimits, doublenums):
	numdice = int(dice)
	dicearr = []
	successes = 0
	successtext = " "
	rerollsremain = []
	doublesremain = []
	for m in range(0, 4):
		doublesremain.append(doublenums[m])
	for j in range(0, 7):
		rerollsremain.append(rerollleftarr[j])
	for i in range(0, numdice):
		die = random.randint(1,10)
		if die >= 7 and not doubles[10 - die]:
			successes += 1
		elif die >= 7 and doubles[10 - die]:
			if doublesremain[10 - die] > 0 or not doublelimits[10 - die]:
				successes += 2
				doublesremain[10 - die] -= 1
			else:
				successes += 1
		elif die == 1 and rerollarr[0] and rerollsremain[0] > 0:
			rerollsremain[0] -= 1
			rerollnum, rerollsucc, throwtext, rleftreturn, doublesreturn = die_roller(1, rerollarr, rerollsremain, doubles, doublelimits, doublesremain)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			for m in range(0, 4):
				doublesremain[m] = doublesreturn[m]
			for k in range(0, 7):
				rerollsremain[k] = rleftreturn[k]
		elif die == 2 and rerollarr[1] and rerollsremain[1] > 0:
			rerollsremain[1] -= 1
			rerollnum, rerollsucc, throwtext, rleftreturn, doublesreturn = die_roller(1, rerollarr, rerollsremain, doubles, doublelimits, doublesremain)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			for m in range(0, 4):
				doublesremain[m] = doublesreturn[m]
			for k in range(0, 7):
				rerollsremain[k] = rleftreturn[k]
		elif die == 3 and rerollarr[2] and rerollsremain[2] > 0:
			rerollsremain[2] -= 1
			rerollnum, rerollsucc, throwtext, rleftreturn, doublesreturn = die_roller(1, rerollarr, rerollsremain, doubles, doublelimits, doublesremain)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			for m in range(0, 4):
				doublesremain[m] = doublesreturn[m]
			for k in range(0, 7):
				rerollsremain[k] = rleftreturn[k]
		elif die == 4 and rerollarr[3] and rerollsremain[3] > 0:
			rerollsremain[3] -= 1
			rerollnum, rerollsucc, throwtext, rleftreturn, doublesreturn = die_roller(1, rerollarr, rerollsremain, doubles, doublelimits, doublesremain)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			for m in range(0, 4):
				doublesremain[m] = doublesreturn[m]
			for k in range(0, 7):
				rerollsremain[k] = rleftreturn[k]
		elif die == 5 and rerollarr[4] and rerollsremain[4] > 0:
			rerollsremain[4] -= 1
			rerollnum, rerollsucc, throwtext, rleftreturn, doublesreturn = die_roller(1, rerollarr, rerollsremain, doubles, doublelimits, doublesremain)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			for m in range(0, 4):
				doublesremain[m] = doublesreturn[m]
			for k in range(0, 7):
				rerollsremain[k] = rleftreturn[k]
		elif die == 6 and rerollarr[5] and rerollsremain[5] > 0:
			rerollsremain[5] -= 1
			rerollnum, rerollsucc, throwtext, rleftreturn, doublesreturn = die_roller(1, rerollarr, rerollsremain, doubles, doublelimits, doublesremain)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			for m in range(0, 4):
				doublesremain[m] = doublesreturn[m]
			for k in range(0, 7):
				rerollsremain[k] = rleftreturn[k]
		elif die <= 6 and rerollarr[6] and rerollsremain[6] > 0:
			rerollsremain[6] -= 1
			rerollnum, rerollsucc, throwtext, rleftreturn, doublesreturn = die_roller(1, rerollarr, rerollsremain, doubles, doublelimits, doublesremain)
			successes += rerollsucc
			for j in range(0, len(rerollnum)):		
				dicearr.append(rerollnum[j])
			for m in range(0, 4):
				doublesremain[m] = doublesreturn[m]
			for k in range(0, 7):
				rerollsremain[k] = rleftreturn[k]
		dicearr.append(die)
	if successes != 1:
		successtext = "Successes"
	else:
		successtext = "Success"
	return dicearr, successes, successtext, rerollsremain, doublesremain
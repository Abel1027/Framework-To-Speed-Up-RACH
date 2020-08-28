import matplotlib.pyplot as plt
import os

if not os.path.isdir('!graphs_average'): os.mkdir('!graphs_average')

iterations = os.listdir('!logs_for_average')

for index, iter_file in enumerate(iterations):
	file = open('!logs_for_average/' + iter_file + '/01.log')
	lines = file.readlines()
	file.close()
	elements_in_line = 0
	for lineIndex in range(0, len(lines), 2):
		elements_in_line += 1

	if index == 0:
		totalDevices = [0 for i in range(elements_in_line)]
		maxSym = [0 for i in range(elements_in_line)]
		maxSC = [0 for i in range(elements_in_line)]
		totalCollisionsNetwork = [0 for i in range(elements_in_line)]
		totalCollisions24Band = [0 for i in range(elements_in_line)]
		totalCollisions = [0 for i in range(elements_in_line)]
		totalEnergyNetwork = [0 for i in range(elements_in_line)]
		totalEnergy24Band = [0 for i in range(elements_in_line)]
		totalEnergy = [0 for i in range(elements_in_line)]
		totalEnergyGNB = [0 for i in range(elements_in_line)]
		totalTimeForRegistration = [0 for i in range(elements_in_line)]
		totalRegisteredByGNB = [0 for i in range(elements_in_line)]
		totalRegisteredByRelay = [0 for i in range(elements_in_line)]
		totalRegisteredDevices = [0 for i in range(elements_in_line)]
		totalDownlinkSC = [0 for i in range(elements_in_line)]
		totalUplinkSC = [0 for i in range(elements_in_line)]
	element_index = 0
	for lineIndex in range(0, len(lines), 2):
		totalDevices[element_index] = float(lines[lineIndex].split('|')[0]) + totalDevices[element_index]
		maxSym[element_index] = float(lines[lineIndex].split('|')[1]) + maxSym[element_index]
		maxSC[element_index] = float(lines[lineIndex].split('|')[2]) + maxSC[element_index]
		totalCollisionsNetwork[element_index] = float(lines[lineIndex].split('|')[3]) + totalCollisionsNetwork[element_index]
		totalCollisions24Band[element_index] = float(lines[lineIndex].split('|')[4]) + totalCollisions24Band[element_index]
		totalCollisions[element_index] = float(lines[lineIndex].split('|')[5]) + totalCollisions[element_index]
		totalEnergyNetwork[element_index] = float(lines[lineIndex].split('|')[6]) + totalEnergyNetwork[element_index]
		totalEnergy24Band[element_index] = float(lines[lineIndex].split('|')[7]) + totalEnergy24Band[element_index]
		totalEnergy[element_index] = float(lines[lineIndex].split('|')[8]) + totalEnergy[element_index]
		totalEnergyGNB[element_index] = float(lines[lineIndex].split('|')[9]) + totalEnergyGNB[element_index]
		totalTimeForRegistration[element_index] = float(lines[lineIndex].split('|')[10])/1000 + totalTimeForRegistration[element_index]
		totalRegisteredByGNB[element_index] = float(lines[lineIndex].split('|')[11]) + totalRegisteredByGNB[element_index]
		totalRegisteredByRelay[element_index] = float(lines[lineIndex].split('|')[12]) + totalRegisteredByRelay[element_index]
		totalRegisteredDevices[element_index] = float(lines[lineIndex].split('|')[13]) + totalRegisteredDevices[element_index]
		totalDownlinkSC[element_index] = float(lines[lineIndex].split('|')[14]) + totalDownlinkSC[element_index]
		totalUplinkSC[element_index] = float(lines[lineIndex].split('|')[15]) + totalUplinkSC[element_index]
		element_index += 1
	if index == len(iterations) - 1:
		for element_index in range(elements_in_line):
			totalDevices[element_index] = int(totalDevices[element_index]/len(iterations))
			maxSym[element_index] = maxSym[element_index]/len(iterations)
			maxSC[element_index] = maxSC[element_index]/len(iterations)
			totalCollisionsNetwork[element_index] = totalCollisionsNetwork[element_index]/len(iterations)
			totalCollisions24Band[element_index] = totalCollisions24Band[element_index]/len(iterations)
			totalCollisions[element_index] = totalCollisions[element_index]/len(iterations)
			totalEnergyNetwork[element_index] = totalEnergyNetwork[element_index]/len(iterations)
			totalEnergy24Band[element_index] = totalEnergy24Band[element_index]/len(iterations)
			totalEnergy[element_index] = totalEnergy[element_index]/len(iterations)
			totalEnergyGNB[element_index] = totalEnergyGNB[element_index] /len(iterations)
			totalTimeForRegistration[element_index] = totalTimeForRegistration[element_index]/len(iterations)
			totalRegisteredByGNB[element_index] = totalRegisteredByGNB[element_index]/len(iterations)
			totalRegisteredByRelay[element_index] = totalRegisteredByRelay[element_index]/len(iterations)
			totalRegisteredDevices[element_index] = totalRegisteredDevices[element_index]/len(iterations)
			totalDownlinkSC[element_index] = totalDownlinkSC[element_index]/len(iterations)
			totalUplinkSC[element_index] = totalUplinkSC[element_index]/len(iterations)

	file = open('!logs_for_average/' + iter_file + '/02.log')
	lines = file.readlines()
	file.close()
	elements_in_line = 0
	for lineIndex in range(0, len(lines), 2):
		elements_in_line += 1

	if index == 0:
		totalDevices2 = [0 for i in range(elements_in_line)]
		maxSym2 = [0 for i in range(elements_in_line)]
		maxSC2 = [0 for i in range(elements_in_line)]
		totalCollisionsNetwork2 = [0 for i in range(elements_in_line)]
		totalCollisions24Band2 = [0 for i in range(elements_in_line)]
		totalCollisions2 = [0 for i in range(elements_in_line)]
		totalEnergyNetwork2 = [0 for i in range(elements_in_line)]
		totalEnergy24Band2 = [0 for i in range(elements_in_line)]
		totalEnergy2 = [0 for i in range(elements_in_line)]
		totalEnergyGNB2 = [0 for i in range(elements_in_line)]
		totalTimeForRegistration2 = [0 for i in range(elements_in_line)]
		totalRegisteredByGNB2 = [0 for i in range(elements_in_line)]
		totalRegisteredByRelay2 = [0 for i in range(elements_in_line)]
		totalRegisteredDevices2 = [0 for i in range(elements_in_line)]
		totalDownlinkSC2 = [0 for i in range(elements_in_line)]
		totalUplinkSC2 = [0 for i in range(elements_in_line)]
	element_index = 0
	for lineIndex in range(0, len(lines), 2):
		totalDevices2[element_index] = float(lines[lineIndex].split('|')[0]) + totalDevices2[element_index]
		maxSym2[element_index] = float(lines[lineIndex].split('|')[1]) + maxSym2[element_index]
		maxSC2[element_index] = float(lines[lineIndex].split('|')[2]) + maxSC2[element_index]
		totalCollisionsNetwork2[element_index] = float(lines[lineIndex].split('|')[3]) + totalCollisionsNetwork2[element_index]
		totalCollisions24Band2[element_index] = float(lines[lineIndex].split('|')[4]) + totalCollisions24Band2[element_index]
		totalCollisions2[element_index] = float(lines[lineIndex].split('|')[5]) + totalCollisions2[element_index]
		totalEnergyNetwork2[element_index] = float(lines[lineIndex].split('|')[6]) + totalEnergyNetwork2[element_index]
		totalEnergy24Band2[element_index] = float(lines[lineIndex].split('|')[7]) + totalEnergy24Band2[element_index]
		totalEnergy2[element_index] = float(lines[lineIndex].split('|')[8]) + totalEnergy2[element_index]
		totalEnergyGNB2[element_index] = float(lines[lineIndex].split('|')[9]) + totalEnergyGNB2[element_index]
		totalTimeForRegistration2[element_index] = float(lines[lineIndex].split('|')[10])/1000 + totalTimeForRegistration2[element_index]
		totalRegisteredByGNB2[element_index] = float(lines[lineIndex].split('|')[11]) + totalRegisteredByGNB2[element_index]
		totalRegisteredByRelay2[element_index] = float(lines[lineIndex].split('|')[12]) + totalRegisteredByRelay2[element_index]
		totalRegisteredDevices2[element_index] = float(lines[lineIndex].split('|')[13]) + totalRegisteredDevices2[element_index]
		totalDownlinkSC2[element_index] = float(lines[lineIndex].split('|')[14]) + totalDownlinkSC2[element_index]
		totalUplinkSC2[element_index] = float(lines[lineIndex].split('|')[15]) + totalUplinkSC2[element_index]
		element_index += 1
	if index == len(iterations) - 1:
		for element_index in range(elements_in_line):
			totalDevices2[element_index] = int(totalDevices2[element_index]/len(iterations))
			maxSym2[element_index] = maxSym2[element_index]/len(iterations)
			maxSC2[element_index] = maxSC2[element_index]/len(iterations)
			totalCollisionsNetwork2[element_index] = totalCollisionsNetwork2[element_index]/len(iterations)
			totalCollisions24Band2[element_index] = totalCollisions24Band2[element_index]/len(iterations)
			totalCollisions2[element_index] = totalCollisions2[element_index]/len(iterations)
			totalEnergyNetwork2[element_index] = totalEnergyNetwork2[element_index]/len(iterations)
			totalEnergy24Band2[element_index] = totalEnergy24Band2[element_index]/len(iterations)
			totalEnergy2[element_index] = totalEnergy2[element_index]/len(iterations)
			totalEnergyGNB2[element_index] = totalEnergyGNB2[element_index] /len(iterations)
			totalTimeForRegistration2[element_index] = totalTimeForRegistration2[element_index]/len(iterations)
			totalRegisteredByGNB2[element_index] = totalRegisteredByGNB2[element_index]/len(iterations)
			totalRegisteredByRelay2[element_index] = totalRegisteredByRelay2[element_index]/len(iterations)
			totalRegisteredDevices2[element_index] = totalRegisteredDevices2[element_index]/len(iterations)
			totalDownlinkSC2[element_index] = totalDownlinkSC2[element_index]/len(iterations)
			totalUplinkSC2[element_index] = totalUplinkSC2[element_index]/len(iterations)

	file = open('!logs_for_average/' + iter_file + '/03.log')
	lines = file.readlines()
	file.close()
	elements_in_line = 0
	for lineIndex in range(0, len(lines), 2):
		elements_in_line += 1

	if index == 0:
		totalDevices3 = [0 for i in range(elements_in_line)]
		maxSym3 = [0 for i in range(elements_in_line)]
		maxSC3 = [0 for i in range(elements_in_line)]
		totalCollisionsNetwork3 = [0 for i in range(elements_in_line)]
		totalCollisions24Band3 = [0 for i in range(elements_in_line)]
		totalCollisions3 = [0 for i in range(elements_in_line)]
		totalEnergyNetwork3 = [0 for i in range(elements_in_line)]
		totalEnergy24Band3 = [0 for i in range(elements_in_line)]
		totalEnergy3 = [0 for i in range(elements_in_line)]
		totalEnergyGNB3 = [0 for i in range(elements_in_line)]
		totalTimeForRegistration3 = [0 for i in range(elements_in_line)]
		totalRegisteredByGNB3 = [0 for i in range(elements_in_line)]
		totalRegisteredByRelay3 = [0 for i in range(elements_in_line)]
		totalRegisteredDevices3 = [0 for i in range(elements_in_line)]
		totalDownlinkSC3 = [0 for i in range(elements_in_line)]
		totalUplinkSC3 = [0 for i in range(elements_in_line)]
	element_index = 0
	for lineIndex in range(0, len(lines), 2):
		totalDevices3[element_index] = float(lines[lineIndex].split('|')[0]) + totalDevices3[element_index]
		maxSym3[element_index] = float(lines[lineIndex].split('|')[1]) + maxSym3[element_index]
		maxSC3[element_index] = float(lines[lineIndex].split('|')[2]) + maxSC3[element_index]
		totalCollisionsNetwork3[element_index] = float(lines[lineIndex].split('|')[3]) + totalCollisionsNetwork3[element_index]
		totalCollisions24Band3[element_index] = float(lines[lineIndex].split('|')[4]) + totalCollisions24Band3[element_index]
		totalCollisions3[element_index] = float(lines[lineIndex].split('|')[5]) + totalCollisions3[element_index]
		totalEnergyNetwork3[element_index] = float(lines[lineIndex].split('|')[6]) + totalEnergyNetwork3[element_index]
		totalEnergy24Band3[element_index] = float(lines[lineIndex].split('|')[7]) + totalEnergy24Band3[element_index]
		totalEnergy3[element_index] = float(lines[lineIndex].split('|')[8]) + totalEnergy3[element_index]
		totalEnergyGNB3[element_index] = float(lines[lineIndex].split('|')[9]) + totalEnergyGNB3[element_index]
		totalTimeForRegistration3[element_index] = float(lines[lineIndex].split('|')[10])/1000 + totalTimeForRegistration3[element_index]
		totalRegisteredByGNB3[element_index] = float(lines[lineIndex].split('|')[11]) + totalRegisteredByGNB3[element_index]
		totalRegisteredByRelay3[element_index] = float(lines[lineIndex].split('|')[12]) + totalRegisteredByRelay3[element_index]
		totalRegisteredDevices3[element_index] = float(lines[lineIndex].split('|')[13]) + totalRegisteredDevices3[element_index]
		totalDownlinkSC3[element_index] = float(lines[lineIndex].split('|')[14]) + totalDownlinkSC3[element_index]
		totalUplinkSC3[element_index] = float(lines[lineIndex].split('|')[15]) + totalUplinkSC3[element_index]
		element_index += 1
	if index == len(iterations) - 1:
		for element_index in range(elements_in_line):
			totalDevices3[element_index] = int(totalDevices3[element_index]/len(iterations))
			maxSym3[element_index] = maxSym3[element_index]/len(iterations)
			maxSC3[element_index] = maxSC3[element_index]/len(iterations)
			totalCollisionsNetwork3[element_index] = totalCollisionsNetwork3[element_index]/len(iterations)
			totalCollisions24Band3[element_index] = totalCollisions24Band3[element_index]/len(iterations)
			totalCollisions3[element_index] = totalCollisions3[element_index]/len(iterations)
			totalEnergyNetwork3[element_index] = totalEnergyNetwork3[element_index]/len(iterations)
			totalEnergy24Band3[element_index] = totalEnergy24Band3[element_index]/len(iterations)
			totalEnergy3[element_index] = totalEnergy3[element_index]/len(iterations)
			totalEnergyGNB3[element_index] = totalEnergyGNB3[element_index] /len(iterations)
			totalTimeForRegistration3[element_index] = totalTimeForRegistration3[element_index]/len(iterations)
			totalRegisteredByGNB3[element_index] = totalRegisteredByGNB3[element_index]/len(iterations)
			totalRegisteredByRelay3[element_index] = totalRegisteredByRelay3[element_index]/len(iterations)
			totalRegisteredDevices3[element_index] = totalRegisteredDevices3[element_index]/len(iterations)
			totalDownlinkSC3[element_index] = totalDownlinkSC3[element_index]/len(iterations)
			totalUplinkSC3[element_index] = totalUplinkSC3[element_index]/len(iterations)

	file = open('!logs_for_average/' + iter_file + '/04.log')
	lines = file.readlines()
	file.close()
	elements_in_line = 0
	for lineIndex in range(0, len(lines), 2):
		elements_in_line += 1

	if index == 0:
		totalDevices4 = [0 for i in range(elements_in_line)]
		maxSym4 = [0 for i in range(elements_in_line)]
		maxSC4 = [0 for i in range(elements_in_line)]
		totalCollisionsNetwork4 = [0 for i in range(elements_in_line)]
		totalCollisions24Band4 = [0 for i in range(elements_in_line)]
		totalCollisions4 = [0 for i in range(elements_in_line)]
		totalEnergyNetwork4 = [0 for i in range(elements_in_line)]
		totalEnergy24Band4 = [0 for i in range(elements_in_line)]
		totalEnergy4 = [0 for i in range(elements_in_line)]
		totalEnergyGNB4 = [0 for i in range(elements_in_line)]
		totalTimeForRegistration4 = [0 for i in range(elements_in_line)]
		totalRegisteredByGNB4 = [0 for i in range(elements_in_line)]
		totalRegisteredByRelay4 = [0 for i in range(elements_in_line)]
		totalRegisteredDevices4 = [0 for i in range(elements_in_line)]
		totalDownlinkSC4 = [0 for i in range(elements_in_line)]
		totalUplinkSC4 = [0 for i in range(elements_in_line)]
	element_index = 0
	for lineIndex in range(0, len(lines), 2):
		totalDevices4[element_index] = float(lines[lineIndex].split('|')[0]) + totalDevices4[element_index]
		maxSym4[element_index] = float(lines[lineIndex].split('|')[1]) + maxSym4[element_index]
		maxSC4[element_index] = float(lines[lineIndex].split('|')[2]) + maxSC4[element_index]
		totalCollisionsNetwork4[element_index] = float(lines[lineIndex].split('|')[3]) + totalCollisionsNetwork4[element_index]
		totalCollisions24Band4[element_index] = float(lines[lineIndex].split('|')[4]) + totalCollisions24Band4[element_index]
		totalCollisions4[element_index] = float(lines[lineIndex].split('|')[5]) + totalCollisions4[element_index]
		totalEnergyNetwork4[element_index] = float(lines[lineIndex].split('|')[6]) + totalEnergyNetwork4[element_index]
		totalEnergy24Band4[element_index] = float(lines[lineIndex].split('|')[7]) + totalEnergy24Band4[element_index]
		totalEnergy4[element_index] = float(lines[lineIndex].split('|')[8]) + totalEnergy4[element_index]
		totalEnergyGNB4[element_index] = float(lines[lineIndex].split('|')[9]) + totalEnergyGNB4[element_index]
		totalTimeForRegistration4[element_index] = float(lines[lineIndex].split('|')[10])/1000 + totalTimeForRegistration4[element_index]
		totalRegisteredByGNB4[element_index] = float(lines[lineIndex].split('|')[11]) + totalRegisteredByGNB4[element_index]
		totalRegisteredByRelay4[element_index] = float(lines[lineIndex].split('|')[12]) + totalRegisteredByRelay4[element_index]
		totalRegisteredDevices4[element_index] = float(lines[lineIndex].split('|')[13]) + totalRegisteredDevices4[element_index]
		totalDownlinkSC4[element_index] = float(lines[lineIndex].split('|')[14]) + totalDownlinkSC4[element_index]
		totalUplinkSC4[element_index] = float(lines[lineIndex].split('|')[15]) + totalUplinkSC4[element_index]
		element_index += 1
	if index == len(iterations) - 1:
		for element_index in range(elements_in_line):
			totalDevices4[element_index] = int(totalDevices4[element_index]/len(iterations))
			maxSym4[element_index] = maxSym4[element_index]/len(iterations)
			maxSC4[element_index] = maxSC4[element_index]/len(iterations)
			totalCollisionsNetwork4[element_index] = totalCollisionsNetwork4[element_index]/len(iterations)
			totalCollisions24Band4[element_index] = totalCollisions24Band4[element_index]/len(iterations)
			totalCollisions4[element_index] = totalCollisions4[element_index]/len(iterations)
			totalEnergyNetwork4[element_index] = totalEnergyNetwork4[element_index]/len(iterations)
			totalEnergy24Band4[element_index] = totalEnergy24Band4[element_index]/len(iterations)
			totalEnergy4[element_index] = totalEnergy4[element_index]/len(iterations)
			totalEnergyGNB4[element_index] = totalEnergyGNB4[element_index] /len(iterations)
			totalTimeForRegistration4[element_index] = totalTimeForRegistration4[element_index]/len(iterations)
			totalRegisteredByGNB4[element_index] = totalRegisteredByGNB4[element_index]/len(iterations)
			totalRegisteredByRelay4[element_index] = totalRegisteredByRelay4[element_index]/len(iterations)
			totalRegisteredDevices4[element_index] = totalRegisteredDevices4[element_index]/len(iterations)
			totalDownlinkSC4[element_index] = totalDownlinkSC4[element_index]/len(iterations)
			totalUplinkSC4[element_index] = totalUplinkSC4[element_index]/len(iterations)

	file = open('!logs_for_average/' + iter_file + '/05.log')
	lines = file.readlines()
	file.close()
	elements_in_line = 0
	for lineIndex in range(0, len(lines), 2):
		elements_in_line += 1

	if index == 0:
		totalDevices5 = [0 for i in range(elements_in_line)]
		maxSym5 = [0 for i in range(elements_in_line)]
		maxSC5 = [0 for i in range(elements_in_line)]
		totalCollisionsNetwork5 = [0 for i in range(elements_in_line)]
		totalCollisions24Band5 = [0 for i in range(elements_in_line)]
		totalCollisions5 = [0 for i in range(elements_in_line)]
		totalEnergyNetwork5 = [0 for i in range(elements_in_line)]
		totalEnergy24Band5 = [0 for i in range(elements_in_line)]
		totalEnergy5 = [0 for i in range(elements_in_line)]
		totalEnergyGNB5 = [0 for i in range(elements_in_line)]
		totalTimeForRegistration5 = [0 for i in range(elements_in_line)]
		totalRegisteredByGNB5 = [0 for i in range(elements_in_line)]
		totalRegisteredByRelay5 = [0 for i in range(elements_in_line)]
		totalRegisteredDevices5 = [0 for i in range(elements_in_line)]
		totalDownlinkSC5 = [0 for i in range(elements_in_line)]
		totalUplinkSC5 = [0 for i in range(elements_in_line)]
	element_index = 0
	for lineIndex in range(0, len(lines), 2):
		totalDevices5[element_index] = float(lines[lineIndex].split('|')[0]) + totalDevices5[element_index]
		maxSym5[element_index] = float(lines[lineIndex].split('|')[1]) + maxSym5[element_index]
		maxSC5[element_index] = float(lines[lineIndex].split('|')[2]) + maxSC5[element_index]
		totalCollisionsNetwork5[element_index] = float(lines[lineIndex].split('|')[3]) + totalCollisionsNetwork5[element_index]
		totalCollisions24Band5[element_index] = float(lines[lineIndex].split('|')[4]) + totalCollisions24Band5[element_index]
		totalCollisions5[element_index] = float(lines[lineIndex].split('|')[5]) + totalCollisions5[element_index]
		totalEnergyNetwork5[element_index] = float(lines[lineIndex].split('|')[6]) + totalEnergyNetwork5[element_index]
		totalEnergy24Band5[element_index] = float(lines[lineIndex].split('|')[7]) + totalEnergy24Band5[element_index]
		totalEnergy5[element_index] = float(lines[lineIndex].split('|')[8]) + totalEnergy5[element_index]
		totalEnergyGNB5[element_index] = float(lines[lineIndex].split('|')[9]) + totalEnergyGNB5[element_index]
		totalTimeForRegistration5[element_index] = float(lines[lineIndex].split('|')[10])/1000 + totalTimeForRegistration5[element_index]
		totalRegisteredByGNB5[element_index] = float(lines[lineIndex].split('|')[11]) + totalRegisteredByGNB5[element_index]
		totalRegisteredByRelay5[element_index] = float(lines[lineIndex].split('|')[12]) + totalRegisteredByRelay5[element_index]
		totalRegisteredDevices5[element_index] = float(lines[lineIndex].split('|')[13]) + totalRegisteredDevices5[element_index]
		totalDownlinkSC5[element_index] = float(lines[lineIndex].split('|')[14]) + totalDownlinkSC5[element_index]
		totalUplinkSC5[element_index] = float(lines[lineIndex].split('|')[15]) + totalUplinkSC5[element_index]
		element_index += 1
	if index == len(iterations) - 1:
		for element_index in range(elements_in_line):
			totalDevices5[element_index] = int(totalDevices5[element_index]/len(iterations))
			maxSym5[element_index] = maxSym5[element_index]/len(iterations)
			maxSC5[element_index] = maxSC5[element_index]/len(iterations)
			totalCollisionsNetwork5[element_index] = totalCollisionsNetwork5[element_index]/len(iterations)
			totalCollisions24Band5[element_index] = totalCollisions24Band5[element_index]/len(iterations)
			totalCollisions5[element_index] = totalCollisions5[element_index]/len(iterations)
			totalEnergyNetwork5[element_index] = totalEnergyNetwork5[element_index]/len(iterations)
			totalEnergy24Band5[element_index] = totalEnergy24Band5[element_index]/len(iterations)
			totalEnergy5[element_index] = totalEnergy5[element_index]/len(iterations)
			totalEnergyGNB5[element_index] = totalEnergyGNB5[element_index] /len(iterations)
			totalTimeForRegistration5[element_index] = totalTimeForRegistration5[element_index]/len(iterations)
			totalRegisteredByGNB5[element_index] = totalRegisteredByGNB5[element_index]/len(iterations)
			totalRegisteredByRelay5[element_index] = totalRegisteredByRelay5[element_index]/len(iterations)
			totalRegisteredDevices5[element_index] = totalRegisteredDevices5[element_index]/len(iterations)
			totalDownlinkSC5[element_index] = totalDownlinkSC5[element_index]/len(iterations)
			totalUplinkSC5[element_index] = totalUplinkSC5[element_index]/len(iterations)	

	file = open('!logs_for_average/' + iter_file + '/06.log')
	lines = file.readlines()
	file.close()
	elements_in_line = 0
	for lineIndex in range(0, len(lines), 2):
		elements_in_line += 1

	if index == 0:
		totalDevices6 = [0 for i in range(elements_in_line)]
		maxSym6 = [0 for i in range(elements_in_line)]
		maxSC6 = [0 for i in range(elements_in_line)]
		totalCollisionsNetwork6 = [0 for i in range(elements_in_line)]
		totalCollisions24Band6 = [0 for i in range(elements_in_line)]
		totalCollisions6 = [0 for i in range(elements_in_line)]
		totalEnergyNetwork6 = [0 for i in range(elements_in_line)]
		totalEnergy24Band6 = [0 for i in range(elements_in_line)]
		totalEnergy6 = [0 for i in range(elements_in_line)]
		totalEnergyGNB6 = [0 for i in range(elements_in_line)]
		totalTimeForRegistration6 = [0 for i in range(elements_in_line)]
		totalRegisteredByGNB6 = [0 for i in range(elements_in_line)]
		totalRegisteredByRelay6 = [0 for i in range(elements_in_line)]
		totalRegisteredDevices6 = [0 for i in range(elements_in_line)]
		totalDownlinkSC6 = [0 for i in range(elements_in_line)]
		totalUplinkSC6 = [0 for i in range(elements_in_line)]
	element_index = 0
	for lineIndex in range(0, len(lines), 2):
		totalDevices6[element_index] = float(lines[lineIndex].split('|')[0]) + totalDevices6[element_index]
		maxSym6[element_index] = float(lines[lineIndex].split('|')[1]) + maxSym6[element_index]
		maxSC6[element_index] = float(lines[lineIndex].split('|')[2]) + maxSC6[element_index]
		totalCollisionsNetwork6[element_index] = float(lines[lineIndex].split('|')[3]) + totalCollisionsNetwork6[element_index]
		totalCollisions24Band6[element_index] = float(lines[lineIndex].split('|')[4]) + totalCollisions24Band6[element_index]
		totalCollisions6[element_index] = float(lines[lineIndex].split('|')[5]) + totalCollisions6[element_index]
		totalEnergyNetwork6[element_index] = float(lines[lineIndex].split('|')[6]) + totalEnergyNetwork6[element_index]
		totalEnergy24Band6[element_index] = float(lines[lineIndex].split('|')[7]) + totalEnergy24Band6[element_index]
		totalEnergy6[element_index] = float(lines[lineIndex].split('|')[8]) + totalEnergy6[element_index]
		totalEnergyGNB6[element_index] = float(lines[lineIndex].split('|')[9]) + totalEnergyGNB6[element_index]
		totalTimeForRegistration6[element_index] = float(lines[lineIndex].split('|')[10])/1000 + totalTimeForRegistration6[element_index]
		totalRegisteredByGNB6[element_index] = float(lines[lineIndex].split('|')[11]) + totalRegisteredByGNB6[element_index]
		totalRegisteredByRelay6[element_index] = float(lines[lineIndex].split('|')[12]) + totalRegisteredByRelay6[element_index]
		totalRegisteredDevices6[element_index] = float(lines[lineIndex].split('|')[13]) + totalRegisteredDevices6[element_index]
		totalDownlinkSC6[element_index] = float(lines[lineIndex].split('|')[14]) + totalDownlinkSC6[element_index]
		totalUplinkSC6[element_index] = float(lines[lineIndex].split('|')[15]) + totalUplinkSC6[element_index]
		element_index += 1
	if index == len(iterations) - 1:
		for element_index in range(elements_in_line):
			totalDevices6[element_index] = int(totalDevices6[element_index]/len(iterations))
			maxSym6[element_index] = maxSym6[element_index]/len(iterations)
			maxSC6[element_index] = maxSC6[element_index]/len(iterations)
			totalCollisionsNetwork6[element_index] = totalCollisionsNetwork6[element_index]/len(iterations)
			totalCollisions24Band6[element_index] = totalCollisions24Band6[element_index]/len(iterations)
			totalCollisions6[element_index] = totalCollisions6[element_index]/len(iterations)
			totalEnergyNetwork6[element_index] = totalEnergyNetwork6[element_index]/len(iterations)
			totalEnergy24Band6[element_index] = totalEnergy24Band6[element_index]/len(iterations)
			totalEnergy6[element_index] = totalEnergy6[element_index]/len(iterations)
			totalEnergyGNB6[element_index] = totalEnergyGNB6[element_index] /len(iterations)
			totalTimeForRegistration6[element_index] = totalTimeForRegistration6[element_index]/len(iterations)
			totalRegisteredByGNB6[element_index] = totalRegisteredByGNB6[element_index]/len(iterations)
			totalRegisteredByRelay6[element_index] = totalRegisteredByRelay6[element_index]/len(iterations)
			totalRegisteredDevices6[element_index] = totalRegisteredDevices6[element_index]/len(iterations)
			totalDownlinkSC6[element_index] = totalDownlinkSC6[element_index]/len(iterations)
			totalUplinkSC6[element_index] = totalUplinkSC6[element_index]/len(iterations)	

	file = open('!logs_for_average/' + iter_file + '/07.log')
	lines = file.readlines()
	file.close()
	elements_in_line = 0
	for lineIndex in range(0, len(lines), 2):
		elements_in_line += 1

	if index == 0:
		totalDevices7 = [0 for i in range(elements_in_line)]
		maxSym7 = [0 for i in range(elements_in_line)]
		maxSC7 = [0 for i in range(elements_in_line)]
		totalCollisionsNetwork7 = [0 for i in range(elements_in_line)]
		totalCollisions24Band7 = [0 for i in range(elements_in_line)]
		totalCollisions7 = [0 for i in range(elements_in_line)]
		totalEnergyNetwork7 = [0 for i in range(elements_in_line)]
		totalEnergy24Band7 = [0 for i in range(elements_in_line)]
		totalEnergy7 = [0 for i in range(elements_in_line)]
		totalEnergyGNB7 = [0 for i in range(elements_in_line)]
		totalTimeForRegistration7 = [0 for i in range(elements_in_line)]
		totalRegisteredByGNB7 = [0 for i in range(elements_in_line)]
		totalRegisteredByRelay7 = [0 for i in range(elements_in_line)]
		totalRegisteredDevices7 = [0 for i in range(elements_in_line)]
		totalDownlinkSC7 = [0 for i in range(elements_in_line)]
		totalUplinkSC7 = [0 for i in range(elements_in_line)]
	element_index = 0
	for lineIndex in range(0, len(lines), 2):
		totalDevices7[element_index] = float(lines[lineIndex].split('|')[0]) + totalDevices7[element_index]
		maxSym7[element_index] = float(lines[lineIndex].split('|')[1]) + maxSym7[element_index]
		maxSC7[element_index] = float(lines[lineIndex].split('|')[2]) + maxSC7[element_index]
		totalCollisionsNetwork7[element_index] = float(lines[lineIndex].split('|')[3]) + totalCollisionsNetwork7[element_index]
		totalCollisions24Band7[element_index] = float(lines[lineIndex].split('|')[4]) + totalCollisions24Band7[element_index]
		totalCollisions7[element_index] = float(lines[lineIndex].split('|')[5]) + totalCollisions7[element_index]
		totalEnergyNetwork7[element_index] = float(lines[lineIndex].split('|')[6]) + totalEnergyNetwork7[element_index]
		totalEnergy24Band7[element_index] = float(lines[lineIndex].split('|')[7]) + totalEnergy24Band7[element_index]
		totalEnergy7[element_index] = float(lines[lineIndex].split('|')[8]) + totalEnergy7[element_index]
		totalEnergyGNB7[element_index] = float(lines[lineIndex].split('|')[9]) + totalEnergyGNB7[element_index]
		totalTimeForRegistration7[element_index] = float(lines[lineIndex].split('|')[10])/1000 + totalTimeForRegistration7[element_index]
		totalRegisteredByGNB7[element_index] = float(lines[lineIndex].split('|')[11]) + totalRegisteredByGNB7[element_index]
		totalRegisteredByRelay7[element_index] = float(lines[lineIndex].split('|')[12]) + totalRegisteredByRelay7[element_index]
		totalRegisteredDevices7[element_index] = float(lines[lineIndex].split('|')[13]) + totalRegisteredDevices7[element_index]
		totalDownlinkSC7[element_index] = float(lines[lineIndex].split('|')[14]) + totalDownlinkSC7[element_index]
		totalUplinkSC7[element_index] = float(lines[lineIndex].split('|')[15]) + totalUplinkSC7[element_index]
		element_index += 1
	if index == len(iterations) - 1:
		for element_index in range(elements_in_line):
			totalDevices7[element_index] = int(totalDevices7[element_index]/len(iterations))
			maxSym7[element_index] = maxSym7[element_index]/len(iterations)
			maxSC7[element_index] = maxSC7[element_index]/len(iterations)
			totalCollisionsNetwork7[element_index] = totalCollisionsNetwork7[element_index]/len(iterations)
			totalCollisions24Band7[element_index] = totalCollisions24Band7[element_index]/len(iterations)
			totalCollisions7[element_index] = totalCollisions7[element_index]/len(iterations)
			totalEnergyNetwork7[element_index] = totalEnergyNetwork7[element_index]/len(iterations)
			totalEnergy24Band7[element_index] = totalEnergy24Band7[element_index]/len(iterations)
			totalEnergy7[element_index] = totalEnergy7[element_index]/len(iterations)
			totalEnergyGNB7[element_index] = totalEnergyGNB7[element_index] /len(iterations)
			totalTimeForRegistration7[element_index] = totalTimeForRegistration7[element_index]/len(iterations)
			totalRegisteredByGNB7[element_index] = totalRegisteredByGNB7[element_index]/len(iterations)
			totalRegisteredByRelay7[element_index] = totalRegisteredByRelay7[element_index]/len(iterations)
			totalRegisteredDevices7[element_index] = totalRegisteredDevices7[element_index]/len(iterations)
			totalDownlinkSC7[element_index] = totalDownlinkSC7[element_index]/len(iterations)
			totalUplinkSC7[element_index] = totalUplinkSC7[element_index]/len(iterations)

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalCollisions24Band, '-d', label='RACH')
plt.plot(totalDevices2, totalCollisions24Band2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalCollisions24Band3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalCollisions24Band4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalCollisions24Band5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Collisions in the 2.4 GHz band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/collisions_24.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalCollisionsNetwork, '-d', label='RACH')
plt.plot(totalDevices2, totalCollisionsNetwork2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalCollisionsNetwork3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalCollisionsNetwork4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalCollisionsNetwork5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Collisions in the Mobile Network band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/collisions_network.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalCollisions, '-d', label='RACH')
plt.plot(totalDevices2, totalCollisions2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalCollisions3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalCollisions4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalCollisions5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Total collisions (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/collisions_total.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalEnergy24Band, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergy24Band2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergy24Band3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergy24Band4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergy24Band5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Energy consumption in the 2.4 GHz band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/energy_24.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalEnergyNetwork, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergyNetwork2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergyNetwork3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergyNetwork4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergyNetwork5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Energy consumption in the Mobile Network band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/energy_network.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalEnergy, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergy2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergy3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergy4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergy5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Total energy consumption (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/energy_total.png')
plt.show()
#__________________________
plt.figure(figsize=(8, 8))
#plt.plot(totalDevices, totalEnergy, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergy2, '-o', label='Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergy3, '-v', label='Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergy4, '-s', label='Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergy5, '-x', label='Framework (before SIB1 + frequency assigned by gNB)')
#plt.yscale('log')
plt.title('Total energy consumption (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/energyTOTAL.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalEnergyGNB, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergyGNB2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergyGNB3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergyGNB4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergyGNB5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Energy consumption by the gNB')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/energy_gNB.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalTimeForRegistration, '-d', label='RACH')
plt.plot(totalDevices2, totalTimeForRegistration2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalTimeForRegistration5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Total time for all devices registration (ms)')
plt.ylabel('Time (ms)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/time.png')
plt.show()
#___________________________
plt.figure(figsize=(8, 8))
#plt.plot(totalDevices, totalTimeForRegistration, '-d', label='RACH')
plt.plot(totalDevices2, totalTimeForRegistration2, '-o', label='Framework (after SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration3, '-v', label='Framework (before SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration4, '-s', label='Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalTimeForRegistration5, '-x', label='Framework (before SIB1 + frequency assigned by gNB)')
#plt.yscale('log')
plt.title('Total time for all devices registration (ms)')
plt.ylabel('Time (ms)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/timeTOTAL.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices2, totalTimeForRegistration2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalTimeForRegistration5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Total time for all devices registration (ms) - Framework')
plt.ylabel('Time (ms)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/time_framework.png')
plt.show()

plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], [totalDownlinkSC[0] for i in range(9)], label='RACH')
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], totalDownlinkSC6, label='Framework')
for index, value in enumerate(totalDownlinkSC6):
    plt.text(index, value, str(int(value)))
plt.title('Total resources offered for downlink (Subcarriers) - 100 devices')
plt.xlabel('Number of subcarriers/Number of symbols')
plt.ylabel('Number of subcarriers offered')
plt.legend(loc='best', shadow=True)
plt.grid(True)
##########
plt.subplot(1, 2, 2)
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], [totalUplinkSC[0] for i in range(9)], label='RACH')
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], totalUplinkSC6, label='Framework')
for index, value in enumerate(totalUplinkSC6):
    plt.text(index, value, str(int(value)))
plt.title('Total resources offered for uplink (Subcarriers) - 100 devices')
plt.xlabel('Number of subcarriers/Number of symbols')
plt.ylabel('Number of subcarriers offered')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/resources_downlink_uplink_100_devices.png')
plt.show()
##########

plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], [totalDownlinkSC[9] for i in range(9)], label='RACH')
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], totalDownlinkSC7, label='Framework')
for index, value in enumerate(totalDownlinkSC7):
    plt.text(index, value, str(int(value)))
plt.title('Total resources offered for downlink (Subcarriers) - 1000 devices')
plt.xlabel('Number of subcarriers/Number of symbols')
plt.ylabel('Number of subcarriers offered')
plt.legend(loc='best', shadow=True)
plt.grid(True)
##########
plt.subplot(1, 2, 2)
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], [totalUplinkSC[9] for i in range(9)], label='RACH')
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], totalUplinkSC7, label='Framework')
for index, value in enumerate(totalUplinkSC7):
    plt.text(index, value, str(int(value)))
plt.title('Total resources offered for uplink (Subcarriers) - 1000 devices')
plt.xlabel('Number of subcarriers/Number of symbols')
plt.ylabel('Number of subcarriers offered')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!graphs_average/resources_downlink_uplink_1000_devices.png')
plt.show()
##########
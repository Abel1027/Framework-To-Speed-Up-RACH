import matplotlib.pyplot as plt
import os

if not os.path.isdir('!best_graphs'): os.mkdir('!best_graphs')

iterations = os.listdir('!best_logs')

histogramT = []
for index, iter_file in enumerate(iterations):
	file = open('!best_logs/' + iter_file + '/01-RACH.log')
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
		histogram = []
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
	if index == 0:
		for lineIndex in range(1, len(lines), 2):
			histogram.append(lines[lineIndex].split('\n')[0])
		histogramT.append(histogram)
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
	
	file = open('!best_logs/' + iter_file + '/02-Bluetooth28clock.log')
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
		histogram = []
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
	if index == 0:
		for lineIndex in range(1, len(lines), 2):
			histogram.append(lines[lineIndex].split('\n')[0])
		histogramT.append(histogram)
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

	file = open('!best_logs/' + iter_file + '/03-BluetoothRandom.log')
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
	
	file = open('!best_logs/' + iter_file + '/04-WiFi28clock.log')
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
	
	file = open('!best_logs/' + iter_file + '/05-WiFiRandom.log')
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

plt.figure(figsize=(10, 10))
hist_f_ = histogramT[0][-1].split('|')
hist_f_.pop(len(hist_f_)-1)
hist_f = [float(_)/1000 for _ in hist_f_]
plt.hist(hist_f, bins=len(hist_f))
plt.title('Histogram for device registration (100 devices) - RACH')
plt.xlabel('Timestamps where devices were registered (ms)')
plt.ylabel('Number of devices registered')
plt.grid(True)
plt.savefig('!best_graphs/hist_rach.png')
plt.savefig('!best_graphs/hist_rach.eps')
plt.show()

plt.figure(figsize=(10, 10))
hist_f_ = histogramT[1][-1].split('|')
hist_f_.pop(len(hist_f_)-1)
hist_f = [float(_)/1000 for _ in hist_f_]
plt.hist(hist_f, bins=len(hist_f))
plt.title('Histogram for device registration (100 devices) - Framework')
plt.xlabel('Timestamps where devices were registered (ms)')
plt.ylabel('Number of devices registered')
plt.grid(True)
plt.savefig('!best_graphs/hist_framework.png')
plt.savefig('!best_graphs/hist_framework.eps')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalCollisions24Band, '-d', label='RACH')
plt.plot(totalDevices2, totalCollisions24Band2, '-o', label='Framework (Bluetooth 28-bit clock)')
plt.plot(totalDevices2, totalCollisions24Band3, '-v', label='Framework (Bluetooth random)')
plt.plot(totalDevices2, totalCollisions24Band4, '-s', label='Framework (Wi-Fi 28-bit clock)')
plt.plot(totalDevices2, totalCollisions24Band5, '-x', label='Framework (Wi-Fi random)')
plt.yscale('log')
plt.title('Collisions in the 2.4 GHz band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!best_graphs/collisions_24.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalCollisionsNetwork, '-d', label='RACH')
plt.plot(totalDevices2, totalCollisionsNetwork2, '-o', label='Framework (Bluetooth 28-bit clock)')
plt.plot(totalDevices2, totalCollisionsNetwork3, '-v', label='Framework (Bluetooth random)')
plt.plot(totalDevices2, totalCollisionsNetwork4, '-s', label='Framework (Wi-Fi 28-bit clock)')
plt.plot(totalDevices2, totalCollisionsNetwork5, '-x', label='Framework (Wi-Fi random)')
plt.yscale('log')
plt.title('Collisions in the Mobile Network band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!best_graphs/collisions_network.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalCollisions, '-d', label='RACH')
plt.plot(totalDevices2, totalCollisions2, '-o', label='Framework (Bluetooth 28-bit clock)')
plt.plot(totalDevices2, totalCollisions3, '-v', label='Framework (Bluetooth random)')
plt.plot(totalDevices2, totalCollisions4, '-s', label='Framework (Wi-Fi 28-bit clock)')
plt.plot(totalDevices2, totalCollisions5, '-x', label='Framework (Wi-Fi random)')
plt.yscale('log')
plt.title('Total collisions (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!best_graphs/collisions_total.png')
plt.savefig('!best_graphs/collisions_total.eps')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalEnergy24Band, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergy24Band2, '-o', label='Framework (Bluetooth 28-bit clock)')
plt.plot(totalDevices2, totalEnergy24Band3, '-v', label='Framework (Bluetooth random)')
plt.plot(totalDevices2, totalEnergy24Band4, '-s', label='Framework (Wi-Fi 28-bit clock)')
plt.plot(totalDevices2, totalEnergy24Band5, '-x', label='Framework (Wi-Fi random)')
plt.yscale('log')
plt.title('Energy consumption in the 2.4 GHz band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!best_graphs/energy_24.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalEnergyNetwork, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergyNetwork2, '-o', label='Framework (Bluetooth 28-bit clock)')
plt.plot(totalDevices2, totalEnergyNetwork3, '-v', label='Framework (Bluetooth random)')
plt.plot(totalDevices2, totalEnergyNetwork4, '-s', label='Framework (Wi-Fi 28-bit clock)')
plt.plot(totalDevices2, totalEnergyNetwork5, '-x', label='Framework (Wi-Fi random)')
plt.yscale('log')
plt.title('Energy consumption in the Mobile Network band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!best_graphs/energy_network.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalEnergy, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergy2, '-o', label='Framework (Bluetooth 28-bit clock)')
plt.plot(totalDevices2, totalEnergy3, '-v', label='Framework (Bluetooth random)')
plt.plot(totalDevices2, totalEnergy4, '-s', label='Framework (Wi-Fi 28-bit clock)')
plt.plot(totalDevices2, totalEnergy5, '-x', label='Framework (Wi-Fi random)')
plt.yscale('log')
plt.title('Total energy consumption (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!best_graphs/energy_total.png')
plt.savefig('!best_graphs/energy_total.eps')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalEnergyGNB, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergyGNB2, '-o', label='Framework (Bluetooth 28-bit clock)')
plt.plot(totalDevices2, totalEnergyGNB3, '-v', label='Framework (Bluetooth random)')
plt.plot(totalDevices2, totalEnergyGNB4, '-s', label='Framework (Wi-Fi 28-bit clock)')
plt.plot(totalDevices2, totalEnergyGNB5, '-x', label='Framework (Wi-Fi random)')
plt.yscale('log')
plt.title('Energy consumption by the gNB')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!best_graphs/energy_gNB.png')
plt.savefig('!best_graphs/energy_gNB.eps')
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(totalDevices, totalTimeForRegistration, '-d', label='RACH')
plt.plot(totalDevices2, totalTimeForRegistration2, '-o', label='Framework (Bluetooth 28-bit clock)')
plt.plot(totalDevices2, totalTimeForRegistration3, '-v', label='Framework (Bluetooth random)')
plt.plot(totalDevices2, totalTimeForRegistration4, '-s', label='Framework (Wi-Fi 28-bit clock)')
plt.plot(totalDevices2, totalTimeForRegistration5, '-x', label='Framework (Wi-Fi random)')
plt.yscale('log')
plt.title('Total time for all devices registration (ms)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Time (ms)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('!best_graphs/time.png')
plt.savefig('!best_graphs/time.eps')
plt.show()
import simpy
import numpy as np
import random
import pandas as pd
import os

def gNB(env, mnPower, timeResolution=31.25, totalNetworkSlices=1, printLogs=False):
	# gNB Configuration
	global totalDev
	global totalRegisteredDevices
	global totalEnergyGNB
	global collisionList
	global collisionListBand24
	global commonDownlinkBW
	global commonUplinkBW
	global downlinkRRC
	global uplinkRRC
	global downlinkBW
	global uplinkBW
	global randomRA_RNTI
	global randomValueForAccess
	randomValueForAccess = 0.8
	RRCPendingList = []
	RACHPendingList = []
	SIB1Periodicity = 5*1000 # 5000us = 5ms (minimum periodicity of SIB1 {5ms, 10ms, 20ms, 40ms, 80ms, 160ms})
	global numerologySlot
	numerologySlot = 66.67 # 66.67us -> slot time for 15kHz numerology
	TTLRar = numerologySlot # (minimum ra-responseWindow interval {sl1, sl2, sl4, sl8, sl10, sl20, sl40, sl80})
	RRCInterval = numerologySlot #interval to listen to RRC Connection Requests
	resourceAllocationTable = np.array(('RA-RNTI', 'T/C-RNTI', 'RB_dl', 'SC_dl', 'L_dl', 'S_dl', 'RB_ul', 'SC_ul', 'L_ul', 'S_ul', 'TTL')) # initializing the resource allocation table
	resourceAllocationTable = np.reshape(resourceAllocationTable, (1, len(resourceAllocationTable)))
	
	#gNB Tasks
	SIB1Timer = 0
	global symbolCounter # global to be used by every device (14 symbols)
	symbolCounter = 0 # this counter is used to count 14 symbols and restart again, this is a time-domain counter
	global slotCounter # global to be used by every device (80 slots) 
	slotCounter = 0 # this counter is used to count 80 slots and restart again, this is a time-domain counter
	while totalRegisteredDevices < totalDev:
		newTC_RNTIList = [int(tc.split('|')[-1]) for tc in RACHPendingList]
		# every 5ms sends SIB1
		if env.now - SIB1Timer >= SIB1Periodicity:
			SIB1Timer = env.now
			if printLogs == True: print(env.now, 'us: gNB -> Sending SIB1')
			totalEnergyGNB += mnPower
			#print(env.now, 'us: gNB -> Sending SIB1')
			commonDownlinkBW[0] = [i for i in range(64)] # sending 64 preambles within SIB1

		# checks common uplink bandwidth to find Random-Access requests
		randomValueForAccessC = 0
		for channelIndex in range(len(commonUplinkBW)):
			if commonUplinkBW[channelIndex] != 'None':
				randomValueForAccessC += 1
				# Random-Access request data has the format: RA-RNTI|preamble
				RA_RNTI = commonUplinkBW[channelIndex].split('|')[0] + '_0'
				TC_RNTI_List = []
				# saving all TC_RNTI in a list to compare later
				for lookup in range(1, resourceAllocationTable.shape[0]):
					TC_RNTI_List.append(resourceAllocationTable[lookup, 1])
				TC_RNTI_Status = False
				while TC_RNTI_Status == False:
					TC_RNTI = random.randint(0, 65535) # random number in interval {0, 65535}
					if str(TC_RNTI) not in TC_RNTI_List and TC_RNTI not in newTC_RNTIList:
						TC_RNTI_Status = True
						newTC_RNTIList.append(TC_RNTI)
				TTL = env.now
				# adding new device to resource allocation table
				new_requester_row = np.array((RA_RNTI, TC_RNTI, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', TTL))
				resourceAllocationTable = np.vstack([resourceAllocationTable, new_requester_row])
				# sends RAR
				RACHPendingList.append(RA_RNTI + '|' + commonUplinkBW[channelIndex].split('|')[1] + '|' + str(TC_RNTI))
		if randomValueForAccessC > 0:
			# adaptates the randomValueForAccess in the interval 0.2-0.8, 
			# if there are 64 received preambles the randomValueForAccess is equal to 0.2, 
			# if there are 0 received preambles the randomValueForAccess is equal to 0.8
			randomValueForAccess = 1-(0.6/64*randomValueForAccessC + 0.2)
			print(env.now, 'gNB -> ', randomValueForAccessC, ' Preambles Received - New Random Access Value=' + str(randomValueForAccess))

		# checks uplink to find forwarded message by a relay from a requester
		# if there are registered relays in the resource allocation table...
		if resourceAllocationTable.shape[0] > 1:
			# for each possible relay...
			data_to_concatenate_with_RAT = []
			for lookup in range(1, resourceAllocationTable.shape[0]):
				if resourceAllocationTable[lookup, 7] != 'None': # if this device has resources allocated for uplink... 
					subcarrierToLookUpInUplink = int(resourceAllocationTable[lookup, 7].split('-')[0]) # gets SC_ul (uplink subcarrier) where the gNB will look up for relay transmission
					#symbolToLookUpUplink = int(resourceAllocationTable[lookup, 9]) # index of the first symbol to look up for relay
					if len(uplinkBW) > 0 and uplinkBW[subcarrierToLookUpInUplink] != 'None':
						# there is data from this relay
						# data has the format: RA-RNTI|SC_dl|SC_ul|NoSym_dl|NoSym_ul
						if uplinkBW[subcarrierToLookUpInUplink] not in data_to_concatenate_with_RAT: # saves only data not repeated
							data_to_concatenate_with_RAT.append(uplinkBW[subcarrierToLookUpInUplink]) # save every relay transmission to concatenate with resource allocation table at the end of this iteration
			if len(data_to_concatenate_with_RAT) > 0: # if there are transmissions from relays saved
				for data in data_to_concatenate_with_RAT:
					# new data from requester to include at the end of the resource allocation table
					for lookup in range(1, resourceAllocationTable.shape[0]):
						if data.split('|')[0] == resourceAllocationTable[lookup, 0]:
							break
					else:
						# if this RA-RNTI is not in resource allocation table includes this requester data in resource allocation table
						RA_RNTI = data.split('|')[0] + '_1'
						TC_RNTI_List = []
						# saving all TC_RNTI in a list to compare later
						for lookup in range(1, resourceAllocationTable.shape[0]):
							TC_RNTI_List.append(resourceAllocationTable[lookup, 1])
						TC_RNTI_Status = False
						while TC_RNTI_Status == False:
							TC_RNTI = random.randint(0, 65535) # random number in interval {0, 65535}
							if str(TC_RNTI) not in TC_RNTI_List and TC_RNTI not in newTC_RNTIList:
								TC_RNTI_Status = True
								newTC_RNTIList.append(TC_RNTI)
						RB_dl = str(int(int(data.split('|')[1])/12))
						RB_ul = str(int(int(data.split('|')[2])/12))
						L_dl = data.split('|')[3]
						L_ul = data.split('|')[4]
						TTL = env.now
						# adding new device to resource allocation table
						new_requester_row = np.array((RA_RNTI, TC_RNTI, RB_dl, 'None', L_dl, 'None', RB_ul, 'None', L_ul, 'None', TTL))
						resourceAllocationTable = np.vstack([resourceAllocationTable, new_requester_row])
						RACHPendingList.append(RA_RNTI + '|' + str(TC_RNTI))

			# checks if TTL has timed up for every requester in the resource allocation table when RRC Connection Request is expected
			rowToDelete = []
			for lookup in range(1, resourceAllocationTable.shape[0]):
				if resourceAllocationTable[lookup, 3] == 'None' and env.now - float(resourceAllocationTable[lookup, 10]) >= TTLRar:
					# if TTL has timed up for this requester includes it in the removing list
					rowToDelete.append(lookup)
			if len(rowToDelete) > 0:
				for listIndex, row in enumerate(rowToDelete):
					resourceAllocationTable = np.delete(resourceAllocationTable, row - listIndex, 0)

		# checks if there are empty spaces in commonDownlinkBW to send pending RARs
		for channelIndex, channel in enumerate(commonDownlinkBW):
			if channelIndex > 0 and channel == 'None':
				if len(RACHPendingList) > 0:
					commonDownlinkBW[channelIndex] = RACHPendingList.pop(0)
					if printLogs == True: print(env.now, 'us: gNB -> Sending RAR to:', commonDownlinkBW[channelIndex])
					totalEnergyGNB += mnPower

		# checks RRC uplink to find RRC Connection Requests
		for channelIndex in range(len(uplinkRRC)):
			if uplinkRRC[channelIndex] != 'None':
				# RRC request data has the format: TC-RNTI|40-bitValue
				TC_RNTI = uplinkRRC[channelIndex].split('|')[0]
				# looking for this TC_RNTI in resource allocation table to check it is in the table
				for lookup in range(1, resourceAllocationTable.shape[0]):
					if TC_RNTI == resourceAllocationTable[lookup, 1]:
						if resourceAllocationTable[lookup, 0] != 'empty' and resourceAllocationTable[lookup, 0].split('_')[1] == '0' and resourceAllocationTable[lookup, 2] == 'None': # this means that the device executed Random-Access procedure
							# 1 RB will be allocated 
							TTL = env.now
							# looks for last device with allocated physical resources
							RB_dl_offered = 'None'
							RB_ul_offered = 'None'
							SC_dl_offered = ''
							SC_ul_offered = ''
							downlink_resources_found = False
							uplink_resources_found = False
							#downlink lookup
							for rowIndex in range(downlinkRB.shape[0]):
								if downlink_resources_found == False:
									symbolCounter = 0
									for columnIndex in range(downlinkRB.shape[1]):
											if downlinkRB[rowIndex, columnIndex] == 0.0:
												symbolCounter += 1
									if symbolCounter == 14:
										downlink_resources_found = True
										SC_dl_offered = rowIndex
							for i in range(14):
								downlinkRB[SC_dl_offered, i] = TC_RNTI
							#uplink lookup
							for rowIndex in range(uplinkRB.shape[0]):
								if uplink_resources_found == False:
									symbolCounter = 0
									for columnIndex in range(uplinkRB.shape[1]):
											if uplinkRB[rowIndex, columnIndex] == 0.0:
												symbolCounter += 1
									if symbolCounter == 14:
										uplink_resources_found = True
										SC_ul_offered = rowIndex
							for i in range(14):
								uplinkRB[SC_ul_offered, i] = TC_RNTI

							SC_dl_offered = str(SC_dl_offered*12) + '-' + str(SC_dl_offered*12 + 11)
							SC_ul_offered = str(SC_ul_offered*12) + '-' + str(SC_ul_offered*12 + 11)
							L_dl_offered = '14'
							L_ul_offered = '14'
							S_dl_offered = '0'
							S_ul_offered = '0'
							# allocating physical resources for this device
							resourceAllocationTable[lookup, 2] = RB_dl_offered
							resourceAllocationTable[lookup, 3] = SC_dl_offered
							resourceAllocationTable[lookup, 4] = L_dl_offered
							resourceAllocationTable[lookup, 5] = S_dl_offered
							resourceAllocationTable[lookup, 6] = RB_ul_offered
							resourceAllocationTable[lookup, 7] = SC_ul_offered
							resourceAllocationTable[lookup, 8] = L_ul_offered
							resourceAllocationTable[lookup, 9] = S_ul_offered
							resourceAllocationTable[lookup, 10] = TTL
							# sends RRC Connection Setup
							RRCPendingList.append('TC-RNTI=' + uplinkRRC[channelIndex].split('|')[0] + '|40-bitValue=' + uplinkRRC[channelIndex].split('|')[1] + '|SC_dl=' + SC_dl_offered + '|K0=0|S=' + S_dl_offered + '|L=' + resourceAllocationTable[lookup, 4] + '|SC_ul=' + SC_ul_offered + '|K2=0|S=' + S_ul_offered + '|L=' + resourceAllocationTable[lookup, 8])						
							# empty RA-RNTI from resource allocation table after resource assigment
							resourceAllocationTable[lookup, 0] = 'empty'
						elif resourceAllocationTable[lookup, 0] != 'empty' and resourceAllocationTable[lookup, 0].split('_')[1] == '1' and resourceAllocationTable[lookup, 3] == 'None': # this means that the device is a requester
							TTL = env.now
							# looks for all devices with allocated physical resources to check if this device resources requirements can be allocated in the same frequency resources
							RB_dl_offered = 'None'
							RB_ul_offered = 'None'
							RB_dl_wanted = int(resourceAllocationTable[lookup, 2])
							RB_ul_wanted = int(resourceAllocationTable[lookup, 6])
							L_dl_wanted = int(resourceAllocationTable[lookup, 4])
							L_ul_wanted = int(resourceAllocationTable[lookup, 8])
							downlink_resources_found = False
							uplink_resources_found = False
							#downlink lookup
							availableResources = 0
							for rowIndex in range(downlinkRB.shape[0]):
								for columnIndex in range(downlinkRB.shape[1]):
									if downlink_resources_found == False:
										if rowIndex+RB_dl_wanted <= downlinkRB.shape[0] and columnIndex+L_dl_wanted <= downlinkRB.shape[1]:
											block = downlinkRB[rowIndex:rowIndex+RB_dl_wanted, columnIndex:columnIndex+L_dl_wanted]
											for R in range(block.shape[0]):
												for S in range(block.shape[1]):
													if block[R, S] == 0.0:
														availableResources += 1
										if availableResources == RB_dl_wanted * L_dl_wanted:
											downlink_resources_found = True
											SC_dl_offered = str(rowIndex*12) + '-' + str(rowIndex*12 + RB_dl_wanted*12 - 1)
											SC_index = rowIndex
											S_dl_offered = str(columnIndex)
											S_index = columnIndex
										else:
											availableResources = 0
							for R in range(RB_dl_wanted):
								for S in range(L_dl_wanted):
									downlinkRB[SC_index + R, S_index + S] = TC_RNTI
							#uplink lookup
							availableResources = 0
							for rowIndex in range(uplinkRB.shape[0]):
								for columnIndex in range(uplinkRB.shape[1]):
									if uplink_resources_found == False:
										if rowIndex+RB_ul_wanted <= uplinkRB.shape[0] and columnIndex+L_ul_wanted <= uplinkRB.shape[1]:
											block = uplinkRB[rowIndex:rowIndex+RB_ul_wanted, columnIndex:columnIndex+L_ul_wanted]
											for R in range(block.shape[0]):
												for S in range(block.shape[1]):
													if block[R, S] == 0.0:
														availableResources += 1
										if availableResources == RB_ul_wanted * L_ul_wanted:
											uplink_resources_found = True
											SC_ul_offered = str(rowIndex*12) + '-' + str(rowIndex*12 + RB_ul_wanted*12 - 1)
											SC_index = rowIndex
											S_ul_offered = str(columnIndex)
											S_index = columnIndex
										else:
											availableResources = 0
							for R in range(RB_ul_wanted):
								for S in range(L_ul_wanted):
									uplinkRB[SC_index + R, S_index + S] = TC_RNTI
							# allocating physical resources for this device
							resourceAllocationTable[lookup, 2] = RB_dl_offered
							resourceAllocationTable[lookup, 3] = SC_dl_offered
							resourceAllocationTable[lookup, 5] = S_dl_offered
							resourceAllocationTable[lookup, 6] = RB_ul_offered
							resourceAllocationTable[lookup, 7] = SC_ul_offered
							resourceAllocationTable[lookup, 9] = S_ul_offered
							resourceAllocationTable[lookup, 10] = TTL
							# sends RRC Connection Setup
							RRCPendingList.append('TC-RNTI=' + uplinkRRC[channelIndex].split('|')[0] + '|40-bitValue=' + uplinkRRC[channelIndex].split('|')[1] + '|SC_dl=' + SC_dl_offered + '|K0=0|S=' + S_dl_offered + '|L=' + resourceAllocationTable[lookup, 4] + '|SC_ul=' + SC_ul_offered + '|K2=0|S=' + S_ul_offered + '|L=' + resourceAllocationTable[lookup, 8])
							# empty RA-RNTI from resource allocation table after resource assigment
							resourceAllocationTable[lookup, 0] = 'empty'
		
		# checks if there are empty spaces in downlinkRRC to send pending RRC Connection Setups
		for channelIndex, channel in enumerate(downlinkRRC):
			if channel == 'None':
				if len(RRCPendingList) > 0:
					downlinkRRC[channelIndex] = RRCPendingList.pop(0)
					if printLogs == True: print(env.now, 'us: gNB -> Sending RRC Connection Setup for:', downlinkRRC[channelIndex])
					totalEnergyGNB += mnPower

		#print(env.now, resourceAllocationTable)
		#print(downlinkRRC)

		symbolCounter += 1
		if symbolCounter > 13: 
			symbolCounter = 0
			slotCounter += 1
			if slotCounter > 80:
				slotCounter = 0

		randomRA_RNTI = random.randint(0, 19054)

		#############################################
		yield env.timeout(timeResolution) # time step
		#############################################

		# cleaning signals
		#print(env.now, 'CLEANED downlinkRRC and commonDownlinkBW by gNB')
		downlinkRRC = ['None' for i in range(64)]
		commonDownlinkBW = ['None' for i in range(65)]
		collisionList = [None for i in range(64)]
		collisionListBand24 = [None for i in range(totalNetworkSlices)]
		for bandIndex in range(len(collisionListBand24)):
			collisionListBand24[bandIndex] = [None for i in range(32)]

def device_configuration(status, max_num_bits):
	# set up binary clock
	if status == 'Requester':
		off = random.choice([0, 16]) # random 'off' for inquiring to simulate that devices inquire at different frequencies
	else:
		off = 0 # setting up 'off' to 0 (scanners always have off=0)
	clock = '0b'
	for i in range(max_num_bits):
		clock = clock + '0'

	slotTimer = 0
	slotNumber = -1

	start = 0

	return start, off, slotTimer, slotNumber, clock

def binary_to_decimal(b_num):
	return int(b_num, 2)

def decimal_to_binary(d_num):
	return bin(d_num)

def D2D_tx(env, index, band24, freq, status, network_slice, msg, printLogs):
	global collisionListBand24
	global totalCollisions24Band
	if band24[network_slice][freq] != 'None' or collisionListBand24[network_slice][freq] != None: # if there are transmissions in this channel (same network slice)...
		if printLogs == True: print(env.now, 'us: ' + status + ' (' + str(index) + '): Collision' + ' (Slice Group: ' + str(network_slice) + ')') # notify collision
		band24[network_slice][freq] = 'None' # free the channel
		collisionListBand24[network_slice][freq] = 'collision'
		totalCollisions24Band += 1
		return False
	else:
		if status == 'Requester':
			if printLogs == True: print(env.now, 'us: Requester (' + str(index) + '): Inquiry packet sent in frequency: ' + str(freq) + ' (Slice Group: ' + str(network_slice) + ')')
			band24[network_slice][freq] = 'inquiry_' + str(index) + '_' + msg
		else:
			if printLogs == True: print(env.now, 'us: Relay (' + str(index) + '): Response packet sent in frequency: ' + str(freq)  + ' (Slice Group: ' + str(network_slice) + ')')
			band24[network_slice][freq] = 'scan_' + str(index) + '_' + msg.split('|')[0]
		return True

def device(env, blePower, mnPower, timeResolution=31.25, index=0, status='Requester', totalNetworkSlices=1, discoverBeforeSIB1=False, backOff=False, framework=False, noClassicRACH=False, maxSym=14, maxSC=3, getFreqFromGNB=False, mobility=False, printLogs=False):
	# Device Configuration
	global commonDownlinkBW
	global commonUplinkBW
	global downlinkRRC
	global uplinkRRC
	global downlinkBW
	global uplinkBW
	global downlinkRB
	global uplinkRB
	global band24
	global randomRA_RNTI
	global symbolCounter
	global slotCounter
	global numerologySlot
	global collisionList
	global totalCollisionsNetwork
	global totalEnergyNetwork
	global totalEnergy24Band
	global totalTimeForRegistration
	global totalRegisteredDevices
	global totalRegisteredByGNB
	global totalRegisteredByRelay
	global totalDev
	global availableFreq24BandListening
	global registeredDevicesByTimestamp
	global randomValueForAccess
	network_slice = random.randint(0, totalNetworkSlices-1) # selects one of all possible coverage area slices
	slot = 312.5 # slot of 312.5us
	timeToResponse = slot*2 # 625us, time after the relay sends a response to the received inquiry packet (this time is necessary to synchronize relay transmission with requester reception)
	listenningInterval = timeResolution*360 # 11.25ms, duration of the listenning interval of the relay
	listennigWindow = 640000 # 0.64ms, listenning interval for relay
	listenningTimer = 0
	backOffTimer = 0
	backOffTimeOut = True
	RelayFoundTime = numerologySlot # (minimum ra-responseWindow interval {sl1, sl2, sl4, sl8, sl10, sl20, sl40, sl80}), ra-responseWindow (after relay found) = 5 slots (5*66.67us -> SCS 15 kHz)
	max_num_bits = 28 # 28-bit clock
	N = random.randint(-1, 30) # N selected by the relay for scanning
	signalTransmitted = False # this flag is used to clean the transmission in the last timeResolution step
	signalReceived = False # this flag is used to stop listen discovery messages when there is an already discovered message
	deviceConfigured = False
	txTogNBByRelay = False # this flag is used to clean the transmission in the uplinkBW (when is forwarded to the gNB a discovery message)
	prachTransmitted = False # this flag is used to clean the prach transmission in the commonUplinkBW
	preambleSelected = False
	stopPRACH = False
	ra_responseWindow = numerologySlot # (minimum ra-responseWindow interval {sl1, sl2, sl4, sl8, sl10, sl20, sl40, sl80})
	ra_responseWindowTimer = 0
	RRCRequestPRACH = False
	RRCRequestRelay = False
	sentRRCRequestPRACH = False
	sentRRCRequestRelay = False
	resourcesAllocated = 0 # number of times that were allocated resources
	stopDiscovery = False
	myULResourcesIndex = 0
	rrcReceived = False
	sib1arrived = False
	forwardMsg = False
	TacbFlag = False
	mobilityTimer = env.now
	mobilityTime = random.randint(160000, 1152000)*timeResolution # mobility every 5s - 36ms
	incomingMsgList = []
	noRACH = 0
	noRACHStored = 0

	################################
	# random start time in the simulation for every device between 0ms - 15ms
	start_back_off = random.randint(0, 480)
	yield env.timeout(timeResolution*start_back_off)
	################################

	if status == 'Requester':
		RA_RNTIRequester = str(random.randint(1, 65523))
		# msg = RA_RNTIRequester + '|SC_dl|SC_ul|NoSym_dl|NoSym_ul'
		rsc = str(random.randint(1, maxSC)*12) + '|' + str(random.randint(1, maxSC)*12) + '|' + str(random.randint(1, maxSym)) + '|' + str(random.randint(1, maxSym))
		msg = RA_RNTIRequester + '|' + rsc
		if printLogs == True: print(env.now, 'us: Device (' + str(index) + '): Requirements via Relay: ' + msg, '(Slice Group: ' + str(network_slice) + ')')
	RA_RNTI = ''
	TC_RNTIRequester = '' # TC-RNTI via relay
	TC_RNTI = '' # TC-RNTI via PRACH

	# Device Tasks
	while totalRegisteredDevices < totalDev:
		if status == 'Requester':
			if mobility == True and env.now - mobilityTimer >= mobilityTime:
				mobilityTimer = env.now
				mobilityTime = random.randint(160000, 1152000)*timeResolution # mobility every 5s - 36ms
				network_slice = network_slice + random.choice([-1, 1])
				if network_slice < 0:
					network_slice = totalNetworkSlices - 1
				elif network_slice >= totalNetworkSlices:
					network_slice = 0

			# checks SIB1 search space
			# if PRACH has not stopped and there are no selected preambles outside ra-responseWindow and there are available preambles (SIB1 received)...
			if TacbFlag == False and stopPRACH == False and preambleSelected == False and len(commonDownlinkBW[0]) == 64:
				if noRACH == 0:
					sib1arrived = True
					discoverBeforeSIB1 = True
					# generates a random uniform number between [0, 1]
					if noClassicRACH == True:
						accessNumber = 0
					else:
						accessNumber = random.randint(0, 100)*0.01 # 0.01 resolution
					if accessNumber < randomValueForAccess: # randomValueForAccess is the access number between [0, 1] sent by the gNB
						preambleSelected = True
						ra_responseWindowTimer = env.now
						preamble = random.choice(commonDownlinkBW[0]) # selects one preamble randomly
						s_id = symbolCounter
						t_id = slotCounter
						f_id = 0 # because is used FDD
						ul_carrier_id = 0 # no SUL carrier in this case, just pure NR
						RA_RNTI = str(1 + s_id + 14*t_id + 14*80*f_id + 14*80*8*ul_carrier_id)
						msgRACH = RA_RNTI + '|' + str(preamble)
						# sends PRACH request
						if commonUplinkBW[preamble] != 'None' or collisionList[preamble] != None:
							if printLogs == True: print(env.now, 'us: Device (' + str(index) + '): Collision in PRACH preamble=' + str(preamble)) # notify collision
							commonUplinkBW[preamble] = 'None'
							collisionList[preamble] = 'collision'
							totalCollisionsNetwork += 1
						else:
							if printLogs == True: print(env.now, 'us: Device (' + str(index) + ') sent PRACH in frequency (preamble)=' + str(preamble), 'PRACH MESSAGE:', msgRACH)
							commonUplinkBW[preamble] = msgRACH
							prachTransmitted = True
						totalEnergyNetwork += mnPower
					else:
						TacbFlag = True
						TacbTimer = env.now
						Tacb = random.choice([4])#, 8, 16, 32, 64, 128, 256, 512])
						Tbarring = (0.7 + 0.6*random.randint(0, 100)*0.01)*Tacb
						print(env.now, 'Device (' + str(index) + ') prob=' + str(accessNumber) + ' selects Tbarring=' + str(Tbarring) + ' seconds')
				else:
					noRACH -= 1

			if TacbFlag == True and env.now - TacbTimer >= Tbarring*10**6: # converts Tbarring from seconds into us
				TacbFlag = False
				print(env.now, 'Device (' + str(index) + ') Tbarring END')

			# if ra-responseWindow has not finished, checks RAR search space
			if stopPRACH == False and preambleSelected == True and env.now - ra_responseWindowTimer < ra_responseWindow:
				# checks RAR search space
				for channelDBWIndex in range(1, len(commonDownlinkBW)):
					if commonDownlinkBW[channelDBWIndex] != 'None':
						if commonDownlinkBW[channelDBWIndex].split('|')[0].split('_')[0] == RA_RNTI and commonDownlinkBW[channelDBWIndex].split('|')[0].split('_')[1] == '0' and commonDownlinkBW[channelDBWIndex].split('|')[1] == str(preamble):
							# RAR acquired via PRACH
							if printLogs == True: print(env.now, 'us: ' + status + ' (' + str(index) + ') RAR received via PRACH, new TC_RNTI=' + commonDownlinkBW[channelDBWIndex].split('|')[2])
							TC_RNTI = commonDownlinkBW[channelDBWIndex].split('|')[2]
							randomValue = random.randint(0, 2**40 - 1) # TC_RNTI|40-bitValue
							stopPRACH = True
							break
			elif stopPRACH == False and preambleSelected == True and env.now - ra_responseWindowTimer >= ra_responseWindow:
				# ra-responseWindow has timed up and it must restart PRACH procedure
				preambleSelected = False
				RA_RNTI = ''
				preamble = ''
				noRACHStored += 1
				noRACH = random.randint(0, noRACHStored)
				#print(env.now, 'noRACH', noRACH)

			# checks RAR search space (via relay)
			if stopPRACH == False and sib1arrived == True: # only if SIB1 has been received the requester can listen to RAR because the device needs SIB1 information to receive RAR
				for channelDBWIndex in range(1, len(commonDownlinkBW)):
					if commonDownlinkBW[channelDBWIndex] != 'None':
						if commonDownlinkBW[channelDBWIndex].split('|')[0].split('_')[0] == RA_RNTIRequester and commonDownlinkBW[channelDBWIndex].split('|')[0].split('_')[1] == '1':
							# RAR acquired via relay
							if printLogs == True: print(env.now, 'us: ' + status + ' (' + str(index) + ') RAR received via RELAY, new TC_RNTI=' + commonDownlinkBW[channelDBWIndex].split('|')[1])
							TC_RNTIRequester = commonDownlinkBW[channelDBWIndex].split('|')[1]
							randomValueRequester = random.randint(0, 2**40 - 1) # TC_RNTI|40-bitValue
							stopPRACH = True
							stopDiscovery = True
							afterRelayFoundTimer = env.now
							break

			# if RAR has arrived for this device, sends RRC Connection Request
			if sentRRCRequestRelay == False and TC_RNTIRequester != '':
				for ulRRCIndex, ulRRCChannel in enumerate(uplinkRRC):
					if ulRRCChannel == 'None':
						uplinkRRC[ulRRCIndex] = TC_RNTIRequester + '|' + str(randomValueRequester) # TC_RNTI|40-bitValue
						RRCIndexRelay= ulRRCIndex
						RRCRequestRelay = True
						sentRRCRequestRelay = True
						afterRelayFoundTimer = env.now
						break
			if sentRRCRequestPRACH == False and stopPRACH == True:
				if TC_RNTI != '':
					for ulRRCIndex, ulRRCChannel in enumerate(uplinkRRC):
						if ulRRCChannel == 'None':
							uplinkRRC[ulRRCIndex] = TC_RNTI + '|' + str(randomValue) # TC_RNTI|40-bitValue
							RRCIndexPRACH = ulRRCIndex
							RRCRequestPRACH = True
							sentRRCRequestPRACH = True
							afterRelayFoundTimer = env.now
							break

			# checks RRC Connection Setup response
			if sentRRCRequestRelay == True:
				for dlRRCIndex, dlRRCChannel in enumerate(downlinkRRC):	
					if dlRRCChannel != 'None' and dlRRCChannel.split('|')[0].split('=')[1] == TC_RNTIRequester and dlRRCChannel.split('|')[1].split('=')[1] == str(randomValueRequester):
						if resourcesAllocated == 0:
							totalRegisteredByRelay += 1
							totalRegisteredDevices += 1
							resourcesAllocated += 1
							registeredDevicesByTimestamp.append(env.now)
							print(env.now, 'us: Registered', totalRegisteredDevices, 'of', totalDev, 'Device (' + str(index) + ') -> (Slice Group: ' + str(network_slice) + ')')
							if printLogs == True: print(env.now, 'us: ' + status + '(' + str(index) + ') RESOURCES ALLOCATED (via RELAY) quantity=' + str(resourcesAllocated) + ' :', dlRRCChannel)
							myULOfferedTotalResources = (int(dlRRCChannel.split('|')[6].split('=')[1].split('-')[1]) - int(dlRRCChannel.split('|')[6].split('=')[1].split('-')[0]) + 1)*int(dlRRCChannel.split('|')[9].split('=')[1]) # (SC_ul_max - SC_ul_min)*L_ul
							if printLogs == True: print('UL offered', myULOfferedTotalResources)
							myULResourcesIndex = int(dlRRCChannel.split('|')[6].split('=')[1].split('-')[0]) + int(dlRRCChannel.split('|')[8].split('=')[1])
							#a = input()
							status = 'Relay'
							rrcReceived = True
							totalTimeForRegistration = env.now
						break
			if sentRRCRequestPRACH == True:
				for dlRRCIndex, dlRRCChannel in enumerate(downlinkRRC):
					if dlRRCChannel != 'None' and dlRRCChannel.split('|')[0].split('=')[1] == TC_RNTI and dlRRCChannel.split('|')[1].split('=')[1] == str(randomValue):
						if resourcesAllocated == 0:
							totalRegisteredByGNB += 1
							totalRegisteredDevices += 1
							resourcesAllocated += 1
							registeredDevicesByTimestamp.append(env.now)
							print(env.now, 'us: Registered', totalRegisteredDevices, 'of', totalDev, 'Device (' + str(index) + ') -> (Slice Group: ' + str(network_slice) + ')')
							if printLogs == True: print(env.now, 'us: ' + status + '(' + str(index) + ') RESOURCES ALLOCATED (via PRACH) quantity=' + str(resourcesAllocated) + ' :', dlRRCChannel)
							myULOfferedTotalResources = (int(dlRRCChannel.split('|')[6].split('=')[1].split('-')[1]) - int(dlRRCChannel.split('|')[6].split('=')[1].split('-')[0]) + 1)*int(dlRRCChannel.split('|')[9].split('=')[1]) # (SC_ul_max - SC_ul_min)*L_ul
							if printLogs == True: print('UL offered', myULOfferedTotalResources)
							myULResourcesIndex = int(dlRRCChannel.split('|')[6].split('=')[1].split('-')[0]) + int(dlRRCChannel.split('|')[8].split('=')[1])
							myDLResourcesIndex = int(dlRRCChannel.split('|')[2].split('=')[1].split('-')[0]) + int(dlRRCChannel.split('|')[4].split('=')[1])
							#a = input()
							status = 'Relay'
							totalTimeForRegistration = env.now
						break
			# clean repeated resource allocation (resources were given twice, from PRACH and from Relay)
			if resourcesAllocated > 1:
				if printLogs == True: print(env.now, 'us: Device (' + str(index) + ') CLEANING DOUBLE ASSIGNED RESOURCES')
				resourcesAllocated -= 1
				downlinkRB[myDLResourcesIndex, :] = 0.0
				uplinkRB[myULResourcesIndex, :] = 0.0

			# Discovery Procedure
			if framework == True and discoverBeforeSIB1 == True and stopPRACH == False and backOffTimeOut == True and stopDiscovery == False:
				if deviceConfigured == False:
					deviceConfigured = True
					start, off, slotTimer, slotNumber, clock = device_configuration(status, max_num_bits)
				# every two slots the device selects two new frequencies based in the 28-bit clock
				if start == 0 or env.now - slotTimer >= slot:
					slotNumber += 1
					if slotNumber > 3: slotNumber = 0
					slotTimer = env.now
					if env.now - slotTimer == 0:
						'''
						if len(list(clock)) < max_num_bits + 2: # if clock is less than 28 characters because 0 at the left are omitted, fills with 0
							chunk = ''
							for j in range(max_num_bits + 2 - len(list(clock))):
								chunk = chunk + '0'
							clock = '0b' + chunk + clock.split('0b')[-1]
						CLK_16_12 = binary_to_decimal('0b' + clock[-17:-12])
						CLK_4_2_0 = binary_to_decimal('0b' + clock[-5:-2] + clock[-1])
						freq = (CLK_16_12 + off + (CLK_4_2_0 - CLK_16_12) % 16) % 32 # new frequency to use
						clock = decimal_to_binary(binary_to_decimal(clock) + 1)
						'''
						freq = random.randint(0, 31)

					# Inquiring only at the begining of the inquiring slot
					if slotNumber == 0 or slotNumber == 1:
						if printLogs == True: print(env.now, 'us: ' + status + ' (' + str(index) + ') -> Inquiring at frequency:', freq, '(Slice Group: ' + str(network_slice) + ')')
						signalTransmitted = D2D_tx(env, index, band24, freq, status, network_slice, msg, printLogs)
						totalEnergy24Band += blePower

				# Scanning every timeResolution within the scanning slot
				if slotNumber == 2 or slotNumber == 3:
					if printLogs == True: print(env.now, 'us: ' + status + ' (' + str(index) + ') -> Scanning at frequency:', freq, '(Slice Group: ' + str(network_slice) + ')')
					if band24[network_slice][freq] != 'None' and band24[network_slice][freq].split('_')[0] == 'scan' and band24[network_slice][freq].split('_')[2] == RA_RNTIRequester:
						if printLogs == True: print(env.now, 'us: RELAY FOUND (' + band24[network_slice][freq].split('_')[1] + ') !!! for ' + status + ' (' + RA_RNTIRequester + ')' + ' (Slice Group: ' + str(network_slice) + ')')
						#a = input()
						stopDiscovery = True
						deviceConfigured = False
						afterRelayFoundTimer = env.now

			# time to wait for RRC response after relay has been found or RAR is received, if no RRC response arrives, restarts discovery 
			if rrcReceived == False and stopDiscovery == True and env.now - afterRelayFoundTimer >= RelayFoundTime:
				sentRRCRequestPRACH = False
				sentRRCRequestRelay = False
				TC_RNTIRequester = ''
				stopDiscovery = False
				stopPRACH = False
				# this speed up the relay procedure
				RA_RNTIRequester = str(random.randint(1, 65523))
				msg = RA_RNTIRequester + '|' + rsc # new RA_RNTI included
				if printLogs == True: print(env.now, 'us: Device (' + str(index) + '): Requirements via Relay (NEW RA_RNTI): ' + msg)

		if status == 'Relay':
			if deviceConfigured == False:
				deviceConfigured = True
				start, off, slotTimer, slotNumber, clock = device_configuration(status, max_num_bits)
				if getFreqFromGNB == True:
					freq = availableFreq24BandListening[network_slice]
					if availableFreq24BandListening[network_slice] == 31:
						availableFreq24BandListening[network_slice] = 0
					else:
						availableFreq24BandListening[network_slice] = availableFreq24BandListening[network_slice] + 1
			# every 0.64s the device selects a new frequency to listen to new discovery messages
			if start == 0 or env.now - slotTimer >= listennigWindow:
				start = 1
				slotTimer = env.now
				listenningTimer = env.now
				if getFreqFromGNB == False:
					if len(list(clock)) < max_num_bits + 2: # if clock is less than 28 characters because 0 at the left are omitted, fills with 0
						chunk = ''
						for j in range(max_num_bits + 2 - len(list(clock))):
							chunk = chunk + '0'
						clock = '0b' + chunk + clock.split('0b')[-1]
					CLK_16_12 = binary_to_decimal('0b' + clock[-17:-12])
					if clock[-1] == '0':
						N += 1
						if N == 32: N = 0 # reseting the clock after 32 frequencies scan
					freq = (CLK_16_12 + N) % 32
					clock = decimal_to_binary(binary_to_decimal(clock) + 2)
			#print(env.now, index, freq,'relay')

			if start == 0 or env.now - listenningTimer <= listenningInterval:
				# Listens to discovery messages in 2.4GHz band
				if signalReceived == False and band24[network_slice][freq] != 'None' and band24[network_slice][freq].split('_')[0] == 'inquiry':
					incomingMsg = band24[network_slice][freq].split('_')[2]
					msgToForward = band24[network_slice][freq]
					msgRequester = band24[network_slice][freq].split('_')[1]
					msgTimestamp = env.now
					if printLogs == True: print(env.now, 'us: ' + status + ' (' + str(index) + ') DISCOVERY SIGNAL ARRIVED in freq=' + str(freq) + ', (Slice Group: ' + str(network_slice) + ')')
					frequencyForResponse = freq
					indexForResponse = index
					signalReceived = True

					# max number of bits of a discovery message: 38 bits = 16 bits (RA_RNTI) + 10 bits (cellID) + 2 bits (SC_dl=12,24,36,48) + 2 bits (SC_ul=12,24,36,48) + 4 bits (NoSym_dl) + 4 bits (NoSym_ul)
					if 38/myULOfferedTotalResources < 1:
						numberOfWaitingSlotsToForward = 0
					else:
						numberOfWaitingSlotsToForward = np.ceil(float(38/myULOfferedTotalResources))*timeResolution

					forwardMsg = True

			# forwards discovery message after numberOfWaitingSlotsToForward slot, 
			# this is used to simulate that the gNB receives more than one transmission
			# when the number of resources for thsi relay is less than the number of bits of the discovery message
			if forwardMsg == True and env.now - msgTimestamp >= numberOfWaitingSlotsToForward:
				forwardMsg = False
				# forwards discovery message to gNB
				if printLogs == True: print(env.now, 'us: ' + status + ' (' + str(index) + ') FORWARDED message to gNB for Requester (' + msgRequester + '): ' + msgToForward)
				uplinkBW[myULResourcesIndex] = incomingMsg # sending discovery message to gNB
				txTogNBByRelay = True
				totalEnergyNetwork += mnPower

			# if there is a discovery message received and an elapsed time of 625us=2slots, sends the response message
			if signalReceived == True and env.now - msgTimestamp >= timeToResponse:
				signalReceived = False
				# sent back a response for the discovery message
				signalTransmitted = D2D_tx(env, index, band24, frequencyForResponse, status, network_slice, incomingMsg, printLogs)
				totalEnergy24Band += blePower

		#############################################
		yield env.timeout(timeResolution) # time step
		#############################################

		# generating random back-off after 11.25ms to avoid collisions 
		# (This solves the collision problem when more than one requester selects the same RA_RNTI, 
		# because this gives different transmission times for them after back-off)
		if stopDiscovery == False and backOffTimeOut == True and stopPRACH == False and status == 'Requester' and backOff == True and env.now - backOffTimer >= listenningInterval:
			# after 11.25ms generates backoff
			backOffTimeOut = False
			backOffTimer = env.now
			back_off = random.randint(0, 10)
			if printLogs == True: print(env.now, status + ' (' + str(index) + ') BACK-OFF=' + str(timeResolution*back_off) + ' (Slice Group: ' + str(network_slice) + ')')
			backOffReqTimer = timeResolution*back_off

		if backOffTimeOut == False and env.now - backOffTimer >= backOffReqTimer:
			backOffTimeOut = True
			backOffTimer = env.now

		# cleaning signals
		if signalTransmitted == True:
			if printLogs == True: print(env.now, 'us: CLEANED by ' + status + ' (' + str(index) + ')'  + ' (Slice Group: ' + str(network_slice) + ')')
			signalTransmitted = False
			band24[network_slice][freq] = 'None'

		if txTogNBByRelay == True:
			if printLogs == True: print(env.now, 'us: CLEANED by ' + status + ' (' + str(index) + ')')
			txTogNBByRelay = False
			uplinkBW[myULResourcesIndex] = 'None'

		if prachTransmitted == True:
			prachTransmitted = False
			commonUplinkBW[preamble] = 'None'

		if RRCRequestPRACH == True:
			RRCRequestPRACH = False
			uplinkRRC[RRCIndexPRACH] = 'None'

		if RRCRequestRelay == True:
			RRCRequestRelay = False
			uplinkRRC[RRCIndexRelay] = 'None'

def main(totalDevices, framework, noClassicRACH, discoverBeforeSIB1, totalNetworkSlices, maxSym, maxSC, blePower, mnPower, getFreqFromGNB, mobility, printLogs, seed):
	# METRICS FOR COMPARISON
	global totalCollisionsNetwork; totalCollisionsNetwork = 0
	global totalCollisions24Band; totalCollisions24Band = 0
	global totalEnergyNetwork; totalEnergyNetwork = 0
	global totalEnergy24Band; totalEnergy24Band = 0
	global totalEnergyGNB; totalEnergyGNB = 0
	global totalTimeForRegistration; totalTimeForRegistration = 0
	global totalRegisteredDevices; totalRegisteredDevices = 0
	global totalRegisteredByGNB; totalRegisteredByGNB = 0
	global totalRegisteredByRelay; totalRegisteredByRelay = 0
	global registeredDevicesByTimestamp; registeredDevicesByTimestamp = []

	global totalDev
	totalDev = totalDevices

	maxNumberOfSubcarriersForDevice = 36
	maxNumberOfSymbolsInFrame = 14
	random.seed(seed) # seed used to replicate random numbers
	timeResolution = 31.25 # resolution of 31.25us
	endTime = 2*10**6 # simulation ends after 2*10**6us = 2s
	global numerologySlot
	numerologySlot = 66.67
	global randomRA_RNTI
	global commonDownlinkBW; commonDownlinkBW = ['None' for i in range(65)] # bandwidth where are transmitted SIB1 (chhanel 0), and RAR (channel 1-65)
	global commonUplinkBW; commonUplinkBW = ['None' for i in range(64)] # bandwidth where are transmitted Random-Access Requests (channel 0-64)
	global downlinkRRC; downlinkRRC = ['None' for i in range(totalDevices*maxNumberOfSubcarriersForDevice*maxNumberOfSymbolsInFrame)] # bandwidth where are transmitted RRC Connection Setup by gNB
	global uplinkRRC; uplinkRRC = ['None' for i in range(totalDevices*maxNumberOfSubcarriersForDevice*maxNumberOfSymbolsInFrame)] # bandwidth where are transmitted RRC Connection Request by devices
	global downlinkBW; downlinkBW = ['None' for i in range(totalDevices*maxNumberOfSubcarriersForDevice*maxNumberOfSymbolsInFrame)] # bandwidth where are allocated downlink resources 
	global uplinkBW; uplinkBW = ['None' for i in range(totalDevices*maxNumberOfSubcarriersForDevice*maxNumberOfSymbolsInFrame)] # bandwidth where are allocated uplink resources
	global band24; band24 = [None for i in range(totalNetworkSlices)] # bandwidth where are transmitted 2.4GHz signals
	for bandIndex in range(len(band24)):
		band24[bandIndex] = ['None' for i in range(32)]
	global downlinkRB
	global uplinkRB
	downlinkRB = np.zeros((totalDevices*maxNumberOfSubcarriersForDevice, 14)) # totalDevices*maxNumberOfSubcarriersForDevice subcarriers and 14 symbols for downlink
	uplinkRB = np.zeros((totalDevices*maxNumberOfSubcarriersForDevice, 14)) # totalDevices*maxNumberOfSubcarriersForDevice subcarriers and 14 symbols for uplink
	global collisionList 
	collisionList = [None for i in range(64)]
	global collisionListBand24
	collisionListBand24 = [None for i in range(totalNetworkSlices)]
	for bandIndex in range(len(collisionListBand24)):
		collisionListBand24[bandIndex] = [None for i in range(32)]
	global availableFreq24BandListening; availableFreq24BandListening = [0 for i in range(totalNetworkSlices)]

	env = simpy.Environment()
	for i in range(totalDevices):
		env.process(device(env=env, blePower=blePower, mnPower=mnPower, timeResolution=timeResolution, index=i, status='Requester', totalNetworkSlices=totalNetworkSlices, discoverBeforeSIB1=discoverBeforeSIB1, backOff=True, framework=framework, noClassicRACH=noClassicRACH, maxSym=maxSym, maxSC=maxSC, getFreqFromGNB=getFreqFromGNB, mobility=mobility, printLogs=printLogs))
	env.process(gNB(env=env, mnPower=mnPower, timeResolution=timeResolution, totalNetworkSlices=totalNetworkSlices, printLogs=printLogs))
	env.run()#until=endTime)

	# Total Resources Allocated
	if printLogs == True: print(downlinkRB)
	if printLogs == True: print(uplinkRB)
	pd.DataFrame(downlinkRB).to_csv('downlinkRB.csv')
	pd.DataFrame(uplinkRB).to_csv('uplinkRB.csv')

	totalDownlinkSC = 0
	for resourceRow in range(downlinkRB.shape[0]):
		for resourceColumn in range(downlinkRB.shape[1]):
			if downlinkRB[resourceRow][resourceColumn] != 0.0:
				totalDownlinkSC += 1
				break
	totalUplinkSC = 0
	for resourceRow in range(uplinkRB.shape[0]):
		for resourceColumn in range(uplinkRB.shape[1]):
			if uplinkRB[resourceRow][resourceColumn] != 0.0:
				totalUplinkSC += 1
				break

	# COMPARISON RESULTS
	print('Total collisions in the mobile network band:', totalCollisionsNetwork)
	print('Total collisions in the 2.4 GHz band:', totalCollisions24Band)
	print('TOTAL COLLISIONS:', totalCollisionsNetwork + totalCollisions24Band)
	print('Total energy spent by devices transmitting to the gNB:', totalEnergyNetwork, 'units')
	print('Total energy spent by devices transmitting in the 2.4 GHz band:', totalEnergy24Band, 'units')
	print('TOTAL ENERGY SPENT BY DEVICES:', totalEnergyNetwork + totalEnergy24Band, 'units')
	print('Total energy spent by the gNB:', totalEnergyGNB, 'units')
	print('TOTAL TIME FOR DEVICE REGISTRATION:', totalTimeForRegistration, 'us')
	print('Total devices registered by the gNB:', totalRegisteredByGNB)
	print('Total devices registered by relays:', totalRegisteredByRelay)
	print('TOTAL REGISTERED DEVICES:', totalRegisteredDevices, 'of', totalDevices)
	print('######################################################################\n')
	histogram = ''
	for timestamp in registeredDevicesByTimestamp:
		histogram = histogram + str(timestamp) + '|'
	return histogram, str(totalDevices) + '|' + str(maxSym) + '|' + str(maxSC) + '|' + str(totalCollisionsNetwork) + '|' + str(totalCollisions24Band) + '|' + str(totalCollisionsNetwork + totalCollisions24Band) + '|' + str(totalEnergyNetwork) + '|' + str(totalEnergy24Band) + '|' + str(totalEnergyNetwork + totalEnergy24Band) + '|' + str(totalEnergyGNB) + '|' + str(totalTimeForRegistration) + '|' + str(totalRegisteredByGNB) + '|' + str(totalRegisteredByRelay) + '|' + str(totalRegisteredDevices) + '|' + str(totalDownlinkSC) + '|' + str(totalUplinkSC)

if __name__ == '__main__':
	totalDevices = 100 # total number of devices that want to get resources from the network

	# FOR COMPARISON
	# pure RACH procedure (False) or using framework (True)
	framework = True
	# start discovery after receiving SIB1 (False) or before SIB1 (True)
	discoverBeforeSIB1 = False
	# total number of network slices (number of possible groups of D2D devices)
	#totalNetworkSlices = int(4.16*10**5/7853.98) # micro-cell coverage area (hexagonal -> a=400m) / bluetooth coverage area (circular -> radius=50m)
	totalNetworkSlices = int(4.16*10**5/31415.93) # micro-cell coverage area (hexagonal -> a=400m) / wifi coverage area (circular -> radius=100m)
	# maximum number of symbols a device can request to the network
	maxSym = 14
	# maximum number of subcarriers a device can request to the network
	maxSC = 3
	# listen only in the frequency the gNB dictates (True)
	getFreqFromGNB = False

	# Bluetooth transmission power (8dBm=0.0063095734448Watts)
	#blePower = int(0.0063095734448/0.0063095734448) # normalizing with 8dBm
	blePower = int(0.1/0.0063095734448) # normalizing with 8dBm (wifi=20dBm=100mWatts)
	# Mobile Network transmission power (24dBm=0.25118864315Watts)
	mnPower = int(0.25118864315/0.0063095734448) # normalizing with 8dBm

	# print logs in console (True)
	printLogs = False

	# devices can move from its D2D slice to neighbor slices (True)
	mobility = True

	# use classic RACH (False) or not (True)
	noClassicRACH = True

	# seed (random generator)
	seed = 0
	
	# for test
	#histogram, logs = main(totalDevices, framework, noClassicRACH, discoverBeforeSIB1, totalNetworkSlices, maxSym, maxSC, blePower, mnPower, getFreqFromGNB, mobility, printLogs, seed=seed)
	#print(logs)
	#print(histogram)

	for seed in range(10):
		if not os.path.isdir('!logs_for_average'): os.mkdir('!logs_for_average')
		if not os.path.isdir('!logs_for_average/logs' + str(seed)): os.mkdir('!logs_for_average/logs' + str(seed))
		
		############ 1 graph ############
		# 1. comparison by number of devices -> 
		# only RACH (without framework), 52 network slices, 14 symbols, 36 subcarriers
		
		for totalD in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
			print('1st graph (1) -> Devices:', totalD)
			histogram, logs = main(totalD, framework=False, noClassicRACH=False, discoverBeforeSIB1=False, totalNetworkSlices=totalNetworkSlices, maxSym=maxSym, maxSC=maxSC, blePower=blePower, mnPower=mnPower, getFreqFromGNB=False, mobility=False, printLogs=False, seed=seed)
			file = open('logs' + str(seed) + '/01.log', 'a')
			file.write(logs + '\n')
			file.write(histogram + '\n')
			file.close()
		
		# 2. comparison by number of devices -> 
		# RACH and framework (after SIB1 discovery), 52 network slices, 14 symbols, 36 subcarriers
		for totalD in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
			print('1st graph (2) -> Devices:', totalD)
			histogram, logs = main(totalD, framework=True, noClassicRACH=True, discoverBeforeSIB1=False, totalNetworkSlices=totalNetworkSlices, maxSym=maxSym, maxSC=maxSC, blePower=blePower, mnPower=mnPower, getFreqFromGNB=False, mobility=False, printLogs=False, seed=seed)
			file = open('!logs_for_average/logs' + str(seed) + '/02.log', 'a')
			file.write(logs + '\n')
			file.write(histogram + '\n')
			file.close()
		
		# 3. comparison by number of devices -> 
		# RACH and framework (before SIB1 discovery), 52 network slices, 14 symbols, 36 subcarriers
		for totalD in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
			print('1st graph (3) -> Devices:', totalD)
			histogram, logs = main(totalD, framework=True, noClassicRACH=True, discoverBeforeSIB1=True, totalNetworkSlices=totalNetworkSlices, maxSym=maxSym, maxSC=maxSC, blePower=blePower, mnPower=mnPower, getFreqFromGNB=False, mobility=False, printLogs=False, seed=seed)
			file = open('!logs_for_average/logs' + str(seed) + '/03.log', 'a')
			file.write(logs + '\n')
			file.write(histogram + '\n')
			file.close()

		# 4. comparison by number of devices -> 
		# RACH and framework (after SIB1 discovery) and frequencies for listening offered by the gNB, 52 network slices, 14 symbols, 36 subcarriers
		for totalD in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
			print('1st graph (4) -> Devices:', totalD)
			histogram, logs = main(totalD, framework=True, noClassicRACH=True, discoverBeforeSIB1=False, totalNetworkSlices=totalNetworkSlices, maxSym=maxSym, maxSC=maxSC, blePower=blePower, mnPower=mnPower, getFreqFromGNB=True, mobility=False, printLogs=False, seed=seed)
			file = open('!logs_for_average/logs' + str(seed) + '/04.log', 'a')
			file.write(logs + '\n')
			file.write(histogram + '\n')
			file.close()

		# 5. comparison by number of devices -> 
		# RACH and framework (before SIB1 discovery) and frequencies for listening offered by the gNB, 52 network slices, 14 symbols, 36 subcarriers
		for totalD in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
			print('1st graph (5) -> Devices:', totalD)
			histogram, logs = main(totalD, framework=True, noClassicRACH=True, discoverBeforeSIB1=True, totalNetworkSlices=totalNetworkSlices, maxSym=maxSym, maxSC=maxSC, blePower=blePower, mnPower=mnPower, getFreqFromGNB=True, mobility=False, printLogs=False, seed=seed)
			file = open('!logs_for_average/logs' + str(seed) + '/05.log', 'a')
			file.write(logs + '\n')
			file.write(histogram + '\n')
			file.close()
		#################################
		
		############ 2 graph ############
		# 6. comparison by maximum number of symbols and number of subcarriers -> 
		# 100 devices, RACH and framework (before SIB1 discovery), 52 network slices
		for maxS in [5, 10, 14]:
			for maxSc in [1, 2, 3]:
				print('2nd graph -> Subcarriers:', maxSc*12, 'Symbols:', maxS)
				histogram, logs = main(100, framework=True, noClassicRACH=True, discoverBeforeSIB1=True, totalNetworkSlices=totalNetworkSlices, maxSym=maxS, maxSC=maxSc, blePower=blePower, mnPower=mnPower, getFreqFromGNB=False, mobility=False, printLogs=False, seed=seed)
				file = open('!logs_for_average/logs' + str(seed) + '/06.log', 'a')
				file.write(logs + '\n')
				file.write(histogram + '\n')
				file.close()
		#################################

		############ 3 graph ############
		# 7. comparison by maximum number of symbols and number of subcarriers -> 
		# 1000 devices, RACH and framework (before SIB1 discovery), 52 network slices
		for maxS in [5, 10, 14]:
			for maxSc in [1, 2, 3]:
				print('3rd graph -> Subcarriers:', maxSc*12, 'Symbols:', maxS)
				histogram, logs = main(1000, framework=True, noClassicRACH=True, discoverBeforeSIB1=True, totalNetworkSlices=totalNetworkSlices, maxSym=maxS, maxSC=maxSc, blePower=blePower, mnPower=mnPower, getFreqFromGNB=False, mobility=False, printLogs=False, seed=seed)
				file = open('!logs_for_average/logs' + str(seed) + '/07.log', 'a')
				file.write(logs + '\n')
				file.write(histogram + '\n')
				file.close()
		#################################
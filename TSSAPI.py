# -*- coding: utf-8 -*-

########################################################
#                                                      #
#  ████████╗███████╗███████╗       █████╗ ██████╗ ██╗  #
#  ╚══██╔══╝██╔════╝██╔════╝      ██╔══██╗██╔══██╗██║  #
#     ██║   ███████╗███████╗█████╗███████║██████╔╝██║  #
#     ██║   ╚════██║╚════██║╚════╝██╔══██║██╔═══╝ ██║  #
#     ██║   ███████║███████║      ██║  ██║██║     ██║  #
#     ╚═╝   ╚══════╝╚══════╝      ╚═╝  ╚═╝╚═╝     ╚═╝  #
#                                                      #                          
#                          ***                         #
#  written by: xfl00d / jndok                          #
#  license: gnu/gpl v3                                 #
#                                                      #
#  iNeal API docs: https://api.ineal.me/tss/docs       # 
#                                                      #
########################################################

# quick documentation to this library:

# functions that begin with '_err' or '_check' are for error handling/error checking.
# functions that begin with a double underscore (__) are low-level functions.
# functions that begin with a sigle underscore (_) are wrappers.
# function without underscores are high-level functions.

# low-level: makes the request to the server and return the json.
# wrapper: packs the request in a dictionary/array or other data structures.
# high-level: interfaces with wrappers to get specific data, based on user input. Only these should be used to interface with the user.

# NOTE: Currently, only low-level functions and wrapper functions are implemented. I will update the library and add the other sets ASAP.

import requests
# from pprint import pprint // debug only

__all__ = ['__getAllCurrentlySignedFirmwares', '__getAllFirmwares', '__getAllCurrentlySignedFirmwaresForBoardConfig', '__getAllFirmwaresForBoardConfig',
		   '__getAllFirmwaresForBoardConfigAndBuildID', '__getAllCurrentlySignedBetaFirmwares', '__getAllBetaFirmwares', '__getAllCurrentlySignedBetaFirmwaresForBoardConfig',
		   '__getAllBetaFirmwaresForBoardConfig', '__getAllBetaFirmwaresForBoardConfigAndBuildID', '_wrapAllCurrentlySignedFirmwares', '_wrapAllFirmwares',
		   '_wrapAllCurrentlySignedFirmwaresForBoardConfig', '_wrapAllFirmwaresForBoardConfig', '_wrapAllFirmwaresForBoardConfigAndBuildID', '_wrapAllFirmwaresForBoardConfigAndBuildID', 
		   '_wrapAllCurrentlySignedBetaFirmwares', '_wrapAllBetaFirmwares', '_wrapAllCurrentlySignedBetaFirmwaresForBoardConfig', '_wrapAllBetaFirmwaresForBoardConfig', 
		   '_wrapAllBetaFirmwaresForBoardConfigAndBuildID', ]

def _errNotAValidJsonObject():
	print "[!] Could not decode JSON object. Make sure your query is valid."

# ****************** #

def __getAllCurrentlySignedFirmwares():		# gets all currently signed firmwares.
	r = requests.get('https://api.ineal.me/tss/all')
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

def __getAllFirmwares(): 	# gets all firmwares regardless of the signing state.	
	r = requests.get('https://api.ineal.me/tss/all/all')
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

def __getAllCurrentlySignedFirmwaresForBoardConfig(board_config): 	# gets all currently signed firmwares with a specific board configuration.
	r = requests.get('https://api.ineal.me/tss/{0}'.format(board_config))
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

def __getAllFirmwaresForBoardConfig(board_config): 	# gets all firmwares with a specific board configuration regardless of the signing state.
	r = requests.get('https://api.ineal.me/tss/{0}/all'.format(board_config))
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

def __getAllFirmwaresForBoardConfigAndBuildID(board_config, build_ID): 	# gets all firmwares with a specific board configuration / build ID combination.
	r = requests.get('https://api.ineal.me/tss/{0}/{1}'.format(board_config, build_ID))
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

# ****************** #

def __getAllCurrentlySignedBetaFirmwares():		# gets all currently signed firmwares.
	r = requests.get('https://api.ineal.me/tss/beta/all')
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

def __getAllBetaFirmwares(): 	# gets all firmwares regardless of the signing state.	
	r = requests.get('https://api.ineal.me/tss/beta/all/all')
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

def __getAllCurrentlySignedBetaFirmwaresForBoardConfig(board_config): 	# gets all currently signed firmwares with a specific board configuration.
	r = requests.get('https://api.ineal.me/tss/beta/{0}'.format(board_config))
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

def __getAllBetaFirmwaresForBoardConfig(board_config): 	# gets all firmwares with a specific board configuration regardless of the signing state.
	r = requests.get('https://api.ineal.me/tss/beta/{0}/all'.format(board_config))
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

def __getAllBetaFirmwaresForBoardConfigAndBuildID(board_config, build_ID): 	# gets all firmwares with a specific board configuration / build ID combination.
	r = requests.get('https://api.ineal.me/tss/beta/{0}/{1}'.format(board_config, build_ID))
	try:
		return r.json()
	except ValueError:
		_errNotAValidJsonObject()

# ****************** #

def _wrapAllCurrentlySignedFirmwares(): # packs devices IDs, devices properties and device firmwares data into three arrays and returns them. (only the ones with signed firmwares)
	json_data = __getAllCurrentlySignedFirmwares()
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

def _wrapAllFirmwares(): # packs devices IDs, devices properties and device firmwares data into three arrays and returns them.
	json_data = __getAllFirmwares()
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

def _wrapAllCurrentlySignedFirmwaresForBoardConfig(board_config):
	json_data = __getAllCurrentlySignedFirmwaresForBoardConfig(board_config)
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

def _wrapAllFirmwaresForBoardConfig(board_config):
	json_data = __getAllFirmwaresForBoardConfig(board_config)
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

def _wrapAllFirmwaresForBoardConfigAndBuildID(board_config, build_ID):
	json_data = __getAllFirmwaresForBoardConfigAndBuildID(board_config, build_ID)
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

# ****************** #

def _wrapAllCurrentlySignedBetaFirmwares(): # packs devices IDs, devices properties and device firmwares data into three arrays and returns them. (only the ones with signed firmwares)
	json_data = __getAllCurrentlySignedBetaFirmwares()
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

def _wrapAllBetaFirmwares(): # packs devices IDs, devices properties and device firmwares data into three arrays and returns them.
	json_data = __getAllBetaFirmwares()
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

def _wrapAllCurrentlySignedBetaFirmwaresForBoardConfig(board_config):
	json_data = __getAllCurrentlySignedBetaFirmwaresForBoardConfig(board_config)
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

def _wrapAllBetaFirmwaresForBoardConfig(board_config):
	json_data = __getAllBetaFirmwaresForBoardConfig(board_config)
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

def _wrapAllBetaFirmwaresForBoardConfigAndBuildID(board_config, build_ID):
	json_data = __getAllBetaFirmwaresForBoardConfigAndBuildID(board_config, build_ID)
	data = {}
	device_ids = []
	devices_data = []
	devices_firmwares = []

	device_ids = list(json_data.keys())	# gets all devices IDs into an array.
	for i in range(len(json_data)):	# gets all devices properties into an array.
		devices_data.append(json_data[json_data.keys()[i]])
	for i in range(len(devices_data)): # gets all devices firmwares into an array.
		devices_firmwares.append(json_data[json_data.keys()[i]]['firmwares'])

	return device_ids, devices_data, devices_firmwares

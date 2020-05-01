#https://github.com/SuperCowPowers/data_hacking/blob/master/clusterfck/clusterfck_pefile
#All the values appear to be saved in the list as Decimal (NOT HEX) may not matter...

import pefile
import os
def e_features(filename): #Extract the features from the given filename. Uses pefile to do the file parsing, only a subset of features are chosen from the parsed file
	features = {}
	try:
		pe = pefile.PE(filename, fast_load=False)

		# Basic Info
		features['Filename'] = os.path.basename(filename)
		features['Size'] = os.path.getsize(filename) # in bytes

		# Dos Header ?

		# File Header
		features['Machine'] = pe.FILE_HEADER.Machine
		features['NumberOfSections'] = pe.FILE_HEADER.NumberOfSections
		features['TimeDateStamp'] = pe.FILE_HEADER.TimeDateStamp
		features['PointerToSymbolTable'] = pe.FILE_HEADER.PointerToSymbolTable
		features['NumberOfSymbols'] = pe.FILE_HEADER.NumberOfSymbols
		features['SizeOfOptionalHeader'] = pe.FILE_HEADER.SizeOfOptionalHeader
		features['Characteristics'] = pe.FILE_HEADER.Characteristics # May be used to calculate flags
		# Flags ?

		# Optional Header
		features['Magic'] = pe.OPTIONAL_HEADER.Magic
		features['MajorLinkerVersion'] = pe.OPTIONAL_HEADER.MajorLinkerVersion
		features['MinorLinkerVersion'] = pe.OPTIONAL_HEADER.MinorLinkerVersion
		features['SizeOfCode'] = pe.OPTIONAL_HEADER.SizeOfCode
		features['SizeOfInitializedData'] = pe.OPTIONAL_HEADER.SizeOfInitializedData
		features['SizeOfUninitializedData'] = pe.OPTIONAL_HEADER.SizeOfUninitializedData
		features['AddressOfEntryPoint'] = pe.OPTIONAL_HEADER.AddressOfEntryPoint
		features['BaseOfCode'] = pe.OPTIONAL_HEADER.BaseOfCode
		#if hasattr(pe.OPTIONAL_HEADER, 'BaseOfData'): # not sure about this one
		#    features['BaseOfData'] = pe.OPTIONAL_HEADER.BaseOfData
		features['ImageBase'] = pe.OPTIONAL_HEADER.ImageBase
		features['SectionAlignment'] = pe.OPTIONAL_HEADER.SectionAlignment
		features['FileAlignment'] = pe.OPTIONAL_HEADER.FileAlignment
		features['MajorOperatingSystemVersion'] = pe.OPTIONAL_HEADER.MajorOperatingSystemVersion
		features['MinorOperatingSystemVersion'] = pe.OPTIONAL_HEADER.MinorOperatingSystemVersion
		features['MajorImageVersion'] = pe.OPTIONAL_HEADER.MajorImageVersion
		features['MinorImageVersion'] = pe.OPTIONAL_HEADER.MinorImageVersion
		features['MajorSubsystemVersion'] = pe.OPTIONAL_HEADER.MajorSubsystemVersion
		features['MinorSubsystemVersion'] = pe.OPTIONAL_HEADER.MinorSubsystemVersion
		features['SizeOfImage'] = pe.OPTIONAL_HEADER.SizeOfImage
		features['SizeOfHeaders'] = pe.OPTIONAL_HEADER.SizeOfHeaders
		features['CheckSum'] = pe.OPTIONAL_HEADER.CheckSum
		features['Subsystem'] = pe.OPTIONAL_HEADER.Subsystem
		features['DllCharacteristics'] = pe.OPTIONAL_HEADER.DllCharacteristics
		features['SizeOfStackReserve'] = pe.OPTIONAL_HEADER.SizeOfStackReserve
		features['SizeOfStackCommit'] = pe.OPTIONAL_HEADER.SizeOfStackCommit
		features['SizeOfHeapReserve'] = pe.OPTIONAL_HEADER.SizeOfHeapReserve
		features['SizeOfHeapCommit'] = pe.OPTIONAL_HEADER.SizeOfHeapCommit
		features['LoaderFlags'] = pe.OPTIONAL_HEADER.LoaderFlags
		features['NumberOfRvaAndSizes'] = pe.OPTIONAL_HEADER.NumberOfRvaAndSizes
		# DLL Characteristics ?

		# PE Sections
		#for section in pe.sections:
		#	if(section.Name == b'.text\x00\x00\x00' or section.Name == b'.data\x00\x00\x00' or section.Name == b'.rdata\x00\x00'):
		#		features[section.Name.decode('ascii')+'Size'] = section.SizeOfRawData
		#		features[section.Name.decode('ascii')+'Entropy'] = section.get_entropy()
		#		features[section.Name.decode('ascii')+'Characteristics'] = section.Characteristics # May be used to calculate flags
		# Flags ?

	except Exception as e:
		print("Error processing %s - %s" % (filename, str(e)))
		# print traceback.format_exc()
		return None
	# print(features)
	return features

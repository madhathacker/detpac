import os
import glob
import numpy as np
import pandas as pd
from clusterfck_pefile import e_features
from plot_features import feature_plot

def plot_features(names):
	features = []
	for name in names:
		features.append(df[name])
	feature_plot(features)
	return

def get_features(file_directory):
	features_list = []
	file_list = glob.glob(file_directory + '/*')
	for filename in file_list:
		if os.path.isfile(filename):
			#print(filename)
			#print(e_features(filename))
			file_features = e_features(filename)
			if file_features: #check for empty dictionaries (could not extract all features of file)
				features_list.append(file_features)
	return features_list

def save_features(directory, output):
	print('\033[34;1m Getting Features for '+directory+' ... \033[39;0m')
	features_list = get_features(directory)
	print('\033[34;1m Generating DataSet for '+directory+'... \033[39;0m')
	df = pd.DataFrame.from_records(features_list)
	if "packed" in directory:
		df["Packed"] = 1
	else:
		df["Packed"] = 0
	print(df)
	print('\033[34;1m Saving Dataset to: '+output+'... \033[39;0m')
	df.to_csv(output, sep=',', encoding='utf-8')
	#plot_features(['Size'])
	print('\033[32;1m DONE \033[39;0m')

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def main():
	data_directory = 'dataset' #change to path of binary files (packed & unpacked)
	for folder in os.listdir(data_directory+'/files'): #for all sets of binary files
		if folder+'.csv' in os.listdir(data_directory): #check if data set exists for the files
			print('\033[31;1m '+folder+'.csv exists!\033[39;0m')
			if not yes_or_no('Would you like to overwrite it?'):
				continue
		print('\033[32;1m Generating '+folder+'.csv\033[39;0m')
		save_features(data_directory+'/files/'+folder, data_directory+'/'+folder+'.csv')

if __name__=="__main__": 
    main() 

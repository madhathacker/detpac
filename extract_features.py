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
			if "packed" in filename:
				file_features["Packed"] = 1
			else:
				file_features["Packed"] = 0
			features_list.append(file_features)
	return features_list

print("\033[34;1m Getting features of unpacked binaries... \033[39;0m")
unpacked_features_list = get_features("dataset/binaries")
print("\033[34;1m Getting features of packed binaries... \033[39;0m")
packed_features_list = get_features("dataset/packed")
features_list = unpacked_features_list + packed_features_list

print("\033[34;1m Generating DataSet... \033[39;0m")
df = pd.DataFrame.from_records(features_list)
print(df)

print("\033[34;1m Saving Dataset to File... \033[39;0m")
df.to_csv('dataset.csv', sep=',', encoding='utf-8')

plot_features(['Size', 'TimeDateStamp'])

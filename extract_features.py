import os
import glob
import numpy as np
import pandas as pd
from clusterfck_pefile import e_features
from plot_features import feature_plot

def plot_feature(name):
	feature = df[name]
	#print(file_sizes)
	feature_plot(feature)

features_list = []

file_directory = "binaries"
file_list = glob.glob(file_directory + '/*')
for filename in file_list:
	if os.path.isfile(filename):
		#print(e_features(filename))
		features_list.append(e_features(filename))

df = pd.DataFrame.from_records(features_list)
df['Packed'] = False
print(df)

df.to_csv('dataset.csv', sep=',', encoding='utf-8')

plot_feature('Size')

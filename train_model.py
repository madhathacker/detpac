import glob
import pandas as pd
import sklearn as ske
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import tree

data_directory = 'dataset'
all_files = glob.glob(data_directory + "/*.csv")
li = []
for filename in all_files:
	df = pd.read_csv(filename, sep=',', index_col=0)
	#print(df)
	li.append(df)

Dataset = pd.concat(li, axis=0, ignore_index=True)
#print(Dataset)
Data = Dataset.drop(['Filename', 'Packed'], axis=1).to_numpy(dtype=int)
#print(Data)

Packed = Dataset['Packed'].values

FeatSelect = ske.ensemble.ExtraTreesClassifier().fit(Data, Packed) #fit data to Tree Classifier Model?
Model = SelectFromModel(FeatSelect, prefit=True)
Data_new = Model.transform(Data)

Unpacked_Train, Unpacked_Test, Packed_Train, Packed_Test = train_test_split(Data_new, Packed, shuffle=True, test_size=0.2)

Classifiers = {"DecisionTree":tree.DecisionTreeClassifier(), "RandomForest":ske.ensemble.RandomForestClassifier(n_estimators=100), "AdaBoost":ske.ensemble.AdaBoostClassifier(n_estimators=100)}

for Classif in Classifiers:
	clf = Classifiers[Classif]
	clf.fit(Unpacked_Train,Packed_Train)

	score = clf.score(Unpacked_Test, Packed_Test)
	print("The score of\033[93;1m %s \033[39;m:\033[36;1m %f %% \033[39;0m" % (Classif, score*100))
	
	Result = clf.predict(Unpacked_Test)
	CM = confusion_matrix(Packed_Test, Result)
	print("False positive rate : %f %%" % ((CM[0][1] / float(sum(CM[0])))*100))
	print('False negative rate : %f %%' % ( (CM[1][0] /float(sum(CM[1]))*100)))

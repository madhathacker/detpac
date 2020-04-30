import pandas as pd
import sklearn as ske
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import tree

Dataset = pd.read_csv('Dataset.csv', sep=',')
Data = Dataset.drop(['Name', 'Packed'], axis=1).values

Packed = Dataset['Packed'].values

FeatSelect = ske.ensemble.ExtraTreesClassifier().fit(Data, Packed)
Model = SelectFromModel(FeatSelect, prefit=True)
Data_new = Model.transform(Data)

Unpacked_Train, Unpacked_Test, Packed_Train, Packed_Test = train_test_split(Data_new, Packed, shuffle=True, test_size=0.2)

Classifiers = {"DecisionTree":tree.DecisionTreeClassifier(), "RandomForest":ske.ensemble.RandomForestClassifier(n_estimators=100), "AdaBoost":ske.ensemble.AdaBoostClassifier(n_estimators=100)}

for Classif in Classifiers:
	clf = Classifiers[Classif]
	clf.fit(Unpacked_Train,Packed_Train)

	score = clf.score(Unpacked_Test, Packed_Test)
	print("\033[34;1m The score of %s : %f %% \033[39;0m" % (Classif, score*100))
	
	Result = clf.predict(Unpacked_Test)
	CM = confusion_matrix(Packed_Test, Result)
	print("False positive rate : %f %%" % ((CM[0][1] / float(sum(CM[0])))*100))
	print('False negative rate : %f %%' % ( (CM[1][0] /float(sum(CM[1]))*100)))

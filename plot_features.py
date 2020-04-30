import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
sns.set(color_codes=True)

def feature_plot(features):
	plt.figure(figsize=(len(features)*3, 3))
	pos = 0
	for feature in features:
		plt.subplot(str(1)+str(len(features))+str(pos))
		pos += 1
		ax = sns.distplot(feature, kde=False, rug=False)
	plt.show()
	# plt.savefig("mygraph.png")
	return

#feature_plot([[0, 1, 4, 1, 1, 2, 3, 2], [2018, 2018, 2017, 2019, 2020, 2019]])

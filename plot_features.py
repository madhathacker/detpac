import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
sns.set(color_codes=True)

def feature_plot(features):
	plt.figure(figsize=(sizeof(features)*3, 3))
	pos = 0
	for feature in features:
		plt.subplot(1+sizeof(features)+pos)
		pos += 1
		ax = sns.distplot(features, kde=False, rug=False)
	plt.show()
	# plt.savefig("mygraph.png")
	return

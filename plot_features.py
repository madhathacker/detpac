import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
sns.set(color_codes=True)

def feature_plot(x):
	ax = sns.distplot(x, kde=False, rug=False)
	plt.show()
	# plt.savefig("mygraph.png")
	return

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
sns.set(color_codes=True)

def feature_plot(feature):
	x = np.random.normal(size=100)
	sns.distplot(x)
	plt.show()
	return

feature_plot(1)

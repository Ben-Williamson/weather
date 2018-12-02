import matplotlib.pyplot as plt


def create_graph(xdata, ydata, title, xlabel, ylabel, filename):
	plt.plot(ydata)
	plt.xticks(range(0, len(ydata)), xdata, rotation=45)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.grid(True)
	plt.tight_layout()
	plt.subplots_adjust(top=0.88)
	plt.savefig(filename, transparent=True)
	plt.close()
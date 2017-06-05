import numpy as np
def Mean_SD(values,freqs):
	values = np.array(values)
	freqs = np.array(freqs)
	count = np.sum(freqs)
	value_sum=np.sum(np.multiply(values,freqs))
	mean = value_sum/count
	diff_squared = np.square(values-mean)
	diff_squared = np.sum(np.multiply(diff_squared,freqs))
	SD = (diff_squared**.5)/count
	return [mean,SD]
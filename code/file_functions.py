def write(data, filename):
	with open(filename, "w+") as f:
		f.write(str(data))

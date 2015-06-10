def skew_index_set(genome):
	# Creates a dictionary of {index:skew} pairs for genome.
	# Dictionary represents skew at any given point in genome.
	skew_index = {0:0}
	c = 0
	g = 0
	for x in range(len(genome)):
		if genome[x] == "C":
			c += 1
		elif genome[x] == "G":
			g += 1
		skew = g - c
		skew_index[x+1] = skew
	return skew_index

# To generate the skew list (formatted)
formatted_num(skew_index_set(genome).values())	


def minimum_skew(d):
	print ' '.join(str(key) for min_value in (min(d.values()),) for key in d if d[key]==min_value)

# To get the indices of the minimum skew(s)
minimum_skew(skew_index_set(genome))
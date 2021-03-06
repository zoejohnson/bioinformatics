PYTHON:

def pattern_count(text, pattern):
# Search through a string (text) and count the frequency that
# another string (pattern) occurs.
	frequency = 0
	for x in range(len(text)):
		if text[x: x + len(pattern)] == pattern:
			frequency += 1
	return frequency


def keys_of_max_values(dictionary):
	count = 0
	keys_for_max_values = []
	for key in dictionary.keys():
		if dictionary[key] > count:
			count = dictionary[key]
			del keys_for_max_values[:]
			keys_for_max_values.append(key)
		elif dictionary[key] == count:
			keys_for_max_values.append(key)
	print keys_for_max_values

def which_values_are_t(dictionary, t):
	# Returns a list of keys whose values are at least t.
	keys = []
	for key in dictionary.keys():
		if dictionary[key] >= t:
			keys.append(key)
	print keys


def kmer_frequency(text, kmer_length):
# Creates a dictionary of {kmers in text: times they occur in text}
	kmers_counts = {}
	for x in range(len(text)-kmer_length):
		pattern = text[x:x + kmer_length]
		if pattern not in kmers_counts:
			frequency = pattern_count(text, pattern)
			kmers_counts[pattern] = frequency
		else:
			kmers_counts[pattern] += 1
	return kmers_counts


def reverse_complement(nucleotides):
	# Prints the reverse complement of a given string.
	reverse_complement = ""
	for x in nucleotides[::-1]:
		if x == "A":
			reverse_complement += "T"
		elif x == "T":
			reverse_complement += "A"
		elif x == "G":
			reverse_complement += "C"
		elif x == "C":
			reverse_complement += "G"
	print reverse_complement


def formatted_num(messy_solution):
	# Returns just the numbers of a list (no [] or ,). Ex:
	# >>> formatted_num([1, 3, 9])
	# >>> 1 3 9
	if len(messy_solution) == 1:
		print messy_solution[0]
	elif len(messy_solution) > 1:
		print ' '.join(str(x) for x in messy_solution)


def indices_of_pattern(pattern, genome):
	# Prints the indices where pattern occurs in genome, formatted.
	indices = []
	for x in range(len(genome) - len(pattern)):
		if pattern == genome[x:x+len(pattern)]:
			indices.append(x)
	print formatted_num(indices)

def clump_finding(genome, k, t, L):
# In genome, finding k-mers of length k that occur at least t times
# within a window of length L.
	frequent_kmers = []

	# Array of length 4^k, all values initialized to 0.
	# 4^k is the total possible kmers of length k.
	clump = [0] * (4^k)

	for x in range((4^k) - 1):
		if

# Not finished. See alt_soln_clumps.txt
def clump_finding(genome, k, L, t):
	# A list of lists. Each index represents a clump, each value
	# represents the kmers in that clump seen >= t times.
	# Length will be len(genome) - L?
	kmers_per_clump = []
	for x in range(len(genome) - L):
		clump = genome[x:x + L]
		# Makes a dictionary of {kmer:count}
		kmer_dictionary = kmer_frequency(clump, k)
		#ONLY if kmer occurs >= t times!
		keys_t_values = which_values_are_t(kmer_dictionary, t)
		kmers_per_clump.append(keys_t_values)
	return kmers_per_clump

def pop_recurrences(seq):
# not order preserving
	set = {}
	map(set.__setitem__, seq, [])
	return set.keys()



def hamming_distance(p, q):
	num_differences = 0
	for x in range(len(p)):
		if p[x] != q[x]:
			num_differences += 1
	return num_differences


def appx_kmer_matching_indices(kmer, genome, hamming):
# Returns indices of kmers that match input kmer up to hamming mismatches.
	approximate_kmer_index = []
	for x in range(len(genome) - len(kmer) + 1):
		if hamming_distance(kmer, genome[x:x + len(kmer)]) <= hamming:
			approximate_kmer_index.append(x)
	return approximate_kmer_index

def appx_kmer_matches_string(kmer, genome, hamming):
	approximate_kmers = []
	for x in range(len(genome) - len(kmer) + 1):
		if hamming_distance(kmer, genome[x:x + len(kmer)]) <= hamming:
			approximate_kmers.append(genome[x:x + len(kmer)])
	return approximate_kmers

def appx_kmer_matches_list(kmer, kmer_list, hamming):
	approximate_kmers = []
	for x in kmer_list:
		hamm = hamming_distance(kmer, x)
		if hamm != 0 and hamm <= hamming:
			approximate_kmers.append(x)
	return approximate_kmers

def some_bullshit(genome, kmer_length, mismatches):
	match_counts = {}
	kmer_count = kmer_frequency(genome, kmer_length)
	for base_kmer, frequency in kmer_count.iteritems():
		for kmer in kmer_count.keys():
			hamm = hamming_distance(base_kmer, kmer)
			if hamm!= 0 and hamm <= mismatches:
				kmer_count[base_kmer] += kmer_count[kmer]
	return kmer_count


keys_for_max_values()

def kmer_mismatches(genome, kmer_length, mismatches):
	match_frequency = {}
	kmer_count = kmer_frequency(genome, kmer_length)
	for base_kmer, frequency in kmer_count.iteritems():
		match_frequency[base_kmer] = frequency
		# Look for mismatches in kmer_count
		matches = appx_kmer_matches_list(base_kmer, kmer_count.keys(), mismatches)
		for x in matches:
			match_frequency[base_kmer] += kmer_count[x]
	return match_frequency


def immediate_neighbors(sequence):
	nucleotides = ['A', 'T', 'G', 'C']
	Neighborhood = [sequence]
	for x in range(len(sequence)):
		seq_mutable = list(sequence)
		for n in nucleotides:
			if sequence[x] != n:
				seq_mutable[x] = n
				Neighborhood.append("".join(seq_mutable))
	return Neighborhood

def suffix(pattern):
	return pattern[1:]


def Neighbors(sequence, mismatches):
# Generates all possible k-mers with at most x mismatches
	nucleotides = ['A', 'T', 'G', 'C']
	if mismatches == 0:
		return sequence
	if len(sequence) == 1:
		return nucleotides
	Neighborhood = []
	suffix_neighbors = Neighbors(suffix(sequence), mismatches)
	for x in suffix_neighbors:
		if hamming_distance(suffix(sequence), x) < mismatches:
			for n in nucleotides:
				Neighborhood.append(n + x)
		else:
			Neighborhood.append(sequence[0] + x)
	return Neighborhood

def total_mismatches(genome, kmer_length, mismatches):
	kmers_counts = {}
	for x in range(len(genome)-kmer_length):
		kmer = genome[x:x + kmer_length]
		kmers_counts[kmer]
		if kmer not in kmers_counts:
			kmer_mismatches = Neighbors(kmer, mismatches)
			kmers_counts[kmer]
			for neighbor in kmer_mismatches
			kmers_counts[kmer] = frequency

		else:
			kmers_counts[kmer] += 1
	return kmers_counts


	# Go through all k-mers in genome

	# Generate all possible mismatches with up to d differences
	# for each k-mer in genome

	# For each of those mismatches, count how many are in genome

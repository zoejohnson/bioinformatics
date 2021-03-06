import sys

input = sys.stdin.read()
sample = input.split()
text = sample[0]
pattern = sample[1]

def pattern_count(text, pattern):
	frequency = 0
	for x in range(len(text)):
		if text[x: x + len(pattern)] == pattern:
			frequency += 1
	return frequency

solution = pattern_count(text, pattern)
print(solution)




from collections import defaultdict
import sys
# find substrings at least kmer long that occur at least min_clumpsize
# times in a window of windowsize in genome
input = sys.stdin.read()
sample = input.split()

genome = sample[0]
kmer = int(sample[1])
windowsize = int(sample[2])
min_clumpsize = int(sample[3])

def get_substrings(g, k):
    """
Take the input genome window 'g', and produce a list of unique
substrings of length 'k' contained within it.
    """
    substrings = list()
    # Start from first character, split into 'k' size chunks
    # Move along one character and repeat. No sense carrying on beyond
    # a starting point of 'k' since that will be the first iteration again
    for i in range(k):
        line = g[i:]
        substrings += [line[i:i + k]
                       for i in range(0, len(line), k) if i + k <= len(line)]
    # Using collections.Counter increases the runtime by about 3 seconds,
    # during testing.
    results = defaultdict(int)
    for s in substrings:
        results[s] += 1
    return results


def find_clumps(genome, kmer, windowsize, clumpsize):
    window = genome[0:windowsize]
    patterns = get_substrings(window, kmer)
    relevant = {p: 1 for p in patterns if patterns[p] >= clumpsize}
    starting_string = genome[0:kmer]
    for i in range(windowsize, len(genome)):
        # Move the window along one character
        window = window[1:]
        window += genome[i]
        patterns[starting_string] -= 1
        starting_string = window[0:kmer]
        ending_string = window[-kmer:]
        patterns[ending_string] += 1
        if patterns[ending_string] >= clumpsize and ending_string not in relevant:
            relevant[ending_string] = 1
    return list(relevant)


if __name__ == "__main__":
	clumps = find_clumps(genome, kmer, windowsize, min_clumpsize)
	print(clumps)

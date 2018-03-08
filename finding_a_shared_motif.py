import time
start = time.time()
### reads in fasta format file, removes all newlines and splits at new sequence (>): does not work for fasta files with sequence IDs of varying length
with open("rosalind_lcsm.txt", "r") as d:
	dna = d.read().replace("\n", "").split(">")[1:]

shortest = min([seq for seq in dna if not len(seq)==0], key=len)	
  
### slices sequence into all possible fragments of a specified size, starts at 13 to skip the sequence ID Rosalind_xxxx
def slice_dna(seq, size):
	start = 13
	fragments = []
	while len(fragments) < len(seq)-size:
		fragments.append(seq[start:start+size])
		start +=1
	return fragments[:-12]

### creates fragments from the shortest sequence starting with the longest fragments and searches for a match in the other sequences, stops when it encounters the first fragment present in all sequences 
def longest_motif():
	for i in range(len(shortest),1,-1):
		fragments = slice_dna(shortest, i)
		for seed in fragments:
			for x, seq in enumerate(dna):
				if seed in seq and x<len(dna)-1:
					pass 
				elif seed in seq and x==len(dna)-1:
					return seed 
				else:
					break
			
seed = longest_motif()
with open("longestmotif.txt", "w") as l:
	l.write(seed)			

print 'It took', time.time()-start, 'seconds.'



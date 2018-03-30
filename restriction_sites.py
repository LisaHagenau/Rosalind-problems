# import fasta file, separate DNA string into variable

with open("rosalind_revp.txt") as fasta:
	fastalist = []	
	for line in fasta:
		if line.startswith(">"):
			fastalist.append("\n"+line.strip()+"\n")
		else:
			fastalist.append("" + line.strip())	
fastalist = ''.join(fastalist)[1:].split('\n')
seq = fastalist[1]

# function for reverse complementing DNA sequence 

rc ={"A":"T", "T":"A", "C":"G", "G":"C"}
def revcomp(sequence):
	result = "".join([rc[x] for x in sequence[::-1]])
	return result

# iterate over slices from length 2 to 6 at every position, call reverse complement function on slice and compare to next slice over 
# not the most time-saving solution, since you could theoretically skip the positions that are not reverse palindromes in a short slice for the longer slices 
# instead of going through all slice lengths at all positions, go through all positions and extend slice lengths only if reverse palindromes are found
# could also skip the result lists and print both results directly
pos = []
length = []

for slice_len in range(2,7):
	for i,c in enumerate(seq):
		slice = seq[i:i+slice_len] 
		if len(slice) == slice_len:
			next = seq[i+slice_len:i+2*slice_len]
			if revcomp(slice) == next:
				pos.append(i+1)
				length.append(slice_len*2)

res = zip(pos,length)				
for e in res:
	print(str(e[0]) + " " + str(e[1]))

		
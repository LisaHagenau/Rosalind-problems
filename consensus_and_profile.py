# consensus and profile
# import fasta file, disregard IDs, store sequences in list 

with open("rosalind_cons.txt") as fasta:
	fastalist = []	
	for line in fasta:
		if line.startswith(">"):
			fastalist.append("\n"+line.strip()+"\n")
		else:
			fastalist.append("" + line.strip())	
fastalist = ''.join(fastalist)[1:].split('\n')
seqlist = fastalist[1::2]

# transpose list of sequences > makes new nested list with first, second, third, ... nucleotides of all sequences
transposed = [[seq[i] for seq in seqlist] for i in range(len(seqlist[0]))]

# create profile by counting nucleotides at every position
# print(*list) prints every item in the list separated by white space > useful to print to console for short sequences
# the commented code below is based on appending to lists needs to convert these lists into strings for printing to file in desired format 
# shorter code directly appends to strings, there is probably a way to making the code shorter by iterating over the 4 nucleotides instead of repeating the command for each
 
# A = []
# C = []
# T = []
# G = []
		
# for x in transposed:
	# A.append(x.count("A"))
	# C.append(x.count("C"))
	# T.append(x.count("T"))
	# G.append(x.count("G"))

# A = " ".join(str(k) for k in A)
# C = " ".join(str(k) for k in C)
# G = " ".join(str(k) for k in G)
# T = " ".join(str(k) for k in T)

A = ""
C = ""
G = ""
T = ""

for x in transposed:
	A += str(x.count("A")) + " "
	C += str(x.count("C")) + " "
	G += str(x.count("G")) + " "
	T += str(x.count("T")) + " "


# write consensus sequence to file by returning the nucleotide that occurs most often for every position > using list comprehension with max(list, key=list.count)
with open("cons_result.txt", "w") as r:
	r.write("".join([max(e, key=e.count) for e in transposed]) + "\n")	
	r.write("A: "+ A + "\n")
	r.write("C: "+ C + "\n")
	r.write("G: "+ G + "\n")
	r.write("T: "+ T + "\n")

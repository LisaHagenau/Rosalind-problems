# import fasta file into dictionary, separate sequences into variables 
with open("rosalind_tran.txt") as fasta:
	fastalist = []	
	for line in fasta:
		if line.startswith(">"):
			fastalist.append("\n"+line.strip()+"\n")
		else:
			fastalist.append("" + line.strip())	
fastalist = ''.join(fastalist)[1:].split('\n')
seq_dict = dict(zip(fastalist[::2], fastalist[1::2]))
seq = list(seq_dict.values())

s1 = seq[0]
s2 = seq[1]

# define pairs of purines and pyrimidines, initiate transition and transversion counter
pur = ["A", "G"]
pyr = ["C", "T"]
ts = 0
tv = 0

# iterate over sequences and count transitions and transversions
for i,c in enumerate(s1):
	if not s1[i] == s2[i]:
		if s1[i] in pur and s2[i] in pur or s1[i] in pyr and s2[i] in pyr:
			ts += 1
		else:
			tv += 1
		
print(ts/tv)
	
			
			
	
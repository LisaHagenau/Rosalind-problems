# opens the file, concatenates the sequence strings and separates the string ID from the sequence
# zips the list of IDs and sequences into dictionary

with open("test.txt") as fasta:
	fastalist = []	
	for line in fasta:
		if line.startswith(">"):
			fastalist.append("\n"+line.strip()+"\n")
		else:
			fastalist.append("" + line.strip())	
fastalist = ''.join(fastalist)[1:].split('\n')
seq = dict(zip(fastalist[::2], fastalist[1::2]))


### above code as function: opens fasta file and stores IDs and sequences in dictionary, takes filename as argument

def parseFasta(file):
	with open(file) as fasta:
		fastalist = []	
		for line in fasta:
			if line.startswith(">"):
				fastalist.append("\n"+line.strip()+"\n")
			else:
				fastalist.append("" + line.strip())	
	fastalist = ''.join(fastalist)[1:].split('\n')
	seq = dict(zip(fastalist[::2], fastalist[1::2]))	
	return(seq)

	
print(parseFasta("test.txt"))
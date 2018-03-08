# read in string, define codons (dictionary, RNA triplets as keys, aa as value), split the string into triplets > list, iterate over list to get value, print list

with open("codons.txt", "r") as c:
	codons = [l.strip() for l in c.readlines()]	# for every line in the file, strip the newline character at the end and put all in a list

with open("aa.txt", "r") as a:
	aa = [l.strip() for l in a.readlines()]

# make a dictionary from the lists of codons and aminoacids 	
codon2aa = {c:a for c, a in zip(codons, aa)}

# read in sequence and split into list of codon triplets
with open("sequence.txt", "r") as s:
	seq = [l.strip() for l in s.readlines()]
	seq = "".join(seq)
	triplets = [seq[n:n+3] for n in range(0, len(seq), 3)]

# write translation to file, stop at the first Stop-codon	
with open("translation.txt", "w") as t:
	translation=[]
	for i in triplets:
		if codon2aa.get(i) == "Stop":
			break
		else:
			translation.append(codon2aa.get(i))
	t.write("".join(translation))
	
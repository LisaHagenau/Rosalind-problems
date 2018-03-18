# finding all possible ORFs in a DNA sequence

# replace all T with U for the translation code to work (DNA to RNA)
with open("rosalind_orf.txt") as f:
	seq = []
	for line in f:
		if not line.startswith(">"):
			seq.append(line.strip())
	seq = "".join(seq)
			
seq = seq.replace("T", "U")

# make reverse complement sequence using dictionary and list comprehension (more elegant than my for-loop solution) and store all 6 reading frames in a list		
rc ={"A":"U", "U":"A", "C":"G", "G":"C"}
rseq = "".join([rc[i] for i in seq[::-1]])

frames = [seq, seq[1:], seq[2:], rseq, rseq[1:], rseq[2:]]

# create the translation dictionary 
with open("codons.txt", "r") as c:
	codons = [l.strip() for l in c.readlines()]	# for every line in the file, strip the newline character at the end and put all in a list

with open("aa.txt", "r") as a:
	aa = [l.strip() for l in a.readlines()]
	
codon2aa = {c:a for c, a in zip(codons, aa)}

# split sequence into list of codon triplets and collect all protein sequences starting with M and ending with "Stop"
allORFs = []
for frame in frames:
	triplets = [frame[n:n+3] for n in range(0, len(frame), 3)]
	orf = []	
	for i in triplets:
		if codon2aa.get(i) == "M":
			orf.append(codon2aa.get(i))		
		elif codon2aa.get(i) == "Stop":
			if len(orf) is not 0:
				allORFs.append(orf)
			orf = []
		else:
			if len(orf) >= 1:
				orf.append(codon2aa.get(i))
			else:
				continue
	

# finds all possible ORFs in sequences containing more than 1 M
res = []
for i in allORFs:
	if i.count("M") == 1:
		res.append("".join(i))
	else:
		pos = [pos for pos, x in enumerate(i) if x == "M"]
		for p in pos:
			res.append("".join(i[p:]))          


# remove duplicates	and print to console
unique = []
[unique.append(x) for x in res if x not in unique]

for i in unique:
	print(i)
		

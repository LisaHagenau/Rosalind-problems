# opens the file and reads all lines into "lines"
with open("rosalind_splc.txt") as fasta:
	lines = fasta.readlines()
# concatenates the sequence strings and separates the string ID from the sequence
fastalist = []	
for line in lines:
	if line.startswith(">"):
		line = "\n"+line.strip()+"\n"
		fastalist.append(line)
	else:
		line = "" + line.strip()
		fastalist.append(line)	
fastalist = ''.join(fastalist)[1:].split('\n')
# maps the list content into a dictionary by alternately creating a key and a value from the list items
fastadict = dict(map(None, *[iter(fastalist)]*2))

# find pre-mRNA by extracting the longest sequence, put intron sequences into list
preseq = max(fastadict.values(), key=len)
introns = [seq for ID,seq in fastadict.items() if not seq == max(fastadict.values(), key=len)] 
print introns
# iterate over introns and return the mRNA string without intron sequence
# for the first iteration, the variable mrna is not yet defined, hence the name error exception 
for intron in introns:
	try:	
		mrna
		preseq = mrna
	except NameError:
		preseq = preseq
	start = preseq.find(intron)
	end = start+len(intron)
	mrna = preseq[:start]+preseq[end:]
	print len(preseq), len(intron), len(mrna)
print preseq, len(preseq)
print mrna, len(mrna)

allintrons = 0
for i in introns:
	allintrons += len(i)
print allintrons

# replace all T with U and split sequence into codon triplets
mrna = mrna.replace("T", "U")	
triplets = [mrna[n:n+3] for n in range(0, len(mrna), 3)]
 
# copied from translate RNA into protein program
with open("codons.txt", "r") as c:
	codons = [l.strip() for l in c.readlines()]	# for every line in the file, strip the newline character at the end and put all in a list

with open("aa.txt", "r") as a:
	aa = [l.strip() for l in a.readlines()]

# make a dictionary from the lists of codons and aminoacids 	
codon2aa = {c:a for c, a in zip(codons, aa)}

with open("translation.txt", "w") as t:
	translation=[]
	for i in triplets:
		if codon2aa.get(i) == "Stop":
			break
		else:
			translation.append(codon2aa.get(i))
	t.write("".join(translation))
	
print "".join(translation)
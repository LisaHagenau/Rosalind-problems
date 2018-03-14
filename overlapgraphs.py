# Overlap Graphs

# opens the file and reads all lines into "lines"
with open("rosalind_grph.txt") as fasta:
	lines = fasta.readlines()
# concatenates the sequence strings and separates the string ID from the sequence (not the most elegant solution...)
fastalist = []	
for line in lines:
	if line.startswith(">"):
		line = "\n"+line.strip()+"\n"
		fastalist.append(line)
	else:
		line = "" + line.strip()
		fastalist.append(line)	
fastalist = ''.join(fastalist)[1:].split('\n')

seq = dict(zip(fastalist[::2], fastalist[1::2]))

# replace sequence with list of first and last 3 nucleotides > not really necessary, could be included in the for-loop
seq.update((id, [s[0:3],s[-3:]]) for id, s in seq.items())

# convert dictionary to list of tuples and remove leading character (>) from sequence ID

seq =[(id.lstrip(">"),s) for id, s in seq.items()]

# create adjacency list
adj =[]

for s in seq:
	for t in seq:
		edge1 = s
		edge2 = t
		# compare tail of first sequence to head of second sequence and exclude same-sequence comparisons 
		if edge1[1][1] == edge2[1][0] and not edge1[0] == edge2[0]:
			adj.append((edge1[0], edge2[0]))

# write output to file
with open("grph_output.txt", "w") as out:
	for item in adj:
		out.writelines(str(item[0]) + " " + str(item[1])+ "\n")
		


with open("rosalind_subs.txt", "r") as s:
	seq, motif = s.read().split("\n")

x = 0
out = []
# searches the string until no more matches are found, which returns the value -1
while not -1 in out:
	out.append(seq.find(motif, x, len(seq)))	
	x = out[-1]+1
	
print " ".join([str(i+1) for i in out[:-1]])
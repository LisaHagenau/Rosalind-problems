#import fasta as dictionary > sequence name = key, sequence = value
#count G and C strings, count all strings, calculate percentage, store under same key as sequence
#return key of max percentage

# opens the file and reads all lines into "lines"
with open("rosalind_gc.txt") as fasta:
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
# function for calculating GC content
def gccontent(val):
	numall = len(val)
	numcg = val.count("C") + val.count("G")
	gc = numcg/float(numall)*100
	return gc
# new dictionary with GC content as value, but same key as in sequence dictionary	
gcdict = {key: gccontent(val) for key, val in fastadict.items()}
# prints out the ID and GC content for the highest calculated GC content in the dictionary
print max(gcdict, key=gcdict.get)
print max(gcdict.values())

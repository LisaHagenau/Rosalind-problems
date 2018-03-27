# import protein string, remove line breaks
with open("rosalind_mrna.txt") as f:
	protein = "".join(line.strip() for line in f)

# define codon multiplicators in dictionary

codon = {"M":1, "W":1, "N":2, "D":2, "C":2, "Q":2, "K":2, "E":2, "H":2, "L":2, "F":2, "Y":2, "I":3, "A":4, "G":4, "P":4, "T":4, "V":4, "R":6, "L":6, "S":6}

# iterate over protein string and multiply current value by dictionary value, initialize current with 3 to account for different stop codons 
current=3
for c in protein:
	current = current*codon[c]

# print the result modulo 1000000	
print(current%1000000)
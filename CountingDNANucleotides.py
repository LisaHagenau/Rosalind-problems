seq = "ATCGAAGGCCT"
from collections import Counter
result = Counter(seq)
resstr = ""
for key, value in sorted(result.items()):
    resstr = resstr + " " + str(value) 
print resstr


### more elegant version of my solution (verschachtelt) ###
from collections import Counter
for k,v in sorted(Counter(seq).items()): print v,

print ""
### easy, but not very elegant ###
a = seq.count("A")
c = seq.count("C")
g = seq.count("G")
t = seq.count("T")

print a, c, g, t

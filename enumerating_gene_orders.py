
from itertools import permutations

num = 5
perm = []
count = 0
for i in permutations(range(1,num+1)):
	count = count+1
	perm.append(i)
	
with open("result.txt", "w") as results:
	results.write(str(count)+"\n")
	for i in perm:
		i = str(i)
		i = i.replace(",", " ")
		i = i.replace("(", "")
		i = i.replace(")", "")
		results.writelines(i+"\n")
	
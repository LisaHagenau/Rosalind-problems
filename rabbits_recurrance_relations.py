# 
months = 5
litter = 3
start = 1
offspring = 0

for i in range(1,int(months)):
	reproductive = start+offspring  # 1		# 4		# 7		# 19
	offspring = start*litter		# 3		# 3		# 12	# 21
	start = reproductive			# 1 	# 4		# 7		# 19
print start
	
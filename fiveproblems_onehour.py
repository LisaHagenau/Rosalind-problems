### 3 functions for adding numbers in a list: the first two iterative, using a for and while loop, the third recursive

def sumfor(listofnumbers):
	count = 0
	for number in listofnumbers:
		finalcount = number + count
		count = finalcount
	return finalcount
	
listofint = [2,3,6,7]

print "The result for the sumfor function is: %d" % sumfor(listofint)

def sumwhile(listofnumbers):
	idx = 0
	count = 0
	while idx < len(listofnumbers):
		result = listofnumbers[idx] + count
		count = result
		idx += 1
	return result

print "The result for the sumwhile function is: %d" %sumwhile(listofint)

def sumrec(x):
	if not x:
		return "List is empty"
	elif len(x) == 1:
		return x[0]
	else:
		return x[0] + sumrec(x[1:])
		
print "The result for the sumrec function is: %d" %sumrec(listofint)


### zip two lists together: the zipit function simply appends the list elements bit by bit; the integrated zip function in python is easier, but creates tuples

one = ["a","b","c"]
two = [1,2,3]

def zipit(lst1, lst2):
	zipped = []
	n = 0
	for element in lst1:
		zipped.append(element)
		zipped.append(lst2[n])
		n += 1
	return zipped
	
print zipit(one, two)
print zip(one,two)

### function to compute the first 100 Fibonacci numbers, probably possible to do recursive as well

def fibo100():
	fibo = [0, 1]
	while len(fibo) < 100:
		fibo.append(fibo[-2] + fibo[-1])
	return fibo
	
print fibo100()

### function to arrange a list of numbers to represent the largest number possible

lst = [50, 9, 2, 4, 11]

strlst = [str(i) for i in lst]

sortlst = sorted(strlst, reverse=True)

print sortlst

print "".join([str(i) for i in sortlst])
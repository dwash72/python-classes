# import collections
# l = ["a","b","c","d","d"]
# print(collections.Counter(l))

#for loop

l1 = ["1","2","3","4","5","6","7","8","9","10","10"]
d = {}
for x in l1:
 # print(x)
	if x in d:
		d[x] and d[x] + 1
# print(x)
	else:
		d[x] = 1
print(d)
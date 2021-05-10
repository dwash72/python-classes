
# import re
# data = "hello"
# r = re.search("he", data)
# if r :
# 	print("yes")
# else:
# 	print("no")

# import re
# data = "hello"
# x = re.findall("hi", data)
# if x :
# 	print("yes")
# else:
# 	print("no")

# import re
# data = "hello"
# x = re.match("hi", data)
# if x :
# 	print("yes")
# else:
# 	print("no")

#method function
# def function(strrrr , dwash):
# 	if (strrrr.find(dwash) == -1):
# 		print("no")
# 	else:
# 		print("yes")
# strrrrr = "vins"
# dwash = ""
# function(strrrrr, dwash)

#excercise-2

# dic1 = {'j':3, 'f':2, 'd':1}
# sorted_dict = {}
# sorted_values = sorted(dic1, key= dic1.get)
# print(sorted_values)
# for x in sorted_values:
# 	sorted_dict[x] = dic1[x]
# print(sorted_dict)
	
dic1 = {'johann':52, 'k':22, 'h':1, 's':2}
sorted_values = sorted(dic1.values())
# print(sorted_values)
sorted_dict = {}
for x in sorted_values:
	for k in dic1.keys():
		if dic1[k] == x:
			sorted_dict[k] = dic1[k]
			break
print(sorted_dict)
			



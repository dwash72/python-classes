# #function to print even number
# def even(n):
# 	for x in range(n):
# 		if x % 2 == 0 :
# 			print(x)
# even(100)

# enumerate method

# def str_len(str):
#     for i , e in enumerate(s):
#     	print(i, e)
# s = ("dwash")
# # y = enumerate(s)
# str_len(enumerate)

# list(enumerate("fdwas"))

# for x in enumerate("dwash"):
# # 	print(x)
# w = ("dwash")
# def fu(w):
# 	for data in range(len(w)):
# 		print(data, w[data])
# fu(w)

# def multiple (num, multiple):
# 	for x in range(1, num + 1):
# 		print(x * multiple)
# multiple(10, 5)

def mul(num,m):
	value = []
	for x in range(1,num + 1):
		value.append(x * m)
	return value
print(mul(10, 5))
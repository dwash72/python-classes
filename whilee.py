# i = 0
# while i < 10 + 1:
# 	print(i)
# # 	i += 1
import random
# def choose_number(run=False):
# 	return "yes",False
counter = 1
while counter < 7:
	user_value = int(input("enter your number:"))
	v =  random.randrange(1, 11)
	if user_value == v:
		print("u get the correct number")
		break
	else:
			counter += 1
			# user_ask = input("do u want to continue yes or no:")
			# if user_ask == yes:
# 	# def function2():
# 	# 	data = choose_number()
# 	# 	return data
# 	# print(function2())
# 	else:
		# 	print("thank u for playing")
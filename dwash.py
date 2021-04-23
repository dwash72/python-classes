# d = "dwash"
# print(help(d.upper))
# l = [1,2,3]
# print(dir(l))
# print(help(l.append))
# append_list = [1,2,3,4]
# l = 1000
# append_list.append(l)
# print(append_list)
# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [11,12,13,14,15,16,17,18,19,20]
# l3 = []
# l3.append(l1)
# print(l3)
# l3.extend(l2)
# print(l3)
# l1.append(l2)
# print(l1)
l1 = list((1,2,3,4))
l2 = list((7,8,9,))
l3 = l1 + l2
l1.copy()
l2.copy()
l1.append(l2)
print(l3)

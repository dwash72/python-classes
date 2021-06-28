# python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# score_list = []
# for i in range(int(input())):
#     name=input()
#     score = float(input())
#     score_list.append([name, score])
# second_high = sorted(set([score for name, score in score_list]))
# print('\n'.join(sorted([name for name, score in score_list if score_list == second_high])))


from itertools import combinations_with_replacement
# print(help(combinations_with_replacement))
s, k = input(). split()
for c in combinations_with_replacement(sorted(s), int(k)):
	print("".join(c))

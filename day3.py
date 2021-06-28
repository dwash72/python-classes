# import itertools
# data_list = {'country':'usa', 'state':'colorona', 'name':'ariyana'},
# {'country':'usa', 'state':'missouri', 'name':'michelle'},{'country':'india', 'state':'co', 'name':'ar'}
# x = itertools.groupby(data_list)
# for k,g in x:
# 	print(k)
# 	print(list(g))

from itertools import groupby
data_list = [
{
"country":"usa",
"state":"olorona", 
"name":"ariyana"
},
{
"country":"usa", 
"state":"missouri", 
"name":"michelle"
}, 
{
'country':"india", 
'state':"co", 
'name':"ariyana"
},
{
'country':"india",
 'state':"chennai", 
 'name':"deag"
 },
]
def function(k):
	return k['country']
data_list = sorted(data_list,key=  function)
for key,value in groupby(data_list,function):
	print(key)
	# print(list(value))
	# print(list(value))
	for data in value:
		print(data)
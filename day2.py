def function(d1 , d2):
	intersect = (d1.keys() & d2.keys())
	di = {key:(d1.get(key),d2.get(key)) for key in intersect}
	print(di)
function({'d':1, 'c':2, 'b':5},{'c':2, 'b':100})

# def intersect(d1, d2):
# 	return (d1.items() & d2.items())
# print(intersect({'a':2,'c':10,'f':20},{'b':42, 'a':2,'c':10}))


from collections import Counter,OrderedDict
d = OrderedDict(zip(['a','b','c','d'],[1,2,3,4]))
print(d)
d.popitem(last=False)
print(d)
d['a']=1
print(d)
d.move_to_end('c')
print(d)
print(d['c'])
print('d' in d,'e' in d)
d.pop('d')
print(d)
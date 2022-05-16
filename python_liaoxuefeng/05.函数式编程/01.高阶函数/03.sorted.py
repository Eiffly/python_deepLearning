# 默认是数值从大到小
print( sorted([36, 5, -12, 9, -21]))  
print( sorted([36, 5, -12, 9, -21], key=abs)) 
#默认是ASCII码从大到小
print( sorted(['bob', 'about', 'Zoo', 'Credit']))
print( sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print( sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))



# 例题
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
def by_score(t):
    return -t[1]

#测试代码
L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)


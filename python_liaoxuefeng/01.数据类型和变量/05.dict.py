d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Adam'] = 67

# 判断key是否存在的方法一
print('Thomas' in d)             #False
# 判断key是否存在的方法二
print( d.get('Thomas'))          #None
#当然也可以自己去指定相应的value
print( d.get('Thomas',-1))       #-1





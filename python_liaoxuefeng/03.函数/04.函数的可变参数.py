def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([]))          #0
print(calc([1, 2, 3]))   #14
# print(calc(1, 2, 3))  #这种写法在这个情境下会报错，需要一个参数但是传入了三个参数


def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc1())         #0
print(calc1(1, 2, 3))  #14
nums = [1, 2, 3]
print(calc1(nums[0], nums[1], nums[2]))  #14
print(calc1(*nums))  #14

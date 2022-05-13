def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, 'Beijing', 'Engineer')           #会报错
person('Jack', 24, city='Beijing', job='Engineer')  #Jack 24 Beijing Engineer


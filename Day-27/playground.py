def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

result = add(1,2,3,4,5,6)
print(result)

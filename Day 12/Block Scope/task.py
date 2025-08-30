import math


def is_prime(num):
    count=0

    for i in range(int(math.sqrt(num))):
        i=i+1
        if num%i==0:
            count+=1
    if count>1:
        return False
    return True

print(is_prime(75))
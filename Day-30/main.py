# Types of errors
# FileNotFoundError
# KeyError
# IndexError
# TypeError

'''
try:
    something that might cause an exception

except:
    Do this if there was an exception
else:
    Do this if there was no exception
finally:
    Do this no matter what happens
'''

# try:
#     file =  open("a_file.txt")
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# else:
#     content= file.read()
#     print(content)
#
# finally:
#     # file.close()
#     # print("File was closed")
#     raise TypeError("This is an error that i made up")
#

height = float(input("Height:"))
weight = float(input("weight"))

if height > 3:
    raise ValueError("The human height could not be more than 3 meters")
bmi = weight/height**2
print(bmi)
#break, continue

# for i in range(0,10):
#     n = int(input("Enter the number = "))
#     if n == 1:
#         break
#     print(n)
# else:
#     print("loop completed for break")

# for i in range (10):
#     n = int(input("Enter a number = "))
#     if n == 1: 
#         continue
#     print(n)
# else:
#     print ("Loop completed for continue")

# username = "r@gmail.com"
# password = "123@abcd"

# while True:
#     user_name = input("Enter the username = ")
#     pass_word = input ("Enter the password = ")
#     if (username == user_name.casefold() and password  == pass_word.casefold()):
#         break

#print ("You have entered")  

#Never use if..else.., till it can be solved by only simple coding
#Example

# user = input("Enter username : ")
# pwd = input("Enter password : ")

# while user != user_name or pwd != pass_word:
#     user = input("Enter username : ")
#     pwd = input("Enter password : ")
# else:
#     print ("Logged in")



#if read-only-scenario then we use tuple rather than list
# because tuple is memory efficient, take low memory space
#from sys import getsizeof to get the size

#key should be unique in dictionary
#in set, it is collection of random unique object
#dictionary is said to be mappable

#dictionary - mappable and hashable object terminology
# key needs to be hashable and unique

#List cannot be hashed, hash is fixed values fixed mapping

#hash(list) - returns the error
#hash(tuple or string) - gives hashing value

#jason and dictionary are the same things
#learn the use on list and dictionary


a = [(1,2,3), (5,6,7), (8,9,0)]
v = 0

for i in a:
    d = 0
    for j in i:
        d = d*10 + j
    v = v + d

print (v)




































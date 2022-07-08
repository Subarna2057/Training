# # # # # *args, **kwargs

# # # # def product(*args):
# # # #     a = 1
# # # #     for i in args:
# # # #         a = a * i
# # # #     print(a)

# # # # product (10,12,13)

# # # #  non-return function bata return expect gardai chha vaney None garcha
# # # # #*****************
# # # # def product_one(num1, num2):
# # # #     print (num1 * num2)

# # # # ans = product_one(10,12)
# # # # print(f"Answer: {ans}")

# # # # def product_two(num1, num2):
# # # #     return (num1*num2)

# # # # ans = product_two(10,12)
# # # # print(f"Answer: {ans}")
# # # # #*****************

# # # def example(*args):
# # #     print(args)

# # # example(1,"subarna",[1,2,3,4],["dewansh"],5)

# # # def example_two(**kwargs):
# # #     print(kwargs)

# # # example_two(name=[1,2,3], address="Ktm", phone="98098")

# # def example_three(*args, **kwargs):
# #     print(args)
# #     print(kwargs)

# # example_three(1,2,3,4,5,"Subarna", name="Dewansh", phone = "3423")

# # #sequence matters a lot, i.e. positioning of the args and kwargs

# #reversing

# def example_four(name, address, contact):
#     print(f"Name : {name}")
#     print(f"Address : {address}")
#     print(f"Contact : {contact}")

# student = {"name" : "Subarna", "contact": "93450", "address" : "Patan"}

# example_four(**student)


# # hete as passing kwargs i.e. **, then it unpacks the dictionary and passes 

#Function

# def add(a, b):
#     print(a+b)
 
# a = add    #Call by reference
# a(10,12)

#Little Complex

# def welcome(name):
#     print(f"Welcome {name}!")

# def greet_ram(func):
#     func("Ram")

# greet_ram(welcome)  #Higher order function

# #Higher order function means that to pass function as the function argument

# #Reason - because everything object in Python, above welcome is the object of function


# def square_root_of_sum(func, num1, num2):
#     return func(num1, num2)**0.5

# def add(num1, num2):
#     return (num1 + num2)

# print(square_root_of_sum(add,10,15))

#max go upto 3 case nested layer indentation
#Scoping

# def outer_func():
#     def first_child():
#         print("I am first child")
#     def second_child():
#         print("I am second child")
#     first_child()
#     second_child()
#     first_child()   # Output here comes as ranking calling of the local functions

# outer_func()

# def calculator(operator):
#     def add(a,b):
#         return a+b
#     def product(a,b):
#         return a*b
#     def subtract(a,b):
#         return a - b
#     if operator == "+":
#         return add
#     elif operator == "*":
#         return product
#     elif operator == "-":
#         return subtract
    
# totalsum = calculator("+")
# multiplication = calculator("*")
# subtraction = calculator("-")
# print(totalsum(10,15))
# print(multiplication(10,15))
# print(subtraction(10,15))



def calculator(operator, a, b):
    def add():
        return a+b
    def product():
        return a*b
    def subtract():
        return a - b
    if operator == "+":
        return add
    elif operator == "*":
        return product
    elif operator == "-":
        return subtract
    
totalsum = calculator("+", 10, 12)
multiplication = calculator("*", 10 ,12)
subtraction = calculator("-", 10 ,12)
print(totalsum())
print(multiplication())
print(subtraction())





































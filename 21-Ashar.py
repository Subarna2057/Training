
#lambda function

# important syntax: lambda p1, p2:p1+p2

# total = lambda a, b:a+b
# print(total(10,12))

# map, filter

# map(func, iterable)

#a = [1,2,3,4,5]
# output = []

# for i in a:
#     output.append(i+1)
# print(output)

# why to use map() because to increase the performance 
# code in map is in cpython and optimal code and return in iterable manner, fast operation for large data set

# def increment_by_one(n):
#     return n+1
# output = map(increment_by_one, a)
# print(list(output))

# #using lambda instead of creating function differently
# output = map(lambda n:n+1, a)
# print(list(output))

# name = "Subarna"
# output = map(lambda n: n+"1", name)
# print(list(output))

#iterator = sabai value ekai choti didaina, cannot be accessed once passed 
#iterable = sabai value ekai choti dincha, can be accessed repeatedly as being stored in memory


# names = ["ram", "shyam", "sita", "hari"]

# output = map(lambda n : n.capitalize(), names)
# print(list(output))

# print(list(map(str.capitalize, names)))

# print(list(map(str.title, names)))    This is object oriented programming

#filter(func, iterable)

# a = [1,2,3,4,5]

# output = filter(lambda n: n%2 != 0, a)

# print(list(output))
# #output : [1,3,5]

# out = map(lambda n: n%2 != 0, a )
# print (list(out))
# # Output : [True, False, True, False, True]

# emails = [
#     "1@gmail.com",
#     "2@yahoo.com",
#     "3@gmail.com",
#     "4@outlook.com",
#     "5@gmail.com",
#     "@gmail.com67"
# 

# print(list(filter(lambda n: n.endswith("@gmail.com"), emails)))

#isinstance(object, class)

# a = [1,2,3,"python","apple",5,6,7]

# print(list(filter(lambda n: isinstance(n, int),a)))

# print(sum(filter(lambda n: isinstance(n, int),a)))   // New function encountered that is sum()

# a = [1,2,3,4,5]
# print(sum(a))

# Read about Decorator>>>>>>>>>>>Need to understand below 3 points
#1. Function ko parameter bata function pass garney
#2. Inner function ko scope local huncha bahira global maa direct call garna mildaina
#3. Yedi baahira ko scope maa call garnu paryo vaney function ko reference return garnu parcha

#Object Oriented Programming in Python

    # 1. Class and object
    # 2. Inheritance --> 'IS A' relationshi[]
    # 3. Polymorphism
    #    - method overloading - not used in Python, because particular datatype is not defined while passing the parameter
    #     - method overriding - used because to define the new characteristics + parents characteristics in the child or difference characteristics than parentin the child
    # 4. Abstraction --> used when something doesnot exit. E.g: That class that cannot have the object, like Shape , but its child Circle, triangle has the childs

# class Car: # attribute and behaviour
#     pass

# c= Car()
# print(c)

# #in dynamically typed programming language

# c. color = "black"
# print(c.color)

# # rarely done but can be done, after creating the object new attribute can be defined within the object and assigned

#initialiser  function and constructor are different things
# Initialiser function 
# def  __init__(self):
#     pass

# class Car: #property and behaviour
#     # initialiser function
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

# c = Car("2022", "Black")
# print(c.color)
# print(c.model)














































































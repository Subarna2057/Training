
# def decorate_function(func):
#     def wrapper():
#         print("Hello students!")
#         func()
#         print("Bye bye students! ")
#     return wrapper
        
# def welcome():
#     print("Welcome students!")

# a = decorate_function(welcome)
# a()
#print(welcome)

# def decorate_function(func):
#     def wrapper():
#         print("Hello students!")
#         func()
#         print("Bye bye students! ")
#     return wrapper

# @decorate_function
# def welcome():
#     print("Welcome students!")

# welcome()     # wrapper() is called    this line equivalent to line 12 and 13

# print(welcome)    #observe the difference with line 14


# def decor(func):
#     def dec():
#         print("My name is Subarna")
#         func()
#         print("I am very handsome")
#     return dec

# @decor
# def d():
#     print("Ghhyamjo is a man")

# d()

# def smart_division(func):
#     def wrapper(a,b):                     # def wrapper(*a, **b) -> then it accepts everything
#         if  b == 0:
#             return "Could not divide"
#         else:
#             return func(a,b)
#     return wrapper

# @smart_division
# def division(a,b):
#     return a/b

# print(division(10,2))
# print(division(10,0))

#Task

# Question
# heros = ['spider man', 'thor', 'hulk','iron man','captain america']
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
# 4.Now you don't like thor and hulk because they get angry easily:)
#          So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool),
#          Do that with one line of code
# 5.Sort the heros list in alphabetical order






# heros = ['spider man', 'thor', 'hulk','iron man','captain america']

# print(f"The length of the list = {len(heros)}")

# heros.append('black panther')
# print(heros)
# heros.remove('black panther')
# print(heros)

# heros.insert(heros.index('hulk')+1, 'black panther')
# print(heros)

# heros[1:3] = ["doctor strange"]
# print(heros)

# heros.sort()
# print(heros)


#Book -> class
#page -> attribute
#read -> attribute

# Noun -> object
# Adjective -> attribute, property
# Verb(action) -> behaviour, method

class Book:
    def __init__(self, page):
        self.page = page

    def read(self):
        print(f"Page number {self.page} is being read")

c = Book(300)
print(c.page)
c.read()

d = Book(20)
print(d.page)
d.read()

Book.read(c)

# Two way to call the method 
# 1. Call through object i.e. line number 113
# 2. Call through class explicitly passing the object i.e. line number 119





















































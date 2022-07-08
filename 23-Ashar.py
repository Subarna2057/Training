
# # class Page{
# #     int page_number;
# #     char content[20];
# #     public:
# #         Page(page_number, content){
            
# #         }

# # }


# class Page:
#     def __init__(self, page_number, content):
#         self.page_number = page_number
#         self.content = content

#     def read(self):   # instance method -> that is object is passed 
#         print(f"Reading {self.content} of page number {self.page_number}")

#     @staticmethod   # Because anything can be returned that is object or variable, object na chahiney case maa use garney , siddhai class name bata call garna milcha without through object
#     def print_to_printer(content):    #static method -> call garna lai object banaunu pardaina, class nai bata call garey pugcha
#         print("Printing.....")
#         print(content)
    
#     def __repr__(self):      # dedicated to the list printing overide
#         return self.content
#     # def read_data(self):
#     #     print({self.page_number}, {self.content})

# # p = Page(1, "This is new paragraph.")
# # p.read()
# # Page.print_to_printer("This is a sentence.")
# # p.print_to_printer("My name is Khan")
# # p.print_to_printer(p)


# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
    
#     def number_of_pages(self):
#         return len(self.pages)
    
#     def add_page(self, page):
#         self.pages.append(page)
    

#     def __str__(self):  # overiding such that to return the desired things as output in behalf of object
#         return self.title

#     # method: (self, page_number) : "content"
#     # b.get_content(1)
    
#     def get_content(self, page_num):
#         for i in self.pages:
#             if (i.page_number == page_num):
#                 return i.content
#         return "Page not found"
    

# pages = []
# for i in range(1,6):
#     p = Page(i, f"This is paragraph {i}.")
#     pages.append(p)

# b = Book("Maths", pages)
# # print(f"Number of pages: {b.number_of_pages()}")

# p = Page(6, "This is new page.")
# b.add_page(p)
# # print(f"Number of pages: {b.number_of_pages()}")

# # a = Book.data()
# # for i in a:
# #     i.read_data()
# # print(b)
# # print(p)
# # print(b.pages)


# # Object is the super class in the Python 
# # so the __repr__, __str__ can be override, vako kura lai over irde gareko ho
# # class Page(object), implicitly vako huncha
# # __str__ -> string representation

# print(b.get_content(7))


# print(b.__dict__)    # Important and in-built function that prepares the dictionary of the present data

# # Handle Runtime Error using try and except

# # #Syntax
# # try:
# #     pass
# # except Exception:  (ValueError, TypeError, FileNotFoundError):  #Specific Error catch garnu parcha
# #     pass
# # except Exception:   # yesley justo error ni catch  garcha, kun error catch gareko ho developer lai thaha hudaina in such case
# #     pass
# # else:
# #     pass
# # finally:
# #     pass

# Using Exception is not the Good practise to use in coding like if... else... statement
# if try block statement successful then only else block executed

try:
    n1 = int(input("Enter number = "))
    n2 = int(input("Enter number = "))
except ValueError:
    print("Cannot convert to interger")
else:
    print(n1 + n2)

# Should know inheritance, association - aggregation and composition for class diagram
# LEarn drawing Class Diagram























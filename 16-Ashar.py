# #Dictionary

# properties = {
#     "data" : [
#         {
#             "name" : "Ram",
#             "rank" : 1,
#             "contact" : ["987633", "97623"]
#         },
#         {
#             "name" : "Sita",
#             "rank" : 2,
#             "contact" : ["9372523", "986322","1"]
#         }
#     ]
# }

# profile = properties.get("data")

# for p in profile:
#     print ("*********************")
#     print("Name = {}".format(p.get("name")))
#     print("Rank = {}".format(p.get("rank")))
#     t = p.get("contact")
#     i = 1
#     for v in t:
#         print("Contact{} = {}".format(i, v))
#         i += 1



def profile(name, address, contact):
    print(f"Name: {name}")
    print(f'Contact: {contact}')
    print(f"Address: {address}")

profile("Subarna", 9869019790, "Patan")
print("***************")
profile(name = "Subarna", contact = 9869019790, address = "Patan")
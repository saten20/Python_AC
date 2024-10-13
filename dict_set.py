#---------------Dictionary-----------

# dictionary in python is same as the object in Javascript.dictionary are mutable. it is unordered collection of key:value pair.
# it store the value in {key: value} form. key is always unique.
# we can use the tuple , list inside the dictionary as value. we can not use list as the key since it is mutable.
# it is defind as dict = {"name" :"satendra", "age": 12}
# if key is string then it is defind under the "key"
# dict["name"] through which we can access the value of the dictionary
# Nesting of the dictionary can also be done.




# dict = {
#     "username": "saten123",
#     "id":123,
#     "email":"saten@gamil.com",
#     "price": [100, 233, 123],
#     "product" :("cloth", "iron", "phone"),
#     12:"key as integer"
# }
# dict["username"] = "satendra_04"
# print(dict["price"])
# print(dict["product"])
# print(dict)
# print(dict[12])

# dict2 = {}
# dict2 = dict
# print(dict2)
# print(len(dict2))


# dict = {
#     "username":"saten123",
#     "product":{
#         "iron":2299,
#         "washingMachine":9999,
#         "tv":15000
#     },
# }

# dict1 = dict["product"]              # one way to access the inner dictionary
# print(type(dict1))
# print(dict1["tv"])

# print(dict["product"]["iron"])      # second way to access the inner dictionary





# ------- method ----------

# len(dict) --> it will return the length of the dictionary i.e count of total key value pairs.
# dict.keys()  --> it will return all the keys. type is dict_keys
# dict.values() --> it will returns all the values of the dict. type id dict_value
# dict.items() --> it will return all the {key: value} pair in the tuple form
# dict.get("key") --> it will return the corresponding value of the key. if key is not present then it will return none
# dict.update({"key":"value"}) --> it is used to update or insert new key:value in the dictionary

# userDetails = {
#     "username":"saten@123",
#     "id":129,
#     "eamil":"saten9834@gmail.com",
#     "product":{
#         "ipad":2,
#         "phone":1,
#         "tv":1
#     }
# }

# print(list(userDetails.keys()))
# print(list(userDetails.values()))
# print(list(userDetails.items()))
# print(userDetails.get("username"))
# userDetails.update({"location":"Mumbai"})

# print(userDetails)





#----------------------- set in python ----------------
# set in unordered collection of unique element.
# it is defind as setval = {1, 2 , "saten"}. it only store the value not key value .
# element of the set are immutable i.e you can not change the element of the set.
# set is mutable i.e we can insert , remove the element from the set.
# To defind the empty set --> setval = set() or setval = {1, }. we can not use setval = {} since it is conflict with dictionary

# setval = {1, 2, 3 ,3 ,3, "jatin", "tushar", "jatin"}
# print(setval)


#-------------------Method of set------------------

# len(setval) --> return the lenght of the set
# setval.add(ele)  --> add the element in the set
# setval.remove(ele) --> remove the element from the set
# setval.clear() --> it will remove all the element from the set
# setval.pop() --> it will pop the random element from the set
# setval1.union(setval2) --> return the new set having union of set1 and set2
# setval1.intersection(setval2)  --> return the new set having intersection of set1 and set2

# setval1 = {"saten", 2,"viren", 3, 4, 5}
# print(len(setval1))
# print(setval1)
# setval1.add(100)
# print(setval1)
# setval1.remove(100)
# print(setval1)
# print(setval1.pop())
# setval1.clear()
# print(setval1)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# res = set1.union(set2)
# print(res)
# res = set1.intersection(set2)
# print(res)







#-----------------Practice--------------

setval = set()
setval.add(int(9))
setval.add(float(9))
print(setval)
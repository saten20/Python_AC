#---------------list-------------------

# list in python is same as array . but it also store different values.
# list are mutable i.e we can change the values and list.
# writing the name of the list is as equivalent to the printing the complete list.

# list = [1, 43, 5, 245, 55, "Saten", "viren", 42]
# print(list)



#------------Method of the list-----------

# list[idx1: idx2] --> slice the element from the idx1 to idx2(excluded).it will not change the orignal list. 
# if idx is not defind then by default it is 0 , if idx2 not defind then by default len(list)
# [2, 5, 3, 6, 7, 79, 10] --> indxing (-7, -6, -5, -4, -3, -2, -1) in case of slice only i.e if we use negitive value in [idx1: idx2]

# len(list) --> return the lenght of the list
# list.append(10) --> insert the value from the back
# list.sort() --> sort the array in assending order. it will change the original list
# list.sort(reverse = True) --> sort in decending order
# list.reverse() --> it will reverse the original list
# list.insert(idx, el) --> insert the element at the specified position
# list.pop(idx) --> pop element from the particular index
# list.remove(ele) --> remove the first occurene of the specified element from the left
# list.copy() --> it return the new copy of the list

# marks = [34, 5, 24, 76 ,5, 78]
# print(marks[2:5])
# print(marks[-4: -2])
# print(marks[:5])
# print(marks[3:])


# marks = [5,4,24,76,43, 4, 5, 3,12,75,46]
# print(len(marks))
# marks.append(1000)
# marks.remove(4)
# print(marks)
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)
# marks.insert(2, 5000)
# print(marks)
# marks.pop(2)
# print(marks)

# list = [1, 2, 3, 4, 5]
# copyList = list.copy()
# print(copyList)







# --------- tuple in python ---------

# Tuples are immutable i.e we can not change the original tuple. while the list are mutable
# instead of [] to define tuple () are used.
# we can store list inside tuple and tuple inside list.

# if we are putting only one element inside the tuple then use comma after the element otherwise python interpretor will take it as normal
# variable rather then tuple --> tuple = (1,)


# tuple = (1, 24, 5, 32)
# print(type(tuple))
# print(tuple)
# tuple2 = (1, )
# print(type(tuple2))








#--------- method in tuple  -------

# tuple.index(ele) --> return the index of the first occurence of the specified element
# tuple[idx1: idx2]  --> slice the value from the tuple
# we can type cast the list to tuple and vice versa.


# tuple = (1, 42, 4, 2, 4, 2, 4, 5)
# print(tuple.index(4))
# print(tuple[2:5])




# ----------------- Practice -----------

# m1 = input("Enter the first movie name: ")
# m2 = input("Enter the second movie name: ")
# m3 = input("Enter the third movie name: ")
# list = [m1 , m2, m3]
# print(list)


# check palindrome 

# list1 = [2, 4, 5, 4, 2]
# copyList = list1.copy()
# copyList.reverse()

# if(list1 == copyList):
#     print("Palindromic list")
# else:
#     print("Not palindromic list")

# tuple = ("a","b","c","a","a","d","c")
# print(tuple.count("a"))
# list = list(tuple)
# print(type(list))
# list.sort()
# print(list)

# list = [1, 2, 4, (13, 43, 23)]
# list.append(122)
# print(list)



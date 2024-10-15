#-----function in python------

# In python there is no need to defind the return type , input parameter type.
# Default argument in python is same as in c++.
# That is if user forgot to pass the value during the function call then our function will take the default value defind in it.
# But if user pass the value then it will take the user value only not the default value.




# def check(a, b):
#     if(a > b):
#         print("greter number is", a)
#     else:
#         print("greter number is", b)

# check(100, 200)


# def addition(a = 10, b = 20):       # default argument
#     print(a + b)
# addition(100, 300)





#----------------Merge sort-------------

# def merge(low, mid, high, list):
#     left = low
#     right = mid + 1
#     temp = []
#     k = 0

#     while(left <= mid and right <= high):
#         if(list[left] > list[right]):
#             temp.append( list[right] )
#             k += 1
#             right += 1
#         else:
#             temp.append( list[left] )
#             left += 1
#             k += 1
    
#     while(left <= mid):
#         temp.append( list[left] )
#         left += 1
#         k += 1
#     while(right <= high):
#         temp.append( list[right])
#         right += 1
#         k += 1
    
#     for i in  range(low, high + 1, 1):
#         list[i] = temp[i - low]



# def divide(low, high, list):
#     if(low >= high):
#         return
#     mid = int((low + high) / 2)
#     divide(low, mid, list)
#     divide(mid + 1, high , list)
#     merge(low, mid, high, list)

# def callmerge():
#     list = [1, 5, 8, 2, 10, 15, 9]
#     divide(0, 6, list)
#     for val in list:
#         print(val)

# callmerge()



# def fact(n):
#     if(n == 0 or n == 1):
#         return n
#     return n * fact(n - 1)

# print(fact(6))

def natural(n):
    if(n <= 0):
        return n
    sum = n + natural(n - 1)
    print(sum)
    return sum

natural(5)

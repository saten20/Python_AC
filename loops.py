#-------------------- while loop ----------

# when we want to work with the index then we will use the while loop
# break and continue key word work in the same way as c c++

# list = [12, 45, 3, 5, 5, 5,  32, 564, 'satendra','viren',124]

# i = 0
# while i < len(list):
#     if(list[i] == 'satendra'):
#         break
#     print(list[i])
#     i += 1



#-------------------for loop-----------

# for loop is same as that of for in loop in js
# syntex --> for val in arr
# else can be used with the for loop which is only run if the complete loop is run successfully.if loop is terminated in-between then the else 
# will not run.
# if we use break statement in the loop then else statement will not run.


# list = [10, 20, 30, 40, 50 , 60, 70, 80]

# for val in list:
#     print(val)

# for val in list:
#     if(val == 70):
#         break
#     print(val)
# else:
#     print("Loop run completly")



#---------------- range() function ----------

# range() function is used with the for loop
# it take three parameter ---> range(start, stop, step).
# by default start is 0, step i.e increment by 1  and stop is excluded.



# for val in range(1, 20, 2):
#     print(val)

# list = [10, 20, 30, 40, 50, 60, "saten", "viren", 100]
# for i in range(0, len(list), 1):
#     print(list[i])



#------------pass statement------
# pass statment used when right now we don't know what to right in the body of loop but we want to execute the other line of code
# so if we don't write the pass inside the loop then interpretor will confuse in indentation and give us error
# pass can be used inside the condition statement also

# for val in range(10):
#     pass
# print("loop is ignored")


# ---------- practice

# i = 0
# n = 5
# sum = 0
# while(i <= n):
#     sum += i
#     i += 1
# print(sum)

f = 1
for val in range(1, 11, 1):
    f = f * val
    print("fact of ", val, "is", f)
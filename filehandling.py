#------------------File Handling -------------------
# All the program run on RAM and ram is volatile storage.so if we want to store our data permanently then for that we have to store that data 
# in secondary storage. This is done by using the file handling.

# First there is copy of file comes in the ram same as c. All the read/ write is perform on that buffer.
# we have to close the file after performing the read or write. why ? when we close the file all the opeartion that we have done on buffer
# in the RAM will updated to actual file.
# file pointer is shifted after performing any operation. hence it become important to close the file to shift the file pointer to the beggning.



# Methods
# f = open("filename", "mode") --> this will open the file and return the file object.
# f.read() --> it is used to read the data from the file. it returns the stream.
# f.readline() --> This function will read the data line by line.
# f.wrtie()  --> This is used to write in the file
# f.close() --> close the file
# f.seek(0) --> This function will shift the file pointer to the beggning.
# modes are --> "a"(append), "r"(read only default), "w"(overide the data), "w+/r+/a+"(read and write)
# "r+" --> it will overide the data from the begning.exsisting data not truncate.read/write
# "w+" --> it will truncate the old data and then perform the write operation.read/write
# "a+" --> it append the data.read/write

# os.remove("filename") --> it will delete the mention file in the parameter
# with open() as f --> this will open the file . it will automatically close the file.


# f = open("first.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# f = open("first.txt", "w")
# f.write("Stays prepair you weapan and your body for the war")
# f.close()
# f1 = open("first.txt" , "r")
# data = f1.read()
# print(data)
# f1.close()


# f = open("first.txt","r+")
# f.write("Aapne aap pe viswas rakha")
# data = f.read()
# print(data)
# f.close()

# f = open("first.txt","w+")
# f.write("With the positive appraoch we can solve any problem in our life")
# data = f.read()
# print(data)
# f.close()


# f =open("first.txt","a+")
# f.write("keep growth mindset")
# f.seek(0)
# data = f.read()
# print(data)
# f.close()


import os
# f = open("second.txt","w+")
# f.write("self confidence rakha bhai satya")
# f.seek(0)
# data = f.read()
# print(data)

# os.remove("second.txt")


# with open("first.txt", "r") as f:
#     data = f.read()
#     print(data)
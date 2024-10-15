#-----------------Abstraction-------------

# Abstraction is the concept of hiding the unwanted details and showing only the related details to the user.
# In the below example user don't know how we are calculating the  Average of the marks. user just call marks() function. 


# class Student:

#     def __init__(self, name, list):
#         self.name = name
#         self.list = list
    
#     @staticmethod

#     def show():
#         print("welcome to NITK")

#     def showDetails(self):
#         return (self.list[0] + self.list[1] + self.list[2]) / 3
    
# s = Student("satendra",[45,79,90])
# print(s.showDetails())
# Student.show()








#---------------- Encapsulation------------

# Wrapping all the information related to single entity inside the one class is called as  encapsultion.
# In the above example student is the entity and we have wrap all the method and variable related to the student in the student class.

# class Account:

#     def __init__(self, balance):
#         self.balance = balance
    
#     @staticmethod

#     def notes():
#         print("Central Bank of India", end =" ")

#     def credit(self, amount):
#         self.notes()
#         print("Account Credited with Rs.", self.balance)
#         self.balance += amount
#         print("Total balance Rs.", self.balance)

#     def debited(self, amount):
#         self.notes()
#         print("Account Debited with Rs.", self.balance)
#         self.balance -= amount
#         print("Total balance Rs.", self.balance)


# acc = Account(10000)
# acc.credit(9000)
# acc.debited(1000)



#--------------------inheritance---------------


# Three types of inheritance in python singleLevel, multiLevel, and multiple inheritance.
# To inherit parent class into child class we use () breaces.
# super() key word is used to call the constructor or method of the parent class inside the child class.
# order of execution of the constructor is depend on the order of calling.


# single level


# class A:
#     varA = "A class"
#     def __init__(self, name):
#         print("You are inside the parent constructor")
#         self.name = name
    
#     def display(self):
#         print("The name of class is", self.name)

# class B(A):
#     varB = "B class"

#     def __init__(self, name1, name2):
#         super().__init__(name1) 
#         print("You are inside the child constructor")             
#         self.name2 = name2
        
    
#     def show(self):
#         print("The Name of class is ",self.name2)

# child = B("Parent", "child")
# child.display()




# multilevel 



# class A:
#     varA = "A class"
#     def __init__(self, name):
#         self.name = name
    
#     def display(self):
#         print("The name of class is", self.name)

# class B(A):
#     varB = "B class"

#     def __init__(self, name1, name2):
#         super().__init__(name1)             
#         self.name2 = name2
        
#     def show(self):
#         print("The Name of class is ",self.name2)


# class C(B):
    
#     def __init__(self, name1, name2, name3):
#         super().__init__(name1, name2)
#         self.name3 = name3
    
#     def show1(self):
#         print("This is grandchild", self.name3)


# child = C("grandparent", "parent", "child")
# child.show1()



# multiple 


# class A:
#     varA = "A class"
#     def __init__(self, name):
#         self.name = name
    
#     def display(self):
#         print("The name of class is", self.name)

# class B:
#     varB = "B class"

#     def __init__(self, name2):     
#         self.name2 = name2
        
#     def show(self):
#         print("The Name of class is ",self.name2)


# class C(A, B):
    
#     def __init__(self, name1, name2, name3):
#         A.__init__(self, name1)
#         B.__init__(self, name2)
#         self.name3 = name3
    
#     def show1(self):
#         print("The name of the class is ", self.name3)


# child = C("grandparent", "parent", "child")
# child.display()
# child.show()
# child.show1()




# ---------------- polymorphisem -----------------

# poly means many and morphisem mean forms.
# when same things(function/operator) have the different working then it is called as the polymorphisem
# In python polymorhisem is acheive through operator overloadning.
# Operator overloading is acheive with the help of the dunder function.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def show(self):
        print(self.real,"+",self.img,"i")
    
    def __add__(self, num2):                # dunder function
        self.newreal = self.real + num2.real
        self.newimg = self.img + num2.img
        return Complex(self.newreal , self.newimg)
    
num1 = Complex(3, 5)
num1.show()
num2 = Complex(2, 4)
num2.show()
num3 = num1 + num2
num3.show()
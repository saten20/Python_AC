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

class Account:

    def __init__(self, balance):
        self.balance = balance
    
    @staticmethod

    def notes():
        print("Central Bank of India", end =" ")

    def credit(self, amount):
        self.notes()
        print("Account Credited with Rs.", self.balance)
        self.balance += amount
        print("Total balance Rs.", self.balance)

    def debited(self, amount):
        self.notes()
        print("Account Debited with Rs.", self.balance)
        self.balance -= amount
        print("Total balance Rs.", self.balance)


acc = Account(10000)
acc.credit(9000)
acc.debited(1000)
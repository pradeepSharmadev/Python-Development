'''classes is the blueprint of real world objects 
as objects have properties(variable) and methods(functions)
1st create blueprint of object then create as many as required objects
'''

class student:
    def __init__(self,name):
        self.name = name # initialising variable
    
    def welcome(self):
        mmss = f"{self.name} this only can access welcome method" #not visible outside method
        self.mms = f"welcome {self.name}" #acceseble anyware whithin class
        return self.mms ,  mmss
    def check(self):
        return True
    
# main
user = "Pradeep kumar sharma"
obj = student(user)
print(obj.name)
result = obj.welcome()
print(result)
print("Know we are intracting with \n class based programming",obj.welcome())

obj2 = student("Rahul")
print(obj2.name)
print(obj2.check())


#inheritance    
'''properties and method can be acceble in diffrent class and method'''
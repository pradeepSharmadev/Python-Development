class student:
    def __init__(self,name):
        self.name = name
    
    def welcome(self):
        mms = f"welcome {self.name}"
        return mms

# main
user = "Pradeep kumar sharma"
obj = student(user)
print(obj.name)
result = obj.welcome()
print(result)
print("Know we are intracting with \n class based programming",obj.welcome())
"""
Defines the class used to aceess User related Data
@author: Aakash Maurya
"""

class User:
    def __init__(self):
        with open("UserData","rt+") as UserData :
            self._Data = UserData.readline()
        if len(self._Data) == 0:
            self.UserPresent = False
            self._Data = []
        else:
            self.UserPresent = True
            self._Data = self._Data.split(", ")

    def save(self, Record):
        self.Data = Record
        with open("UserData","rt+") as UserData :
            UserData.write(Record[0])
            for i in range(1,5):
                UserData.write(", ")
                UserData.write(Record[i])
        self.UserPresent = True
        with open("UserData","rt+") as UserData :
            self._Data = UserData.readline()
        self._Data = self._Data.split(", ")
    
    def getName(self):
        if self.UserPresent == True:
            return self._Data[0]
        
    def getAge(self):
        if self.UserPresent == True:
            return self._Data[1]
    
    def gerGender(self):
        if self.UserPresent == True:
            return self._Data[2]
    
    def getEmail(self):
        if self.UserPresent == True:
            return self._Data[3]
    
    def getPhone(self):
        if self.UserPresent == True:
            return self._Data[4]


MainUser = User()
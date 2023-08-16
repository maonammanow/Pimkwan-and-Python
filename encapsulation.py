
class student: #class ไพรเวท
    def __init__(self):
        self.ID = 23728
        self.fName = "Pimkwan"
        self.lName = "Chiraprawattrakun"
        self.__score = 30
    def ShowData(self):
        print(self.ID, self.fName, self.lName, self.__score)
    def __updateData(self, degree):
        self.degree = degree
        print(self.ID, self.fName, self.lName, self.__score, self.degree)
        
std = student()
std.ShowData()
std.__score = 50
#std.__student__updateData("YOU ARE NOT MY FATHER") #เรียกแบบไม่ใช่ไพรเวท




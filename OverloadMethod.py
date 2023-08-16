
class Mobile: #class แม่
    def __init__(self): #constructor = __init__
        self.brand = "Barbie"
    def OpenMobile(self):
        return "Open Mobile"
    def __str__(self):
        return "{}","{}".format(self.brand, self.OpenMobile()) #{} = ค่าที่ว่างไว้ก่อน

class MobileOne(Mobile): #สืบทอด class แม่
    def __init__(self):
        super().__init__() 
    def OpenMobile(self):
        return "Open Mobile with Finger Scan"

class MobileTwo(MobileOne):
    def __init__(self):
        super().__init__() 
    def OpenMobile(self):
        return "Open Mobile with Face Scan"


#สร้าง instant(ตัวแปรอ้างอิง) มาเรียกใช้ class
mobile = Mobile()
mobileOne = MobileOne()
mobileTwo = MobileTwo()

m1 = input("Enter Mobile One = ")
mobileOne.brand = m1
m2 = input("Enter Mobile Two = ")
mobileTwo.brand = m2

print(mobile)
print(mobileOne)
print(mobileTwo)

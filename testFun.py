
#ส่งค่า argument, รับค่า parameter 

def student():
    print("Pimkwan")
student() 

def student1(name): # รับค่า name => parameter
    print("Name = ", name)
student1("Pim") #ต้องมีการส่งค่าเข้าไป => argument

def student2():
    name = "Pimkwan"
    return name 
print(student2())  #ฟังก์ชันนี้มีการ return ค่าออกมา ดังนั้นจะต้องสั่ง print ฟังก์ชัน

#def student3(name):
#    name1 = print("Name = ", name)
#    return name1
#print(student3("Ohla"))#

def student3(name):
    name = "kunha"
    return name
print(student3("TTTTTT")) #ฟังก์ชันเรียกใช้ค่าแรกก่อนเสมอ

def student4(name):
    return name
name = input("Enter name = ")
print(student4(name))



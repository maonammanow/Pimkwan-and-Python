
def student(ID,Name):
    info = ID + " " + Name
    return info

def score(a,b,c):
    d = a+b+c
    return d


ID = input("Your student ID = ")
Name = input("Your student name = ")
#student(ID,Name)
#print(student(ID,Name))

a = int(input('Exam 30 points = '))
b = int(input('Collect 60 points = '))
c = int(input('Mind 10 points = '))
#score(a,b,c)
#print(score(a,b,c))

print(student(ID,Name), ", My score = ", score(a,b,c))
    
    
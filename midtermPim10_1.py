
class Student:
    def __init__(self, stuID, stuName, beScore, afScore, examScore):
        self.stuID = stuID
        self.stuName = stuName
        self.beScore = beScore
        self.afScore = afScore
        self.examScore = examScore
    
    def total_Score(self):
        totalScore = self.beScore + self.afScore + self.examScore
        print("Total Score : ", totalScore)
        return totalScore

    def grade(totalScore):
        if totalScore >= 80:
            print("Grade : A")
        elif totalScore >= 70:
            print("Grade : B")
        elif totalScore >= 60:
            print("Grade : C")
        elif totalScore >= 50:
            print("Grade : D")
        else:
            print("Grade : F")
    
class Major(Student):
    def __init__(self, student):
        self.student = student
        
    def getStudent(self):
        self.stuID = input("Student ID : ")
        self.stuName = input("Student Name : ")
        Major = input("Major : ")
        
        self.beScore = int(input("Score Before Midterm (35 points) : "))
        if self.beScore > 35:
            print("Please Try Again")
            return False 
            
        self.afScore = int(input("Score After Midterm (35 points) : "))
        if self.afScore > 35:
            print("Please Try Again")
            return False
        
        self.examScore = int(input("Score Exam (30 points) : "))
        if self.examScore > 30:
            print("Please Try Again")
            return False
        
        return self.beScore, self.afScore, self.examScore
    
A = Major.getStudent(Student)
B = Student.total_Score(Student)
C = Student.grade(B)
print(" ")
D = Major.getStudent(Student)
E = Student.total_Score(Student)
F = Student.grade(E)

#พิมพ์ขวัญ จิระประวัติตระกูล ม.6 CE เลขที่ 10 เลขประจำตัว 23728

class Student:
    def __init__(self):

        self.student_id = input("Student ID : ")
        self.student_name = input("Student Name : ")
        
        self.score_bemid = int(input("Score Before Midterm (35 points) : "))
        self.score_afmid = int(input("Score After Midterm (35 points) : "))
        self.score_exam = int(input("Score Exam (30 points) : "))

    def total_score(self):
        totalScore = self.score_bemid + self.score_afmid + self.score_exam
        print("Total Score : ", totalScore)
        return totalScore

    
    
class Major(Student):
    def __init__(self, student):
        self.student = student
        
    def getStudent(self):
        return self.student
    
    def grade(self, totalScore):
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
    
#A = Major("Pimkwan", "023728", 30, 35, 20)
#C = A.getStudent()
#B = Student()
#B.grade(C)

##student .grade -> major . getscore
#B = Major.getStudent(Student)
D = Student()
C = D.total_score()
E = Major(D)
E.grade(C)
#A = Student.grade(Major.getStudent)


    

        










class Subject:
    def student(id, name):
        id_st = id
        name_st = name
        print(id_st, " ", name_st)
    
    def register(idSubject, nameSubject):
        id_sj = idSubject
        name_sj = nameSubject
        print(id_sj, " ", name_sj)
        
    def drop(idDrop, nameDrop):
        id_drop = idDrop
        name_drop = nameDrop
        print(id_drop, " ", name_drop)

IdSt = input("Enter student ID : ")
nameSt = input("Enter name : ")
a = Subject.student(IdSt, nameSt)

IdSj = input("Enter subject ID : ")
nameSj = input("Enter Subject Name : ")
b = Subject.register(IdSj, nameSj)     
    
IdDrop = input("Enter drop subject ID : ")
nameDrop = input("Enter drop Subject Name : ")
c = Subject.drop (IdDrop, nameDrop) 
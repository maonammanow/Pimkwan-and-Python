#ใช้เขียนโปรแกรมเป็นทีม

class Book: #object หลัง class ไม่ต้องมี วงเล็บ
    #ประกาศตัวแปรให้ method อื่น ใช้ได้ด้วย
    nameBook = "Python" 
    ISBN = 1111111111   
    
    def read(nameBook, isbn): #method
        nameBook = nameBook
        ISBN = isbn
        print(nameBook, ISBN)
        #return nameBook + isbn
    def eat():
        print("กิน")
        
    def mousepad():
        print("รองเมาส์")
        
b = Book.read("Java", 2222222222)

    

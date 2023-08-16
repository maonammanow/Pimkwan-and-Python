
from tkinter import*
from tkinter import ttk

mainFrame = Tk()
mainFrame.title("Python GUI")

#การสร้าง Label Widget
labelTitle = ttk.Label(mainFrame, text = "โปรแกรมการคำนวณ")
labelNumber1 = ttk.Label(mainFrame, text = "ป้อนตัวเลขที่ 1 : ")
labelNumber2 = ttk.Label(mainFrame, text = "ป้อนตัวเลขที่ 2 : ")
labelTotal = ttk.Label(mainFrame, text = "ผลลัพธ์ : ")


#การจัดวางตำแหน่ง Widget
labelTitle.grid(column=0, columnspan=2, padx=150, pady=10)
labelNumber1.grid(column=0, row=2, padx=5, sticky="NE") #sticky = บอกทิศ
labelNumber2.grid(column=0, row=3, padx=5, sticky="NE") 
labelTotal.grid(column=0, row=4, padx=5, sticky="NE") 

#การวางตำแหน่ง Widget Entry
EntryNumber1 = ttk.Entry(mainFrame, width=25).grid(column=1, row=2, sticky="W")
EntryNumber2 = ttk.Entry(mainFrame, width=25).grid(column=1, row=3, sticky="W")
EntryTotal = ttk.Entry(mainFrame, width=25).grid(column=1, row=4, sticky="W")

#การทำ button
buttonClick = ttk.Button(mainFrame, text="Click", width=10)
buttonClear = ttk.Button(mainFrame, text="Clear", width=10)

buttonClick.grid(column=0, row=5, pady=10, sticky="NE")
buttonClear.grid(column=1, row=5, padx=10, sticky="W")



mainFrame.mainloop()
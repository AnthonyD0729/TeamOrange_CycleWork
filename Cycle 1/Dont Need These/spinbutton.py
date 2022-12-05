from tkinter import *
  
root = Tk()
root.geometry("300x200")
  
w = Label(root, text ='How Many Bots Do You Want?', font = "50") 
w.pack()
  
sp = Spinbox(root, from_= 0, to = 6)
sp.pack()
  
root.mainloop() 
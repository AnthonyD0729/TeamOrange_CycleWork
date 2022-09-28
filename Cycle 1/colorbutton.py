from tkinter import *
from tkinter import messagebox   
  
top = Tk()  
  
top.geometry("200x100")  
  
def red():  
    messagebox.showinfo("Hello", "Red Button clicked")  
def blue():  
    messagebox.showinfo("Hello", "Blue Button clicked")  
def green():  
    messagebox.showinfo("Hello", "Green Button clicked")  
def yellow():  
    messagebox.showinfo("Hello", "Yellow Button clicked")  
  
  
b1 = Button(top,text = "Red",command = red,activeforeground = "red",activebackground = "black",pady=10)  
  
b2 = Button(top, text = "Blue",command = blue,activeforeground = "blue",activebackground = "black",pady=10)  
  
b3 = Button(top, text = "Green",command = green, activeforeground = "green",activebackground = "black",pady = 10)  
  
b4 = Button(top, text = "Yellow",command = yellow, activeforeground = "yellow",activebackground = "black",padx =10,pady = 10)  
  
b1.pack(side = LEFT)  
  
b2.pack(side = RIGHT)  
  
b3.pack(side = TOP)  
  
b4.pack(side = BOTTOM)  
  
top.mainloop()  
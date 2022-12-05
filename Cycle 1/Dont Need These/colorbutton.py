from tkinter import *
from tkinter import messagebox   
  
top = Tk()  
  
top.geometry("200x100")  
  
def red():  
    messagebox.showinfo("Hello", "Start Button clicked")  
def blue():  
    messagebox.showinfo("Hello", "Quit Button clicked")  
def green():  
    messagebox.showinfo("Hello", "Green Button clicked")  
def yellow():  
    messagebox.showinfo("Hello", "Yellow Button clicked")  
  
  
b1 = Button(text = "Start",command = red,activeforeground = "red",activebackground = "black",pady=10)  
b1.place(x=0, y=60)  
b2 = Button(text = "Quit",command = blue,activeforeground = "blue",activebackground = "black",pady=10)  
b2.place(x=165, y=60)
  
top.mainloop()  
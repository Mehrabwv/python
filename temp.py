from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      

img = PhotoImage(file='gif-file.gif')      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()

# C:\Users\mehra\python>python temp.py
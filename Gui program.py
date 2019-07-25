from tkinter import*
window = Tk()
window.geometry("1600x800")
window.configure(bg="light green")
f1=Frame(window,height=50, width=500)
text1=Entry(f1)
b1=Button(f1,text="ok")
f1.pack()
text1.pack(side=BOTTOM)

b1.pack(side=RIGHT)

window.mainloop()

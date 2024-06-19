import tkinter

window = tkinter.Tk()
window.title("Tkinter Deneme")
window.minsize(600, 600)

#label
myLabel = tkinter.Label(text="Hello Tkinter")
myLabel.config(bg="black", fg="white", font=("Arial", 24, "bold"))
myLabel.pack()
def clickedFunction():
    print(myEntry.get())

#button
myButton = tkinter.Button(text="This is a button", command=clickedFunction)
myButton.place(x=300-myButton.winfo_reqwidth()//2, y=300-myButton.winfo_reqheight()//2)


#entry
myEntry = tkinter.Entry(width="20")
myEntry.pack()
window.mainloop()
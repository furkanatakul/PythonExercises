from tkinter import *

win = Tk()
win.title("Hello Python")
win.minsize(600,600)

label=Label(text="MyLabel")
label.config(padx=10, pady=20)
label.pack()

def buttonClicked():
    print(myText.get("1.0", END))

button = Button(text="MyButton", command=buttonClicked)
button.config(bg="Black", fg="white")
button.pack()

entry = Entry(width=20)
entry.pack()

#multiline
#text
myText = Text(width=30,height=10)
myText.focus()
myText.pack()

def scaleSelected(value):
    print(value)
#scale
myScale = Scale(from_=0, to=50,command=scaleSelected)
myScale.pack()

def spinboxSelected():
    print(mySpinbox.get())
#spinbox
mySpinbox = Spinbox(from_=0, to=50, command=spinboxSelected)
mySpinbox.pack()

def isSelected():
    print(checkState.get())

#checkbutton
checkState = IntVar()
myCheckbutton =Checkbutton(text="CheckButton",variable=checkState,command=isSelected)
myCheckbutton.pack( )

#radioButton
def isSelectedRadio():
    print(radioCheckState.get())
radioCheckState = IntVar()
myRadiobutton = Radiobutton(text="Option1", value=10, variable=radioCheckState, command=isSelectedRadio)
myRadiobutton2 = Radiobutton(text="Option2", value=20, variable=radioCheckState, command=isSelectedRadio)
myRadiobutton.pack()
myRadiobutton2.pack()

#listbox
def listboxSelect(event):
    print(myListBox.get(myListBox.curselection()))

myListBox = Listbox()
nameList = ["Furkan", "Atakul", "Selam", "Merhaba"]

for i in range(len(nameList)):
    myListBox.insert(i,nameList[i])
myListBox.bind('<<ListboxSelect>>',listboxSelect)
myListBox.pack()

win.mainloop()
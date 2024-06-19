from tkinter import *
window = Tk()
window.title("BMI Calculator")
window.minsize(450, 300)
window.config(pady=10)

myLabel1 = Label(text="Enter your Height(cm)", font=('Arial','15'))
myLabel1.pack(pady=10)

myEntry = Entry(width=10, font=('Arial','20'))
myEntry.pack()

myLabel2 = Label(text="Enter your Weight(kg)", font=('Arial','15'))
myLabel2.pack(pady=10)

myEntry2 = Entry(width=10, font=('Arial','20'))
myEntry2.pack()

def calculate():
    height_text = myEntry.get()
    weight_text = myEntry2.get()

    if not height_text or not weight_text:
        myLabel3.config(text="Fill in both fields!")
        myLabel3.pack()
        return
    try:
        weight = float(weight_text)
        height = float(height_text) / 100
        BMI = weight / (height ** 2)
        if BMI < 16:
            text = "Severely Underwight"
        elif BMI < 18.5:
            text = "Underwight"
        elif BMI < 25:
            text = "Normal"
        elif BMI < 30:
            text = "Overweight"
        elif BMI < 35:
            text = "Moderately Obese"
        elif BMI < 40:
            text = "Severely Obese"
        elif BMI >= 40:
            text = "Morbidly Obese"
        myLabel3.config(text=f"Your BMI is: {BMI:.2f}, You are {text}")
        myLabel3.pack(pady=10)
    except:
        myLabel3.config(text="Invalid Value!!")
        myLabel3.pack(pady=10)
myButton = Button(text="Calculate",command=calculate, font=('Arial','15'))
myButton.pack(pady=10)

myLabel3 = Label(font=('Arial','15'))
window.mainloop()
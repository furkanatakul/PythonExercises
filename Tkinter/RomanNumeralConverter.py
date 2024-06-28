from tkinter import *
from tkinter import ttk, messagebox

window = Tk()
window.minsize(1230,600)
window.title("Roman Numeral Converter")

label1 = Label(text="Enter Roman Number",font=('Arial','21'))
label1.place(x=475,y=150)

entry1 = Entry(width=50,font=('Arial','21'),justify='center')
entry1.place(x=213,y=200,height=50)


entry2 = Entry(state="readonly",width=50,font=('Arial','21'),justify='center')
entry2.place(x=213,y=400,height=50)

lst = [
    ("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100),
    ("D", 500), ("M", 1000), ("_I", 1000), ("_V", 5000),
    ("_X", 10000), ("_L", 50000), ("_C", 100000), ("_D", 500000), ("_M", 1000000)
]
total_rows = len(lst)
total_columns = len(lst[0])
for i in range(total_rows):
    for j in range(total_columns):
        e = Entry(window, width=7, fg='black', justify='center',
                  font=('Arial', 16, 'bold'))

        e.grid(row=j, column=i)
        e.insert(END, lst[i][j])
        e.config(state="readonly")
def convertFunction():
    num = str(entry1.get().strip())
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "_": 0.5}
    sum = 0
    i = 0
    x = 1
    y = 1
    while i > -1:
        if x == 1:
            i = len(num) - 1
        try:
            if len(num) == 3 and num[i] == num[i-1] == num[i-2] and num[i] in ("I", "X", "C", "M"):
                sum =3 * roman[num[i]]
                i = -1
            elif len(num) == 6 and num[i] == num[i-2] == num[i-4] and num[i] in ("I", "X", "C", "M") and num[i-1] == num[i-3] == num[i-5] == "_":
                sum =3000 * roman[num[i]]
                i = -1
            elif len(num) == 1:
                sum = roman[num[i]]
                i = -1
            elif len(num) == 2 and roman[num[i - 1]] == 0.5:
                sum = 1000 * roman[num[i]]
                i = -1
            elif roman[num[i - 1]] != 0.5:
                if roman[num[i]] / x == 10 and roman[num[i - 1]] / x == 1:
                    sum += 9 * x
                    i -= 2
                    x *= 10
                    continue
                elif roman[num[i]] / x == 5:
                    if roman[num[i - 1]] / x == 1:
                        sum += 4 * x
                        i -= 2
                        x *= 10
                        continue
                    else:
                        sum += 5 * x
                        i -= 1
                        x *= 10
                        continue
                elif roman[num[i]] / x == 1 and roman[num[i - 1]] / x != 5:
                    if roman[num[i - 1]] / x == 1 and roman[num[i - 2]] / x != 5:
                        if roman[num[i - 2]] / x == 1 and roman[num[i - 3]] / x != 1:
                            if roman[num[i - 3]] / x == 5:
                                sum += 8 * x
                                i -= 4
                                x *= 10
                                continue
                            sum += 3 * x
                            i -= 3
                            x *= 10
                            continue
                        sum += 2 * x
                        i -= 2
                        x *= 10
                        continue
                    if roman[num[i - 1]] / x == 1 and roman[num[i - 2]] / x == 5:
                        sum += 7 * x
                        i -= 3
                        x *= 10
                        continue
                    sum += x
                    i -= 1
                    x *= 10
                    continue
                elif roman[num[i]] / x == 1 and roman[num[i - 1]] / x == 5:
                    sum += 6 * x
                    i -= 2
                    x *= 10
                    continue
                else:
                    if x < 1000:
                        x *= 10
                        continue
                    raise Exception("Invalid Input!!")
            elif roman[num[i - 1]] == 0.5:
                if roman[num[i]] / y == 10 and roman[num[i - 2]] / y == 1:
                    sum += 9000 * y
                    i -= 4
                    y *= 10
                    continue
                elif roman[num[i]] / y == 5:
                    if roman[num[i - 2]] / y == 1:
                        sum += 4000 * y
                        i -= 4
                        y *= 10
                        continue
                    else:
                        sum += 5000 * y
                        i -= 2
                        y *= 10
                        continue
                elif roman[num[i]] / y == 1 and roman[num[i - 2]] / y != 5:
                    if roman[num[i - 2]] / y == 1 and roman[num[i - 4]] / y != 5:
                        if roman[num[i - 4]] / y == 1 and roman[num[i - 6]] / y != 1:
                            if roman[num[i - 6]] / y == 5:
                                sum += 8000 * y
                                i -= 8
                                y *= 10
                                continue
                            sum += 3000 * y
                            i -= 6
                            y *= 10
                            continue
                        sum += 2000 * y
                        i -= 4
                        y *= 10
                        continue
                    if roman[num[i - 2]] / y == 1 and roman[num[i - 4]] / y == 5:
                        sum += 7000 * y
                        i -= 6
                        y *= 10
                        continue
                    sum += 1000 * y
                    i -= 2
                    y *= 10
                    continue
                elif roman[num[i]] / y == 1 and roman[num[i - 2]] / y == 5:
                    sum += 6000 * y
                    i -= 4
                    y *= 10
                    continue
                else:
                    if y < 1000:
                        y *= 10
                        continue
                    raise Exception("Invalid Input!!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            break
    entry2.config(state="normal")
    entry2.delete(0, END)
    entry2.insert(0, str(sum))
    entry2.config(state="readonly")
button = Button(text="Convert", command=convertFunction,font=('Arial','21'))
button.place(x=555,y=300)
window.mainloop()
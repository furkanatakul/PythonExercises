from tkinter import *
from tkinter import ttk, messagebox
from ExchangeRateAPI import *
import requests 
FONT=('Arial','18')

window = Tk()
window.minsize(800,600)
window.title("Currency Converter")

label1 = Label(text="Amount",font=FONT)
label1.place(x=122,y=150)

label2 = Label(text="From",font=FONT)
label2.place(x=360,y=150)

label3 = Label(text="To",font=FONT)
label3.place(x=580,y=150)

entry1 = Entry(width=10,font=FONT)
entry1.place(x=100,y=200)

variable1 = StringVar(window)
variable1.set(OPTIONS[0])
variable2 = StringVar(window)
variable2.set(OPTIONS[0])
w = ttk.Combobox(window, textvariable=variable1, values=OPTIONS,font=('Arial','15'),width=10)
w.place(x=330,y=200)
w2 = ttk.Combobox(window, textvariable=variable2, values=OPTIONS,font=('Arial','15'),width=10)
w2.place(x=550,y=200)

entry2 = Entry(state="readonly",width=40,font=('Arial','21'),justify='center')
entry2.place(x=70,y=400,height=50)
def convertFunction():
    try:
        amount = float(entry1.get().strip())
        fromCurrency = w.get()
        toCurrency = w2.get()
        url = apikey + fromCurrency
        response = requests.get(url)
        if response.status_code == 200:
            conversationRates = response.json()["conversion_rates"]
            for (x, y) in conversationRates.items():
                if toCurrency in x:
                    result = f"{amount} {fromCurrency} = {(y * amount):.2f} {toCurrency}"
                    entry2.config(state="normal")
                    entry2.delete(0, END)
                    entry2.insert(0, result)
                    entry2.config(state="readonly")
                    break
        else:
            raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
button = Button(text="Convert", command=convertFunction,font=FONT)
button.place(x=340,y=300)
window.mainloop()
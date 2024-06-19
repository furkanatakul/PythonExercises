import base64
from tkinter import *
from tkinter import messagebox
import nacl.secret
import nacl.utils
import hashlib
from PIL import ImageTk, Image
window = Tk()
window.title("Secret Note")
window.minsize(750,600)
window.config(padx=10)
FONT=('Arial','15')
myLabel1 = Label(text="Enter Your Title", font=FONT)
myLabel1.place(x=100,y=10)
myEntry = Entry(width=30,font=FONT)
myEntry.place(x=0,y=50)
myLabel2 = Label(text="Enter Your Secret", font=FONT)
myLabel2.place(x=90,y=90)
myText1 = Text(width=42,height=20)
myText1.place(x=0,y=130)
myLabel3 = Label(text="Enter Master Key", font=FONT)
myLabel3.place(x=90,y=470)
myEntry1 = Entry(width=30,font=FONT)
myEntry1.place(x=0,y=510)
img = ImageTk.PhotoImage(Image.open("image.jpg"))
panel = Label(image = img)
panel.place(x=360,y=40)
myLabel4 = Label(font=FONT)
def generate_key():
    user_key_bytes = myEntry1.get().encode('utf-8')
    if user_key_bytes:
        hashed_key = hashlib.sha256(user_key_bytes).digest()
        key = hashed_key[:nacl.secret.SecretBox.KEY_SIZE]
        return key
    raise Exception("Master key cannot be empty")
def encrypt(key):
    box = nacl.secret.SecretBox(key)
    if not len(myText1.get("1.0", "end-1c")) == 0:
        plaintext = myText1.get(1.0, END)
        plaintext_bytes = plaintext.encode('utf-8')
        encrypted = box.encrypt(plaintext_bytes)
        return encrypted
    raise Exception("Secret cannot be empty")
def encryptWrite():
    try:
        key = generate_key()
        encrypted = encrypt(key)
        encrypted_base64 = base64.b64encode(encrypted).decode('utf-8')
        try:
            text_file = open("Secrets.txt", "a")
            text_file.write("Title: " + myEntry.get() + '\n' + encrypted_base64 + '\n' + "---------------------------------------------------------------------------------------------------------------------------------------------" + '\n')
            text_file.close()
        except FileNotFoundError:
            text_file = open("Secrets.txt", "w")
            text_file.write("Title: " + myEntry.get() + '\n' + encrypted_base64 + '\n' + "---------------------------------------------------------------------------------------------------------------------------------------------" + '\n')
            text_file.close()
        myLabel4.config(text="Encrypt Successful")
        myLabel4.place(x=360, y=470)
        myEntry.delete(0,END)
        myEntry1.delete(0,END)
        myText1.delete("1.0", END)
    except Exception as e:
        messagebox.showinfo("Encrypt Error", str(e))
myButton1 = Button(text="Save & Encrypt",command=encryptWrite)
myButton1.config(width=31,font=FONT)
myButton1.place(x=360,y=320)
def decrypt():
    try:
        key = generate_key()
        box = nacl.secret.SecretBox(key)
        encrypted = encrypt(key)
        encrypted_base64 = myText1.get(1.0, END)
        encrypted_decoded = base64.b64decode(encrypted_base64.encode('utf-8'))
        decrypted_bytes = box.decrypt(encrypted_decoded)
        decrypted_text = decrypted_bytes.decode('utf-8')
        myText1.delete('1.0', END)
        myText1.insert('1.0', decrypted_text)
        myLabel4.config(text="Decrypt Successful")
        myLabel4.place(x=360, y=470)
        myEntry.delete(0,END)
        myEntry1.delete(0,END)
    except Exception as e:
        messagebox.showinfo("Decrypt Error", str(e))
myButton1 = Button(text="Decrypt",command=decrypt)
myButton1.config(width=31,font=FONT)
myButton1.place(x=360,y=420)
window.mainloop()
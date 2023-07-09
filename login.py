from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
from main_frame import MainFrame

#----LOG IN sqlite3 dizanje---
def log_in():
    try:
        connection = sqlite3.connect('users.db')
    except Exception as ex:
            messagebox.showerror(message=f'ERROR: {ex}')
    
    cursor = connection.cursor()
    cursor.execute('SELECT username, password FROM login')
    rows = cursor.fetchall()
    
    for row in rows:
        username, password = row
    
    if password_entry.get() == password and user_entry.get() == username:
        messagebox.showinfo(message='Uspješno ste se prijavili u aplikaciju pyPosude', )
        login.destroy()
        window = MainFrame()
        window.load
    else:
        messagebox.showwarning(message='Krivo uneseni podatci')
    cursor.close()
    connection.close()
#----LOGIN-------
login = Tk()
image_login = Image.open('login_img.jpg')

photo_image = ImageTk.PhotoImage(image_login)
label_img = Label(login, image=photo_image)
label_img.grid(column = 0, row =0)
login.resizable(0,0)
login.config( padx= 5, pady=5,)
login.geometry('350x150')
login.title('Login')

login.rowconfigure(0, weight=1)
login.columnconfigure(0, weight =1)

#----Labelframe---
login_frame = LabelFrame(login,  borderwidth =4,  )
login_frame.grid(column =0, row =0, padx=5, pady=5, sticky =NSEW,)
login_frame.columnconfigure((0,1), weight = 0)
login_frame.rowconfigure((0,1), weight = 0)

#----Labels------
user_label = Label(login_frame, text='Username:', width =20)
user_label.grid(column = 0, row = 0, pady=5, padx=5)


password_label = Label(login_frame, text = 'Password:', width =20)
password_label.grid(column=0, row = 1, pady=5, padx=5)

#----Entry------
user_entry = Entry(login_frame, width = 20)
user_entry.grid(column = 1, row = 0,pady=5, padx=5, sticky = W)
user_entry.focus()

password_entry = Entry(login_frame, width = 20, show ='*')
password_entry.grid(column=1, row =1,pady=5, padx=5, sticky = W)

#----Button-----
login_button = Button(login_frame,
                      text = 'Login',
                      command = log_in,
                      width = 10,
                      border = 3,                                   
                      padx=5,
                      pady=5,
                      bg= '#B0E0E6',
                      overrelief =GROOVE,
                      activebackground='Light blue')
login_button.grid(column = 0, row =2,pady=5, padx=5)

login.mainloop()
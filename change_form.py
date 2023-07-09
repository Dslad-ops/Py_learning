from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from generator import Database
from main_frame import MainFrame
from frames_for_main import add_new


class ChangeForm(LabelFrame):
    def __init__(self, master= None):
        LabelFrame.__init__(self, master )
        self.columnconfigure((0,1,2,3,4,5), weight =1)    
        self.rowconfigure((0,1,2,3,4,5,6,7), weight =1)
        
    def save_button(self):
        self.button_save = Button(self,
                                    text = 'Spremi',
                                    command = None,
                                    width = 12,
                                    font=('Viner hand ITC',10,),
                                    border = 3,                                   
                                    padx=5,
                                    pady=5,
                                    bg= '#B0E0E6',
                                    overrelief =GROOVE,
                                   activebackground='Light blue')
        self.button_save.grid( column = 5, row = 0)
        
def browse(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select a File")
        print("Selected file:", self.filename)
        

if __name__ == '__main__':
    window = MainFrame()
    f = ChangeForm(window)
    
    f.grid(column = 0, row = 3, sticky = N)
    window.mainloop()
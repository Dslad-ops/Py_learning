from tkinter import *
from info import InfoFrame

class MainFrame():
    def __init__(self, master=None):
        self.window = Tk()
        self.window.title('PyPosuda')
        self.window.geometry('830x600')
        self.window.columnconfigure((0,1,2), weight =1)
        self.window.config(padx=20, pady=20, bg ='#C1CDCD',  )
        self.window.resizable(1,1)
        
        self.window.mainloop()
        
#-----donji frame-varijabilni----          
class LowerFrame(LabelFrame):
    def __init__(self, master):
        LabelFrame.__init__(self,master, 
        
        padx = 10,
        pady = 10)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.config(width=master.winfo_width(), height=master.winfo_height())
        self.canvas(master)
    
        
    def canvas(self,master):
        self.canvas = Canvas(self)
        self.canvas.grid(column= 0, row = 0, rowspan = 3, columnspan =3, sticky = NSEW)
        self.canvas.config(width=master.winfo_width(), height=master.winfo_height())
        self.scrollbar = Scrollbar(self.canvas, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(column=2, row=0, sticky=N+S+E)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        
        

        
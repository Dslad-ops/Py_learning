from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from main_frame import MainFrame
from PIL import Image, ImageTk

class Database(LabelFrame):
    def __init__(self, master= None):
        LabelFrame.__init__(self, master )
        self.columnconfigure((0,1,2,3,4,5), weight =1)    
        self.rowconfigure((0,1,2,3,4,5,6,7), weight =1)
       
        
    def database_canvas(self, ):
        self.canvas_db = Canvas(self, height = 450, width = 800) 
        self.canvas_db.grid(column = 0 , row = 0, rowspan = 8, columnspan = 6, sticky = NSEW) 
        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.canvas_db.yview, troughcolor="red")
        self.scrollbar.grid(column = 5, row = 0 , rowspan =8, sticky=N+E+S)
        self.canvas_db.configure(yscrollcommand=self.scrollbar.set)
        
        
    def update_button(self):
        self.button_update = Button(self,
                                    text = 'Ažuriraj',
                                    command = None,
                                    width = 12,
                                    font=('Viner hand ITC',10,),
                                    border = 3,                                   
                                    padx=5,
                                    pady=5,
                                    bg= '#B0E0E6',
                                    overrelief =GROOVE,
                                   activebackground='Light blue')
        self.button_update.grid( column = 5, row = 7)
        
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
        self.button_save.grid( column = 0, row = 5, sticky= E)
    
    def browse_button(self):
        self.button_browse = Button(self,
                                    text = 'Traži sliku',
                                    command = self.browse,
                                    width = 12,
                                    font=('Viner hand ITC',10,),
                                    border = 3,                                   
                                    padx=5,
                                    pady=5,
                                    bg= '#B0E0E6',
                                    overrelief =GROOVE,
                                   activebackground='Light blue')
        self.button_browse.grid( column = 5, row = 5, sticky= W)
        
    def labels(self):
        self.label_ime = Label(self, text = 'Ime cvijeta', font=('Viner hand ITC',10,))
        self.label_ime.grid(row = 0, column = 0, sticky = W)
        
        self.label_water = Label(self, text = 'Frekvencija zaljevanja', font=('Viner hand ITC',10,))
        self.label_water.grid(row = 1, column = 0, sticky = W)
        
        self.label_ph = Label(self, text = 'pH (kiselo/lužnato)', font=('Viner hand ITC',10,))
        self.label_ph.grid(row = 2, column = 0, sticky = W)
        
        self.label_light = Label(self, text = 'Količina svjetlosti', font=('Viner hand ITC',10,))
        self.label_light.grid(row = 3, column = 0, sticky = W)
        
        self.label_temperature = Label(self, text = 'Temperatura', font=('Viner hand ITC',10,))
        self.label_temperature.grid(row = 4, column = 0, sticky = W)
       
    def entry(self):
        self.entry_ime = Entry(self, width = 30, )
        self.entry_ime.grid(row = 0, column = 1, sticky = W, padx = 10, pady =10)
        
        self.entry_water = Entry(self, width = 30, )
        self.entry_water.grid(row = 1, column = 1, sticky = W, padx = 10, pady =10)
        
        self.entry_ph = Entry(self, width = 30)
        self.entry_ph.grid(row = 2, column = 1, sticky = W, padx = 10, pady =10)
        
        self.entry_light = Entry(self, width = 30)
        self.entry_light.grid(row = 3, column = 1, sticky = W, padx = 10, pady =10)
        
        self.entry_temperature = Entry(self, width = 30)
        self.entry_temperature.grid(row = 4, column = 1, sticky = W, padx = 10, pady =10)
    
    def browse(self):
        self.filename = filedialog.askopenfilename(initialdir="./", title='Odaberi sliku')
        print("Selected file:", self.filename)
        self.image = Image.open(self.filename)
        self.image = self.image.resize((200,200))
        self.photo_flower = ImageTk.PhotoImage(self.image)
        self.canvas_db.create_image((680,150), image = self.photo_flower, anchor = CENTER)
       
if __name__ == '__main__':
    window = MainFrame()
    f = Database(window)
    f.database_canvas()
    f.update_button()
    f.labels()
    f.grid(column = 0, row = 1, sticky = N)
    f.grid_forget()
    
    g =  Database(window)
    g.database_canvas()
    g.save_button()
    g.browse_button()
    g.labels()
    g.entry()
    g.grid(column = 0, row = 1, sticky = N)
    window.mainloop()
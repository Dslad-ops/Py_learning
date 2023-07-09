from tkinter import *
from PIL import Image, ImageTk
from info import InfoFrame

class PosudaLabelFrame(LabelFrame):
    def __init__(self,id, name, master):
        LabelFrame.__init__(self,master)
        self.id = id
        self.name = name
        self.columnconfigure((0,1,2,3,4,5), weight =1)
        self.rowconfigure((0,1,2,3,4,5), weight =1)
        self.image_flower = Image.open('ruza.png')
        self.resize = self.image_flower.resize((100,100))
        self.photo_flower = ImageTk.PhotoImage(self.resize)
        
        # self.add_new()  
    def posuda(self):
        self.posuda_canvas = Canvas(self, width = 150, height =100)
        self.posuda_canvas.create_image(50,50,image =self.photo_flower, anchor = 'center')
        self.posuda_canvas.grid(column =0, row = 0)
        
        self.posuda_name_label = Label(self, text = self.name, font=('Viner hand ITC',10,))
        self.posuda_name_label.grid(column=1, row =0, sticky = W)
        
        self.status_posuda_label = Label(self, text = 'Status:', font=('Viner hand ITC',10,))
        self.status_posuda_label.grid(column=0, row =1, sticky = W)
        
        self.enter_status_label = Label(self, text = 'Dodati funkciju za text:', font=('Viner hand ITC',10,))
        self.enter_status_label.grid(column=1, row =1, sticky = W)
        
        self.change_button = Button(self, 
                                    text = 'Postavke',
                                    font=('Viner hand ITC',12),
                                    command = None,
                                    border = 4,                                    
                                    padx=1,
                                    pady=1,
                                    bg= '#B0E0E6',
                                    overrelief =GROOVE,
                                    activebackground='Light blue')
        self.change_button.grid(column =1, row =4, sticky = SE)
        
    def add_new(self): 
        self.posuda_canvas_2 = Canvas(self, width = 150, height =100)
        self.posuda_canvas_2.grid(column =0, row = 0, sticky = NSEW )
         
        self.add_new_button = Button(self, 
                                    text = 'Dodaj novu posudu',
                                    font=('Viner hand ITC',12),
                                    command = self.add_new_command,
                                    border = 4,                                    
                                    padx=1,
                                    pady=1,
                                    bg= '#B0E0E6',
                                    overrelief =GROOVE,
                                    activebackground='Light blue')
        self.add_new_button.grid(column = 1 , row = 1, sticky = NSEW)
        
    def add_new_command(self,):
        self.posuda_info = InfoFrame(master=None)
        self.posuda_info.config(width = 600, height =400,borderwidth=4, )
        self.posuda_info.grid(column =0, row =0, sticky = NS)
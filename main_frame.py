from tkinter import *
from PIL import Image, ImageTk
from posude import PosudaLabelFrame
import sqlite3
from tkinter import messagebox
from profil import Profile
from frames_for_main import LowerFrame

#---Klasa za prozor-------
class MainFrame(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        
        self.title('PyPosuda')
        self.geometry('830x700')
        self.columnconfigure((0,1,2), weight =1)
        self.rowconfigure((0,1,2), weight =1)
        self.label_frame = LabelFrameUpper(self)
        self.label_frame.grid(column = 0, row =0, columnspan=3, rowspan =1 )
        self.label_frame.configure(borderwidth=4, bg='#F5FFFA')
        self.config(padx=20, pady=20, bg ='#C1CDCD',  )
        self.resizable(0,1)
        self.lower_frame = LowerFrame(self)
        self.lower_frame.grid(column = 0, row =2, columnspan = 3, sticky = NSEW)
        
        
        
        
       
        # self.load()
        
#-----dizanje posuda iz baze-----        
    def load(self):
        self.column_row_list = []
        try:
            connection = sqlite3.connect('data.db')
        except Exception as ex:
            messagebox.showerror(message=f'ERROR: {ex}')
    
        cursor = connection.cursor()
        cursor.execute('SELECT ID, name, column, row FROM posude')
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        
        for posuda in rows:
            id, name, column_grid, row_grid = posuda
            if id == '' :
                self.posuda_create = PosudaLabelFrame(master = self.lower_frame )
                self.posuda_create.add_new()
                self.posuda_create.grid(column = 0, row = 0, sticky =N, pady=5)
                
            else:
                self.column_row_list.append([column_grid, row_grid])
                self.posuda_create = PosudaLabelFrame(id = id, name = name, master = self.lower_frame, )
                self.posuda_create.posuda()
                self.posuda_create.grid(column = column_grid, row = row_grid, sticky =N, pady=5)

        index = len(self.column_row_list)
        new_column, new_row = self.column_row_list[index-1]
        self.posuda_create = PosudaLabelFrame( master = self.lower_frame, id=None, name = None )
        self.posuda_create.add_new()
        if new_column == 0:
                    self.posuda_create.grid(column = 1, row = new_row, sticky =N, pady=5)
        else:
                    self.posuda_create.grid(column = 0, row = (new_row+1), sticky =N, pady=5)
                
#----Klasa za gornji frame +widgets---
class LabelFrameUpper(LabelFrame):
    def __init__(self, master):
        LabelFrame.__init__(self, master)
        self.image_frame = Image.open('Untitled.jpg')
        self.photo_image = ImageTk.PhotoImage(self.image_frame)
        self.sticky = NSEW
        self.columnconfigure((0,1,2), weight =1)
        self.rowconfigure((0,1,2), weight =1)
        self.top_picture_frame()
          
    def top_picture_frame(self):
#---canvas---------       
        self.image_canvas = Canvas(self, width = 800, height =100 )
        self.image_canvas.grid(column=0, row=0, columnspan = 5)
        self.image_canvas.create_image(400,50,image = self.photo_image, anchor='center')
        self.image_canvas.create_text(400,85, text='PyFlora Posude', font=('Viner hand ITC',16,'bold'))
#----buttons--------      
        self.button_profile = Button(self,
                                    text = 'Moj profil',
                                    font=('Viner hand ITC',12,),
                                    height = 1,
                                    command = self.open_profile,
                                    width = 10,
                                    border = 4,                                    
                                    padx=5,
                                    pady=5,
                                    bg= '#B0E0E6',
                                    overrelief =GROOVE,
                                    activebackground='Light blue')
        
        self.button_profile.grid(column = 4, row =1, sticky = SE)
        
        self.button_sync= Button(self, 
                                    text = 'Sync',
                                    font=('Viner hand ITC',12,),
                                    height = 1,
                                    command = None,
                                    width = 10,
                                    border = 4,                                   
                                    padx=5,
                                    pady=5,
                                    bg= '#B0E0E6',
                                    overrelief =GROOVE,
                                    activebackground='Light blue')
        self.button_sync.grid(column = 0, row =1, sticky = W)
        
#----otvaranje prozora sa profilom-----    
    def open_profile(self):
        profile = Profile()
        

        
                              
if __name__ == '__main__':
    window = MainFrame()
    window.load()
    window.mainloop()
    
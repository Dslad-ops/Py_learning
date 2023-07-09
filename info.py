from tkinter import *
from PIL import Image, ImageTk

from tkinter import messagebox

class InfoFrame(LabelFrame):
    def __init__(self, master):
        LabelFrame.__init__(self,master)
        self.columnconfigure((0,1,2,3), weight =1)
        self.rowconfigure((0,1,2), weight = 1)
        
        self.height = 600
        self.width = 800
        self.image_flower = Image.open('ruza.png')
        self.resize = self.image_flower.resize((200,200))
        self.photo_flower = ImageTk.PhotoImage(self.resize)
        self.widgets()
        
    def widgets(self):
#---naziv--labels--------        
        self.posuda_title_label = Label(self, text = 'Naziv posude: ', font=('Viner hand ITC',12,) )
        self.posuda_title_label.grid(column=0, row= 0, sticky = W, padx=10)
        
        self.posuda_title_show = Label(self, text = 'aaa')
        self.posuda_title_show.grid(column = 0, row = 0, sticky = E, padx=10)
        
        self.canvas_a = Canvas(self, width = 800, height = 400 )
        self.canvas_a.grid(column = 0, row = 0,padx=10 )
        
#----button-------
        self.posuda_button_promijeni = Button(self,
                                                text = 'Promijeni',
                                                font=('Viner hand ITC',12,),
                                                height = 1,
                                                command = None,
                                                width = 10,
                                                border = 4,                                    
                                                padx=1,
                                                pady=1,
                                                bg= '#B0E0E6',
                                                overrelief =GROOVE,
                                                activebackground='Light blue')
        self.posuda_button_promijeni.grid(column = 1, row = 0, sticky = E)
        
#----Canvas--------
        self.flower_show_canvas = Canvas(self, width = 200, height = 200 )
        self.flower_show_canvas.grid(column = 1, row = 1, sticky = E,padx=10 )
        self.flower_show_canvas.create_image(100,100, image = self.photo_flower, anchor='center')
        
        self.graph_show_canvas =  Canvas(self, bg = 'red' )
        self.graph_show_canvas.grid(column = 0, columnspan =2, row = 3, sticky = NSEW, padx=30, pady = 30)       
                                    
if __name__ == '__main__' :
    window = Tk()  
    window.geometry('830x600')
    f = InfoFrame(master =window, )
    
    f.grid(column = 0, row = 0, sticky  = NSEW)
    
    window.mainloop()
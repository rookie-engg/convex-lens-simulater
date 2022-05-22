from convex_lens_simulater import convex_lens_simulater
import tkinter as tk
import turtle
#
#canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
#draw = turtle.Turtle()
#canvas.pack()

class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.title("")
        self.master = master
        self.pack()
        canvas = tk.Canvas(master = None, width = 800, height = 800)
        self.master.minsize(190,100)
        self.master.maxsize(190,100)
        self.create_widgets()
        
    def create_widgets(self):
        self.simulate = tk.Button(self,fg='blue',bg='white',padx=20,pady=5,)
        self.simulate["text"] = "\nDraw\n"
        self.simulate['command'] = self.simulater
        self.simulate['activeforeground']='white'
        self.simulate['activebackground']='orange'
        self.simulate.pack(side='left')

        self.quit = tk.Button(self,text="\nQUIT\n",fg="white",bg='red',
            activeforeground='red',activebackground='white',
            command=exit,padx=20,pady=5)
            
        self.quit.pack(side='right')
        self.Lcm = tk.Label(text ='units in cm , Use TAB to switch')
        self.Lcm.pack(side='bottom')

        self.Lf = tk.Label(text='Focal Length(f) : ',fg='white',bg='blue')
        self.Lf.pack(side='left')
        self.f = tk.Entry() ; self.f.pack(side='left')
        self.Lh1 = tk.Label(text='  Object Height(h1) : ',fg='white',bg='red')
        self.Lh1.pack(side='left')
        self.h1 = tk.Entry(); self.h1.pack(side='left')
        self.Lu = tk.Label(text='  Object Distance(u) : ',fg='black',bg='yellow')
        self.Lu.pack(side='left')
        self.u = tk.Entry() ; self.u.pack(side = 'left')
        
    def simulater(self):
        convex_lens_simulater(float(self.f.get()),
                              float(self.h1.get()),
                              float(self.u.get()))



root = tk.Tk()
app = App(master=root)
app.mainloop()

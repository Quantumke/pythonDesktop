import tkinter
from tkinter import ttk
from sqlalchemy import *
from sqlalchemy import schema, types, Table, column, String
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
metadata = schema.MetaData()
import psycopg2
from datetime import *
LARGE_FONT= ("Nexa Light", 12)


class GuiInit(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        container= tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for F in (RegisterPage, Home):
            frame=F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(RegisterPage)
    def show_frame(self, count):
        frame=self.frames[count]
        frame.tkraise()
        class RegisterPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.register_gui()
    def register_gui(self):
        self.grid(column=0, row=0, sticky='nsew')
        self.username = ttk.Entry(self, width=5)
        self.username.grid(column=1, row=2)
        self.email = ttk.Entry(self, width=5)
        self.email.grid(column=8, row=2)
        self.password = ttk.Entry(self, width=5)
        self.password.grid(column=3, row=2)
        self.submit_button = ttk.Button(self, text="Register",  command=self.register)
        self.submit_button.grid(column=0, row=3, columnspan=4)
        self.status = ttk.LabelFrame(self, text='Status', height=100)
        self.status.grid(column=0, row=4, columnspan=4, sticky='nesw')

        self.status_label = ttk.Label(self.status, text='',font=LARGE_FONT)
        self.status_label.grid(column=0, row=0)

        ttk.Label(self, text='Login',font=LARGE_FONT).grid(column=0, row=0,  columnspan=4)
        ttk.Label(self, text='Username',font=LARGE_FONT).grid(column=0, row=2, sticky='w')
        ttk.Label(self, text='Password',font=LARGE_FONT).grid(column=2, row=2, sticky='w')
        ttk.Label(self, text='email',font=LARGE_FONT).grid(column=5, row=2, sticky='w')
        ttk.Separator(self, orient='horizontal').grid(column=0, row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

class Home(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(RegiterPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


app=GuiInit()
app.mainloop()

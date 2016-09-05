import tkinter
from tkinter import ttk
from sqlalchemy import *
from sqlalchemy import schema, types, Table, column, String
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
metadata = schema.MetaData()
import psycopg2

LARGE_FONT= ("Verdana", 12)

class GuiInit(tkinter.Tk):

    def __init__(self, *args, **kwargs):

        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)
          def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        self.login_gui()
    def login_gui(self):
        # self.root.title('WELCOME')
        self.grid(column=0, row=0, sticky='nsew')
        self.username = ttk.Entry(self, width=5)
        self.username.grid(column=1, row=2)
        self.password = ttk.Entry(self, width=5)
        self.password.grid(column=3, row=2)
        self.submit_button = ttk.Button(self, text='Login', command=self.login)
        self.submit_button.grid(column=0, row=3, columnspan=4)
        self.status = ttk.LabelFrame(self, text='Status',
									 height=100)
        self.status.grid(column=0, row=4, columnspan=4, sticky='nesw')

        self.status_label = ttk.Label(self.status, text='')
        self.status_label.grid(column=0, row=0)

        ttk.Label(self, text='Login').grid(column=0, row=0,
										   columnspan=4)
        ttk.Label(self, text='Username').grid(column=0, row=2,
											  sticky='w')
        ttk.Label(self, text='Password').grid(column=2, row=2,
											  sticky='w')

        ttk.Separator(self, orient='horizontal').grid(column=0,
													  row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

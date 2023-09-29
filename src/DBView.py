import customtkinter as ctk
import mysql.connector as mysql

class DBViewWindow(ctk.CTk):
    def __init__(self, cnx, db):
        super().__init__()
        # self.connection = cnx
        # self.connection = mysql.connect()

    def mainloop(self, *args, **kwargs):
        return super().mainloop(*args, **kwargs)
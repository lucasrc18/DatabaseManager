import mysql.connector as mysql
import customtkinter as ctk

from tkinter import messagebox as msgbox
from DBView import DBViewWindow
from DBConnectWindow import DBConnectWindow

class Main:
    def __init__(self):
        self.connection = None
        
        self.main = DBViewWindow()
        self.connectionScreen = DBConnectWindow(master=self.main, handler=self)
        
        self.main.mainloop()

    def createConnection(self, config: dict, db):
        try: 
            self.connection = mysql.connect(**config)
        except mysql.Error as e:
            msgbox.showinfo("Fim de execução do programa", f"Falha ao conectar com banco de dados.\nErro: ({e.errno})")
            quit()
        
        if self.connection != None:        
            cur = self.connection.cursor()
            
            cur.execute(f'CREATE DATABASE IF NOT EXISTS {db};')
            self.connection.database = db
            
            self.main.showConnection(self.connection, db)

app = Main()
import mysql.connector as mysql
import customtkinter as ctk
import tkinter

from tkinter import messagebox as msgbox
from DBView import DBViewWindow
from DBConnectWindow import DBConnectWindow

class Main:
    def __init__(self):
        self.connection = None
        
        self.home = DBViewWindow(cnx="", db="Teste")
        self.connectionScreen = DBConnectWindow(master=self.home, handler=self)
        
        self.home.mainloop()

    def createConnection(self, config: dict):
        try: 
            self.connection = mysql.connect(**config)
        except mysql.Error as e:
            msgbox.showinfo("Fim de execução do programa", f"Falha ao conectar com banco de dados.\nErro: ({e.errno})")
            quit()
        
        if self.connection != None:
            print(self.connection)
            diag = ctk.CTkInputDialog(text="Digite o nome do banco de dados: ", title="Conectar ao Banco de Dados")
            db = diag.get_input()
            
            if db == None:
                msgbox.showinfo("Fim de execução do programa", "Nenhum banco de dados foi especificado.")
                quit()
            
            cur = self.connection.cursor()
            
            cur.execute(f'CREATE DATABASE IF NOT EXISTS {db};')
            cur.execute(f'USE {db}')
            
            self.window = DBViewWindow(cnx=self.connection, db=db)

app = Main()
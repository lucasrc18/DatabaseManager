import mysql.connector as mysql
import customtkinter as ctk
from os import system

system("cls || clear")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

cnx = None

def createConnection():
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'port': '3306',
    }
    
    try:
        return mysql.connect(**config)
    except mysql.Error as error:
        print("Erro ao tentar conectar com o banco de dados!")
        
        print(f"\n\nCódigo do erro: \n{error.errno}")
        quit()

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MariaDB  -  127.0.0.1:3306")
        self.geometry("800x600", )
        self.db = None

    def loadDB_screen(self, cnx):
        diag = ctk.CTkInputDialog(text="Digite o nome do banco de dados: ", title="Conectar ao Banco de Dados")
        self.db = diag.get_input()
        
        if self.db == None:
            self.destroy()
            system("msg * Fim de execução do programa, nenhum banco de dados foi especificado.")
            quit()
        
        useDatabase(cnx, self.db)
        self.title(f"MariaDB  -  127.0.0.1:3306 - [{self.db}]")
        return cnx

    def main_screen(self):
        self.label = ctk.CTkLabel(master=self, text=f"Banco de Dados: {self.db}", text_font=("Arial", 20))
        

    def mainloop(self, *args, **kwargs):
        return super().mainloop(*args, **kwargs)

def useDatabase(cnx, db):
    cur = cnx.cursor()
    cur.execute(f'CREATE DATABASE IF NOT EXISTS {db};')
    cur.execute(f'USE {db}')

app = Window()
cnx = app.loadDB_screen(cnx=createConnection())

if cnx != None:
    print(cnx)
    print("Conexão realizada com sucesso!")
    app.main_screen()


app.mainloop()
cnx.close()
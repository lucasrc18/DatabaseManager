import customtkinter as ctk
import mysql.connector as mysql
from tkinter import messagebox as msgbox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DBConnectWindow(ctk.CTkToplevel):
    def __init__(self, handler, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.handler = handler
        self.title("Set up the database:")
        self.resizable(width=False, height=False)
        
        # Host
        self.host_label = ctk.CTkLabel(master=self, text="Host: ")
        self.host_label.grid(row=0, column=0, padx=10, pady=10)
        self.host_input = ctk.CTkEntry(master=self, placeholder_text="127.0.0.1")
        self.host_input.grid(row=0, column=1, padx=2, pady=2)
        
        # Port
        self.port_label = ctk.CTkLabel(master=self, text="Port: ")
        self.port_label.grid(row=1, column=0, padx=10, pady=10)
        self.port_input = ctk.CTkEntry(master=self, placeholder_text="3306")
        self.port_input.grid(row=1, column=1, padx=2, pady=2)
        
        # User
        self.user_label = ctk.CTkLabel(master=self, text="User: ")
        self.user_label.grid(row=2, column=0, padx=10, pady=10)
        self.user_input = ctk.CTkEntry(master=self, placeholder_text="admin")
        self.user_input.grid(row=2, column=1, padx=2, pady=2)
        
        # Password
        self.password_label = ctk.CTkLabel(master=self, text="Password: ")
        self.password_label.grid(row=3, column=0, padx=10, pady=10)
        self.password_input = ctk.CTkEntry(master=self, placeholder_text="", show="*")
        self.password_input.grid(row=3, column=1, padx=2, pady=2)
        
        # Database
        self.database_label = ctk.CTkLabel(master=self, text="Banco de dados: ")
        self.database_label.grid(row=4, column=0, padx=10, pady=10)
        self.database_input = ctk.CTkEntry(master=self, placeholder_text="")
        self.database_input.grid(row=4, column=1, padx=2, pady=2)        
        
        # Connect
        self.connect_button = ctk.CTkButton(master=self, text="Connect", command=self.getConnectionData)
        self.connect_button.grid(row=5, column=1, padx=10, pady=10)

    def getConnectionData(self):
        host = self.host_input.get().strip() if self.host_input.get() != "" else "127.0.0.1"
        port = self.port_input.get().strip() if self.port_input.get() != "" else "3306"
        user = self.user_input.get().strip() if self.user_input.get() != "" else "root"
        passwd = self.password_input.get().strip()
        database = self.database_input.get().strip()
        
        if database == "":
            msgbox.showinfo("Fim de execução do programa", "Nenhum banco de dados foi especificado.")
            quit()
        
        config = {
            "host": host,
            "port": port,
            "user": user,
            "password": passwd
        }
        
        self.handler.createConnection(config, database)
        self.destroy()
import customtkinter as ctk
import mysql.connector as mysql

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DBConnectWindow(ctk.CTk):
    def __init__(self, handler):
        super().__init__()
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
        
        # Connect
        self.connect_button = ctk.CTkButton(master=self, text="Connect", command=self.getConnectionData)
        self.connect_button.grid(row=4, column=1, padx=10, pady=10)

    def getConnectionData(self):
        host = self.host_input.get().strip() if self.host_input.get() != "" else "127.0.0.1"
        port = self.port_input.get().strip() if self.port_input.get() != "" else "3306"
        user = self.user_input.get().strip() if self.user_input.get() != "" else "root"
        passwd = self.password_input.get().strip()
        
        config = {
            "host": host,
            "port": port,
            "user": user,
            "password": passwd
        }
        
        self.handler.createConnection(config)
        print(config)
    def mainloop(self, *args, **kwargs):
        return super().mainloop(*args, **kwargs)
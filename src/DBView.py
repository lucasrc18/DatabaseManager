import customtkinter as ctk

class DBViewWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)
        
        # ! Left space
        ctk.CTkFrame(master=self).grid(row=0, column=0, padx=0, pady=0, sticky="wn")
        
        self.data_frame = ctk.CTkFrame(master=self)

        
        # ! Right space
        ctk.CTkFrame(master=self).grid(row=0, column=3, padx=0, pady=0, sticky="ne")
    def showConnection(self, cnx, db):
        self.connection = cnx
        self.db = db
        
        self.cnxLabel['value'].set(f"Conectado ao banco: {db}")
        
        self.geometry("800x600")
        self.title(f"MySQL - {cnx.user}@{cnx.server_host}:{cnx.server_port}")
        
        
        self.sel_table = {
            'value': ctk.StringVar(master=self, value="Esperando conexão..."),	
        }
        self.sel_table['widget'] = ctk.CTkLabel(master=self.table_selection_frame, textvariable=self.sel_table['value'])
        self.sel_table['widget'].grid(row=0, column=0, padx=10, pady=10)

        cur = cnx.cursor(buffered=True)

        cur.execute("SHOW TABLES;")
        table_list = cur.fetchall()
        cur.nextset()
        
        if len(table_list) == 0:
            self.sel_table['value'].set("Nenhuma tabela foi encontrada.")
        else:
            table_list = tuple([t[0] for t in table_list])
            self.sel_table['value'].set(f"Selecione uma tabela:")
            self.table_option = ctk.CTkOptionMenu(master=self.table_selection_frame, values=table_list)
            self.table_option.grid(row=0, column=1)
        

    def mainloop(self, *args, **kwargs):
        return super().mainloop(*args, **kwargs)
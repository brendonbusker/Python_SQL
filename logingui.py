import tkinter as t
import tkinter.messagebox
import pyodbc


class SQL_Login:
    def __init__(self):
        #Main window
        self.main_window = t.Tk()
        self.main_window.geometry("250x125")
        self.main_window.title("SQL Server Login")

        #Frames
        self.enter_login_frame = t.Frame(self.main_window)
        self.password_frame = t.Frame(self.main_window)
        self.login_frame = t.Frame(self.main_window)

        #Login
        self.login_label = t.Label(self.enter_login_frame, text = "Login:       ")
        self.login_entry = t.Entry(self.enter_login_frame, width = 20)
        self.login_label.pack(side = "left")
        self.login_entry.pack(side = "left")

        #Password
        self.pass_label = t.Label(self.password_frame, text = "Password:")
        self.pass_entry = t.Entry(self.password_frame, width = 20, show = "*")
        self.pass_label.pack(side = "left")
        self.pass_entry.pack(side = "left")

        #Login Button
        self.login_button = t.Button(self.login_frame, text = "Login", command = self.access_database, width = 20)
        self.login_button.pack(side = "top")

        #Pack Frames
        self.enter_login_frame.pack()
        self.password_frame.pack()
        self.login_frame.pack()

        #Loop
        t.mainloop()

    #Access Database Command
    def access_database(self):
        login = self.login_entry.get()
        password = self.pass_entry.get()
        
        self.main_window.destroy()
        
        cn_str = (
            
        'Driver={SQL Server Native Client 11.0};' #data source driver
            
        'Server=MIS-SQLJB;' #server name
            
        'Database=School;' #database name
            
        'UID='+login+';'   #username
            
        'PWD='+password+';' #user password
            
        )
        
               
        #connect to server
        
        cn = pyodbc.connect(cn_str)


#Run GUI
SQL_server_login = SQL_Login()
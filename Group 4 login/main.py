import tkinter as tk
from tkinter import ttk
import loginhandler
import gwaframe
import signup
import accountdetails
import forgotpw


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("GWA CALCULATOR")
        self.frames = {}
        self.frames['Log_In'] = loginhandler.LogIn_Page(self)
        self.frames['LSecondWindow'] = loginhandler.LSecondWindow(self)
        self.frames['GwaCalculator'] = gwaframe.GwaCalculator(self)
        self.frames['Signup_Page'] = signup.Signup_Page(self)
        self.frames['ForgotPW'] = forgotpw.ForgotPW(self)
        self.frames['Account_Details'] = accountdetails.AccDetails(self)
        self.change_frame('Log_In')
       
        
    def change_frame(self, name, **kwargs):
        for frame in self.frames.values():
            frame.grid_forget()
            
        self.frames[name].grid()
    
  
root = MainWindow()
root.resizable(False, False)
root.mainloop()

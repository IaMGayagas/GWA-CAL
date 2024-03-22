import tkinter as tk
import time
import tkinter.messagebox as tk_messagebox
import gwaframe
from captcha.image import ImageCaptcha
import signup
import random 
import smtplib
from email.message import EmailMessage
from customtkinter import *
import dbhandler



class ForgotPW(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,)
        self.parent = master
        self.config(height=480, width=380, bg='#313131')
        self.grid()

        #Fields
        self.Title = tk.Label(self, text="Forgot Password", font=('Microsoft YaHei UI Bold', 17), bg='#313131', fg='white',
                                    width=15)
        self.Title.place(x=80, y=30)

        #EMAIL
        self.email_label = tk.Label(self, text="Email: ", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white')
        self.email_label.place(x=38, y=100)

        self.email_entry = tk.Entry(self, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,
                                    width=25)
        self.email_entry.place(x=41, y=130)

        self.entryLine = tk.Label(self, bg='#414141')
        self.entryLine.place(x=41, y=155, width=290, height=3)

        self.confirm_otp = tk.Label(self, text="Verify OTP:", font=('Microsoft YaHei UI Light', 11), bg='#313131',
                                fg='white', width=15)
        self.confirm_otp.place(x=8, y=230)

        self.confirm_otp_entry = tk.Entry(self, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,
                                    width=25)
        self.confirm_otp_entry.config(state='disabled', disabledbackground="#313131")
        self.confirm_otp_entry.place(x=41, y=260)


        self.entryLine = tk.Label(self, bg='#414141')
        self.entryLine.place(x=41, y=285, width=290, height=3)

        #Button

        self.back_button = CTkButton(self, text="Cancel", width=120, bg_color="#313131", fg_color='#CA3E47', border_width=0, height=40, corner_radius=50,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.btnCancel, hover_color='#414141')
        self.back_button.place(x=40, y=400)


        self.sentotp_button = CTkButton(self, text="Send OTP", width=100, bg_color="#313131", fg_color='#414141', border_width=0, height=35, corner_radius=50,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.btnSendOTP, hover_color='#414141')
        self.sentotp_button.place(x=40, y=170)


        self.confirm_button = CTkButton(self, text="Confirm", width=120, bg_color="#313131", fg_color='#CA3E47', border_width=0, height=40, corner_radius=50,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.btnConfirm, hover_color='#414141', state='disabled')
        self.confirm_button.place(x=200, y=400)



    # def Confirm(self):
    #     self.parent.change_frame('Forgot_SecondWindow') ## make a validation of email through the database
    #                                                     ##and if the email is valid make it appear on the second window
       
    def email_exists(self, email):
        db_handler = dbhandler.DbHandler() 
        return db_handler.check_email_exists(email)
        
    def btnSendOTP(self):
                email = self.email_entry.get()
                if not email:
                    tk_messagebox.showerror("Error", "Please enter your email before sending OTP.")
                    return
                if not self.email_exists(email):
                    tk_messagebox.showerror("Error", "Email does not exist. Please enter a valid email.")
                    return
                self.sendOTP = tk_messagebox.showinfo("Sending OTP", "Your OTP was sent via email")
                self.otp = ""
                for i in range(6):
                            self.otp += str(random.randint(0,9))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                    
                mail = "g4testacc@gmail.com"
                password = "loqm xgxb wpwr ieub"
                server.login(mail, password)
                to_mail = self.email_entry.get()

                msg = EmailMessage()
                msg['Subject'] = 'OTP Verification'  
                msg['From'] = mail
                msg['To'] = to_mail
                msg.set_content("Your OTP is: " + self.otp)  

                server.send_message(msg)  
                self.confirm_button.configure(state='normal')
                self.confirm_otp_entry.config(state='normal')

    def btnConfirm(self): 
        input_otp = self.confirm_otp_entry.get()
        if input_otp == self.otp:
            self.otp_confirmation = tk_messagebox.showinfo("Confirmation", "OTP VERIFIED")
            self.Forgot_ThirdWindow()
        else:
            self.otp_error= tk_messagebox.showwarning("Confirmation", "INVALID OTP")
        
    def btnCancel(self):
        confirm_cancel = tk_messagebox.askyesno("Confirmation", "Do you wish to cancel procedure?")
        if not confirm_cancel:
            return

        log_in_frame = self.parent.frames['Log_In']
        log_in_frame.username_entry.delete(0, 'end')
        log_in_frame.password_entry.delete(0, 'end')
        self.parent.change_frame('Log_In')


    def Forgot_ThirdWindow(self):

            self.forgotsecondwindow = tk.Toplevel(self)
            self.forgotsecondwindow.title("Reset Password")
            self.forgotsecondwindow.geometry("380x480")

            self.forgotsecondwindow.grab_set()

            second_window = tk.Frame(self.forgotsecondwindow, bg='#313131')
            second_window.place(x=0, y=0, height=600, width=380)

            #Fields
            self.Title = tk.Label(self.forgotsecondwindow, text="Forgot Password", font=('Microsoft YaHei UI Bold', 17), bg='#313131', fg='white',
                                        width=15)
            self.Title.place(x=80, y=30)


            self.newpassword= tk.Label(self.forgotsecondwindow, text="New Password:", font=('Microsoft YaHei UI Light', 11), bg='#313131',
                                    fg='white', width=15)
            self.newpassword.place(x=26, y=170)

            self.newpassword = tk.Entry(self.forgotsecondwindow, show="*", bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,
                                        width=25)
            self.newpassword.place(x=41, y=200)

            self.entryLine = tk.Label(self.forgotsecondwindow, bg='#414141')
            self.entryLine.place(x=41, y=225, width=290, height=3)

            self.Conf_password = tk.Label(self.forgotsecondwindow, text="Confirm Password", font=('Microsoft YaHei UI Light', 11), bg='#313131',
                                 fg='white',
                                 width=15)
            self.Conf_password.place(x=30, y=310)

            self.Conf_password = tk.Entry(self.forgotsecondwindow, show="*", bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,
                                    width=25)
            self.Conf_password.place(x=41, y=340)

            self.entryLine = tk.Label(self.forgotsecondwindow, bg='#414141')
            self.entryLine.place(x=41, y=365, width=290, height=3)


            self.btnCancel = tk.Button(self.forgotsecondwindow, text="Cancel", width=8, bg="#CA3E47", fg='white', border=0,
                    font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.btnCancel)
            self.btnCancel.place(x=50, y=400)

            self.buttConfirm = tk.Button(self.forgotsecondwindow, text="Confirm", width=8, bg="#CA3E47", fg='white', border=0,
                    font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.buttConfirm)
            self.buttConfirm.place(x=220, y=400)



    def buttConfirm(self): 
        new_password = self.newpassword.get()
        confirm_password = self.Conf_password.get()

        if new_password != confirm_password:
            tk_messagebox.showerror("Error", "Passwords do not match. Try again.")
            return


        db_handler = dbhandler.DbHandler()
        db_handler.update_password(self.email_entry.get(), new_password)

        tk_messagebox.showinfo("Confirmation", "Password has been changed successfully.")

        self.email_entry.delete(0, 'end')
        self.confirm_otp_entry.delete(0, 'end')
        self.newpassword.delete(0, 'end')
        self.Conf_password.delete(0, 'end')

        self.forgotsecondwindow.destroy()
        log_in_frame = self.parent.frames['Log_In']
        log_in_frame.username_entry.delete(0, 'end')
        log_in_frame.password_entry.delete(0, 'end')
        self.parent.change_frame('Log_In')
            
    def btnCancel(self):
            confirm_cancel = tk_messagebox.askyesno("Confirmation", "Do you wish to go back?")
            if not confirm_cancel:
                return
            
            self.email_entry.delete(0, 'end')
            self.confirm_otp_entry.delete(0, 'end')
            self.parent.change_frame('Log_In')

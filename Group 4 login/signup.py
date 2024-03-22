import tkinter as tk
import tkinter.messagebox as tk_messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
from customtkinter import *
from PIL import Image, ImageTk
import random 
import smtplib
from email.message import EmailMessage
import models
import dbhandler



class Signup_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(height=600, width=380, bg='#313131')
        
        # LABELS
        self.Title_label = tk.Label(self, text="Create a New Account", bg='#313131', fg='white',
                                     font=('Microsoft YaHei UI Light', 20, 'bold'))
        self.Title_label.place(x=40, y=10)

        line_label0 = tk.Label(self, bg='#414141')
        line_label0.place(x=70, y=115, width=255, height=3)

        line_label = tk.Label(self, bg='#414141')
        line_label.place(x=70, y=195, width=255, height=3)

        line_label1 = tk.Label(self, bg='#414141')
        line_label1.place(x=70, y=275, width=255, height=3)

        line_label2 = tk.Label(self, bg='#414141')
        line_label2.place(x=70, y=355, width=255, height=3)

        line_label2 = tk.Label(self, bg='#414141')
        line_label2.place(x=70, y=435, width=255, height=3)

        line_label2 = tk.Label(self, bg='#414141')
        line_label2.place(x=70, y=515, width=255, height=3)

        self.username_label = tk.Label(self, text="Username", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.username_label.place(x=35, y=65)

        self.firstname_label = tk.Label(self, text="First Name", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.firstname_label.place(x=35, y=145)

        self.lastname_label = tk.Label(self, text="Last Name", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.lastname_label.place(x=35, y=220)

        self.password_label = tk.Label(self, text="Password", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.password_label.place(x=30, y=375)

        self.passwordconfirmation_label = tk.Label(self, text="Confirm Password", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.passwordconfirmation_label.place(x=60, y=455)

        # ENTRIES
        self.username_entry = tk.Entry(self, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.username_entry.place(x=70, y=90)

        self.firstname_entry = tk.Entry(self, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.firstname_entry.place(x=70, y=170)

        self.lastname_entry = tk.Entry(self, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.lastname_entry.place(x=70, y=250)


        self.password_entry = tk.Entry(self, show="*", bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.password_entry.place(x=70, y=410)

        self.passwordconfirmation_entry = tk.Entry(self, show="*" , bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.passwordconfirmation_entry.place(x=70, y=490)

    # Buttons


        self.cancel_button = CTkButton(self, text="Cancel", width=120, bg_color="#313131", fg_color='#CA3E47', border_width=0,
                                      corner_radius=50, height=40, font=('Microsoft YaHei UI Light', 13, 'bold'), hover_color='#414141', command=self.cancel)
        self.cancel_button.place(x=50, y=545)

        self.proceed_button = CTkButton(self, text="Proceed", width=120, bg_color="#313131", fg_color='#CA3E47', border_width=0, height=40, corner_radius=50,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.proceed_validation, hover_color='#414141')
        self.proceed_button.place(x=210, y=545)

        self.birthdate_label = tk.Label(self, text="Birth Date", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.birthdate_label.place(x=33, y=290)

        self.birthdate_entry = DateEntry(self, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0, width=25)
        self.birthdate_entry.place(x=68, y=320)

        self.current_window = None

    def proceed_validation(self):
        username = self.username_entry.get()
   
   
        db_conn = dbhandler.DbHandler()
        if db_conn.check_username_exists(username):
            tk_messagebox.showerror("Invalid Field", "Username already exists. Please choose another username.")
            return
        # elif db_conn.check_email_exists(email):
        #     tk_messagebox.showerror("Invalid Field", "Email already exists. Please use another email.")
        #     return

        if self.firstname_entry.get() == "":
            tk_messagebox.showerror("Invalid Field","Please input your First Name")
        elif self.username_entry.get() == "":
            tk_messagebox.showerror("Invalid Field","Please input a username")
        elif self.lastname_entry.get() == "":
            tk_messagebox.showerror("Invalid Field","Please input your Last Name")
        elif self.password_entry.get() == "":
                tk_messagebox.showerror("Invalid Field", "Please input a password")
        elif self.passwordconfirmation_entry.get() == "":
                tk_messagebox.showerror("Invalid Field", "Please confirm your password")
        elif self.password_entry.get() != self.passwordconfirmation_entry.get():
                tk_messagebox.showerror("Invalid Field", "Passwords do not match")
        else:
            self.username = self.username_entry.get()
            self.firstname = self.firstname_entry.get()
            self.lastname = self.lastname_entry.get()
            self.password = self.password_entry.get()
            self.birthday = self.birthdate_entry.get_date()
            
            self.SecondWindow()
    

    def cancel(self):
        confirm_cancel = tk_messagebox.askyesno("Confirmation", "Do you want to cancel sign up?")
        if not confirm_cancel:
            return
        log_in_frame = self.parent.frames['Log_In']
        log_in_frame.username_entry.delete(0, 'end')
        log_in_frame.password_entry.delete(0, 'end')
        self.parent.change_frame('Log_In')



    def SecondWindow(self):

        self.second_window = tk.Toplevel(self)
        self.second_window.title("Sign Up")
        self.second_window.geometry("380x600")

        self.second_window.grab_set()

        second_window = tk.Frame(self.second_window, bg='#313131')
        second_window.place(x=0, y=0, height=600, width=380)


        self.Title_label = tk.Label(self.second_window, text="Create a New Account", bg='#313131', fg='white',
                                     font=('Microsoft YaHei UI Light', 20, 'bold'))
        self.Title_label.place(x=40, y=20)

        choose_photo_image = Image.open("iconsa.png").resize((100, 100), Image.LANCZOS)
        choose_photo_image = ImageTk.PhotoImage(choose_photo_image)
        self.choose_photos = CTkButton(self.second_window, text="Choose Photo", image=choose_photo_image, compound="top", font=('Microsoft YaHei UI Light', 13, 'bold'), fg_color="#CA3E47", 
                                       height=150, width=150, corner_radius=30, bg_color="#313131", text_color="#EDEDED", border_width=0, command=self.add_photo, hover_color='#414141')
        self.choose_photos.place(x=110, y=80)


        self.back_button = CTkButton(self.second_window, text="Back", width=120, bg_color="#313131", fg_color='#CA3E47', border_width=0, height=40, corner_radius=50,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.back, hover_color='#414141')
        self.back_button.place(x=50, y=530)

        self.signup_button = CTkButton(self.second_window, text="Sign Up", width=120, bg_color="#313131", fg_color='#CA3E47', border_width=0, height=40, corner_radius=50,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.proceed, hover_color='#414141')
        self.signup_button.place(x=210, y=530)

        self.terms_label = tk.Label(self.second_window, text="By signing up, you are agreeing to our", bg='#313131', fg='white',
                                     font=('Microsoft YaHei UI Light', 8))
        self.terms_label.place(x=25, y=575)

        self.terms_button = tk.Button(self.second_window, text="Terms and Conditions", bg="#313131", fg='#CA3E47', border=0,
                                      font=('Microsoft YaHei UI Light', 8, 'bold'), command=self.termstop)
        self.terms_button.place(x=219, y=574)

        self.capvar=tk.BooleanVar()
        self.captcha = tk.Checkbutton(self.second_window, text='Captcha', bg='#313131', fg='black',variable=self.capvar,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'))
        self.captcha.place(x=140, y=280)

        line_label2 = tk.Label(self.second_window, bg='#414141')
        line_label2.place(x=50, y=390, width=255, height=3)

        self.email_label = tk.Label(self.second_window, text="Enter your email:", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.email_label.place(x=35, y=330)

        self.email_entry = tk.Entry(self.second_window, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.email_entry.place(x=50, y=365)

    def add_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    def proceed(self):

        email = self.email_entry.get()
        db_conn = dbhandler.DbHandler()
        if db_conn.check_email_exists(email):
                    tk_messagebox.showerror("Invalid Field", "Email already exists. Please use another email.")
                    return

        self.btnSendOTP()

        self.otp_window= tk.Toplevel(self)
        self.otp_window.title("Account Verification")
        self.otp_window.geometry("400x500")
        self.bg_frame2 = tk.Frame(self.otp_window, height=500, width=400, bg='#313131')
        self.bg_frame2.place(x=0, y=0)

        self.otp_window.grab_set()

        self.first_label = tk.Label(self.otp_window, text="Please enter the OTP sent to your Email", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white')
        self.first_label.place(x=50, y=50)


        line_label = tk.Label(self.otp_window, bg='#414141')
        line_label.place(x=70, y=150, width=255, height=3)

        self.email_label = tk.Label(self.otp_window, text="Confirm Email:", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.email_label.place(x=45, y=100)

        self.email = tk.Entry(self.otp_window, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.email.place(x=70, y=125)

        self.confirm_button = CTkButton(self.otp_window, text="Confirm", width=120, bg_color="#313131", fg_color='#CA3E47', border_width=0, height=40, corner_radius=50,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.btnConfirm, hover_color='#414141')
        self.confirm_button.place(x=150, y=400)


    def back(self):
        
        self.parent.change_frame('Signup_Page')
    
    def termstop(self):
        self.terms_window = tk.Toplevel(self)
        self.terms_window.title("Terms and Condition")
        self.terms_window.geometry("400x500")

        terms_frame = tk.Frame(self.terms_window, bg='#313131')
        terms_frame.place(x=0, y=0, width=400, height=500)

        

    def btnSendOTP(self):
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

        
    def btnConfirm(self): 
        input_otp = self.email.get()
        if input_otp == self.otp:
            self.otp_confirmation = tk_messagebox.showinfo("OTP VERIFIED", "YOUR ACCOUNT HAS BEEN CREATED")
            self.create_user()
            self.username_entry.delete(0, 'end')
            self.firstname_entry.delete(0, 'end')
            self.lastname_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            self.birthdate_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            self.passwordconfirmation_entry.delete(0, 'end')
            self.otp_window.destroy()
            self.second_window.destroy()
            self.parent.change_frame('Log_In')
            
        else:
            self.otp_error= tk_messagebox.showwarning("Confirmation", "INVALID OTP")

    def create_user(self):
            
            new_user=models.User()

            new_user.firstname = self.firstname
            new_user.lastname = self.lastname
            new_user.username = self.username
            new_user.password = self.password
            new_user.email = self.email_entry.get()

            dbconn = dbhandler.DbHandler()
            dbconn.create_user(new_user)

    # def on_return(self, **kwargs):

    #     self.firstname = kwargs.get("firstname","")
    #     self.lastname = kwargs.get("lastname", "")
    #     self.password = kwargs.get("password", "")
    #     self.birthday = kwargs.get("birthday", "")
    #     self.username = kwargs.get("username", "")

    #     print(self.firstname) 
    #     print(self.lastname) 


        
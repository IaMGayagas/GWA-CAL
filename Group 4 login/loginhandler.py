import tkinter as tk
import tkinter.messagebox as tk_messagebox
import gwaframe 
from captcha.image import ImageCaptcha
import signup
from customtkinter import *
import dbhandler
import string
import random


class LogIn_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(height=550, width=450)
        
        # Background Frame
        self.frame = tk.Frame(self, bg="#313131", height=600, width=500)
        self.frame.place(x=0, y=0)

        # Inside Background Frame
        self.bg_frame1 = tk.Frame(self.frame, bg="#414141", height=500, width=400)
        self.bg_frame1.place(x=25, y=25)
        self.bg_frame = tk.Frame(self.frame, bg="#313131", height=490, width=390)
        self.bg_frame.place(x=30, y=30)

        # Line under entry
        line_label = tk.Label(self.bg_frame, bg='#414141')
        line_label.place(x=70, y=150, width=255, height=3)

        line_label1 = tk.Label(self.bg_frame, bg='#414141')
        line_label1.place(x=70, y=230, width=255, height=3)

        self.App_label = tk.Label(self.bg_frame, text="GWA Calculator", bg='#313131', fg='white',
                                     font=('Microsoft YaHei UI Light', 18, 'bold'))
        self.App_label.place(x=100, y=30)

        self.username_label = tk.Label(self.bg_frame, text="Username", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.username_label.place(x=37, y=100)

        self.password_label = tk.Label(self.bg_frame, text="Password", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=15)
        self.password_label.place(x=35, y=175)

        self.username_entry = tk.Entry(self.bg_frame, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.username_entry.place(x=70, y=125)
  
        self.password_entry = tk.Entry(self.bg_frame, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.password_entry.place(x=70, y=205)
        self.password_entry.config(show="*")

        self.login_button = CTkButton(self.bg_frame, text="Log In", width=230, bg_color="#313131", fg_color='#CA3E47', border_width=0,
                                      corner_radius=50, height=40, font=('Microsoft YaHei UI Light', 13, 'bold'), hover_color='#414141', command=self.login)
        self.login_button.place(x=80, y=340)

        self.signin_label = tk.Label(self.bg_frame, text="Don't have an account?", bg='#313131', fg='white',
                                     font=('Microsoft YaHei UI Light', 8))
        self.signin_label.place(x=100, y=380)

        self.signup_button = tk.Button(self.bg_frame, text="Sign Up", width=6, bg="#313131", fg='#CA3E47', border=0,
                                      font=('Microsoft YaHei UI Light', 8, 'bold'), command=self.signup)
        self.signup_button.place(x=222, y=380)

        self.password_entry.bind('<Return>', lambda event: self.login())

        self.capvar=tk.BooleanVar()
        self.captcha = tk.Checkbutton(self.bg_frame, text='Captcha', bg='#313131', fg='black',variable=self.capvar,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'),command=self.captcha_validation)
        self.captcha.place(x=140, y=280)

        self.forgotpass_button = tk.Button(self.bg_frame, text="Forgot Password?", bg="#313131", fg='white', border=0,
                                      font=('Microsoft YaHei UI Light', 8,'italic'), command=self.forgotpw)
        self.forgotpass_button.place(x=145, y=235)

        self.terms_label = tk.Label(self.bg_frame, text="By signing up, you are agreeing to our", bg='#313131', fg='white',
                                     font=('Microsoft YaHei UI Light', 8))
        self.terms_label.place(x=40, y=800)

        self.terms_button = tk.Button(self.bg_frame, text="Terms and Conditions", bg="#313131", fg='#CA3E47', border=0,
                                      font=('Microsoft YaHei UI Light', 8, 'bold'))
        self.terms_button.place(x=130, y=460)


    def signup(self):
        self.grid_forget()

        signup_frame = self.parent.frames['Signup_Page']
        signup_frame.username_entry.delete(0, 'end')
        signup_frame.birthdate_entry.delete(0, 'end')
        signup_frame.firstname_entry.delete(0, 'end')
        signup_frame.lastname_entry.delete(0, 'end')
        signup_frame.password_entry.delete(0, 'end')
        signup_frame.passwordconfirmation_entry.delete(0, 'end')
        self.parent.change_frame('Signup_Page')

    def captcha_validation(self):
        self.parent.change_frame('LSecondWindow')

    def termsandcondition(self):
        self.grid_forget()
        pass

    def forgotpw(self):
        self.grid_forget()
        self.parent.change_frame('ForgotPW')

    def login(self):
        if not self.validate():
            return
        
        username = self.username_entry.get()
        password = self.password_entry.get()

        dbconn = dbhandler.DbHandler()
        result = dbconn.login_credential(username, password)

        if result:
            tk_messagebox.showinfo("Login Successful", "Welcome!")  
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

            self.grid_forget()
            self.parent.change_frame('GwaCalculator')
        else:
            tk_messagebox.showerror("Login Failed", "Invalid username or password")

    def validate(self):
        if not self.username_entry.get() or not self.password_entry.get():
            tk_messagebox.showerror("Error", "Username and password should not be empty")
            return False
        return True

class LSecondWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(height=600, width=380, bg='#313131')

        self.Title_label = tk.Label(self, text="CAPTCHA VERIFICATION", bg='#313131', fg='white',
                                     font=('Microsoft YaHei UI Light', 20, 'bold'))
        self.Title_label.place(x=40, y=20)


        self.first_label = tk.Label(self, text="Not A Robot? ", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white')
        self.first_label.place(x=50, y=100)

        line_label = tk.Label(self, bg='#414141')
        line_label.place(x=70, y=200, width=255, height=3)

        self.captcha_confirmation = tk.Label(self, text="Verify Captcha below: ", font=('Microsoft YaHei UI Light', 11), bg='#313131', fg='white', width=25)
        self.captcha_confirmation.place(x=45, y=125)

        self.captcha_confirmation = tk.Entry(self, bg="#313131", fg='white', font=('Microsoft YaHei UI Light', 13), border=0,  width=25)
        self.captcha_confirmation.place(x=100, y=175)

        self.canvas = tk.Canvas(self, width=280, height=90)
        self.canvas.place(x=50, y=250)
        self.Image = ImageCaptcha(width=280, height=90)
        self.generate_and_display_captcha()


        self.confirm_button = CTkButton(self, text="Confirm", width=120, bg_color="#313131", fg_color='#CA3E47', border_width=0, height=40, corner_radius=50,
                                      font=('Microsoft YaHei UI Light', 13, 'bold'), command=self.validate_captcha, hover_color='#414141')
        self.confirm_button.place(x=200, y=450)

    def generate_random_text(self, length=8):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    def generate_captcha(self):
        captcha_text = self.generate_random_text()
        captcha_image = self.Image.generate(captcha_text)
        return captcha_text, captcha_image

    def save_captcha(self, captcha_text, captcha_image, filename):
        self.Image.write(captcha_text, filename)


    def generate_and_display_captcha(self):
        self.captcha_text, captcha_image = self.generate_captcha()
        self.save_captcha(self.captcha_text, captcha_image, 'random_captcha.png')
        self.render_captcha_image()

    def render_captcha_image(self):
        photo = tk.PhotoImage(file='random_captcha.png')
        self.captchaimage_label= tk.Label(self, image=photo)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo 

    def validate_captcha(self):
        user_input = self.captcha_confirmation.get().strip()
        if self.captcha_text == user_input:
            tk_messagebox.showinfo("Validation Result", "CAPTCHA validation successful!")
            self.parent.change_frame('Log_In')
            
        else:
            tk_messagebox.showerror("Validation Result", "CAPTCHA validation failed!")
        self.captchaimage_label.destroy()
        self.generate_and_display_captcha()

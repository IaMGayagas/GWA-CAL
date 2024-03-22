import tkinter as tk
import tkinter.messagebox as tk_messagebox
from customtkinter import *
import sqlite3

class AccDetails(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master

        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

        self.configure(height=600, width=1000, bg='#525252')

        #Whole Background
        self.bg_frame = tk.Frame(self, bg='#313131', height=600, width=1000)
        self.bg_frame.place(x=0, y=0)

        #Heading Background
        self.heading_frame = tk.Frame(self.bg_frame, bg='#c93535', height=60, width=1000)
        self.heading_frame.place(x=0, y=0)

        self.name_label = tk.Label(self.heading_frame, text="Name", font=('Microsoft YaHei UI Light', 20, 'bold'), bg='#c93535', fg='white')
        self.name_label.place(x=30, y=10)

        self.back_btn = tk.Button(self.heading_frame, text="Back", bg="#c93535", fg="black", height=2, width=5,command=self.profile_settings)
        self.back_btn.place(x=945, y=10)

        #Underheading, background
        self.acc_detailsbg = tk.Frame(self.bg_frame, bg='#313131', height=600, width=1000)
        self.acc_detailsbg.place(x=0, y=60)

        self.pic_label = tk.Label(self.acc_detailsbg, bg="#afafaf", height=12, width=30)
        self.pic_label.place(x=30, y=20)

        self.email_label = tk.Label(self.acc_detailsbg, text="", bg="#313131", fg="white", font=('Microsoft YaHei UI Light', 14))
        self.email_label.place(x=30, y=210)

        self.acc_detaillbl = tk.Label(self.acc_detailsbg, text="Account Details", font=('Microsoft YaHei UI', 20, 'bold'), bg='#313131', fg='white')
        self.acc_detaillbl.place(x=450, y=50)

        #Labels
        self.fname_label = tk.Label(self.acc_detailsbg, text="First Name:", bg="#313131", fg="white", font=('Microsoft YaHei UI Light', 14))
        self.fname_label.place(x=353, y=143)

        self.lname_label = tk.Label(self.acc_detailsbg, text="Last Name:", bg="#313131", fg="white", font=('Microsoft YaHei UI Light', 14))
        self.lname_label.place(x=353, y=193)

        self.username_label = tk.Label(self.acc_detailsbg, text="Username:", bg="#313131", fg="white", font=('Microsoft YaHei UI Light', 14))
        self.username_label.place(x=353, y=243)

        self.pass_label = tk.Label(self.acc_detailsbg, text="Password:", bg="#313131", fg="white", font=('Microsoft YaHei UI Light', 14))
        self.pass_label.place(x=353, y=293)

        self.bday_label = tk.Label(self.acc_detailsbg, text="Birthdate:", bg="#313131", fg="white", font=('Microsoft YaHei UI Light', 14))
        self.bday_label.place(x=353, y=343)


        #Entries
        self.fname_entry = CTkEntry(self.acc_detailsbg, font=('Monsterrat', 30), width=400, corner_radius=30, fg_color="#d9d9d9", border_color="#313131",text_color="black")
        self.fname_entry.place(x=470, y=140)

        self.lname_entry = CTkEntry(self.acc_detailsbg, font=('Monsterrat', 30), width=400, corner_radius=30, fg_color="#d9d9d9", border_color="#313131",text_color="black")
        self.lname_entry.place(x=470, y=190)
        
        self.username_entry = CTkEntry(self.acc_detailsbg, font=('Monsterrat', 30), width=400, corner_radius=30, fg_color="#d9d9d9", border_color="#313131",text_color="black")
        self.username_entry.place(x=470, y=240)

        self.pass_entry = CTkEntry(self.acc_detailsbg, font=('Monsterrat', 30), width=400, corner_radius=30, fg_color="#d9d9d9", border_color="#313131",text_color="black")
        self.pass_entry.place(x=470, y=290)

        self.bday_entry = CTkEntry(self.acc_detailsbg, font=('Monsterrat', 30), width=400, corner_radius=30, fg_color="#d9d9d9", border_color="#313131",text_color="black")
        self.bday_entry.place(x=470, y=340)

        self.view_button = CTkButton(self.acc_detailsbg, text="View History", font=('Microsoft YaHei UI Light', 20, 'bold'), fg_color="#c93535", 
                                      corner_radius=30, width=40)
        self.view_button.place(x=50, y=460)

        self.edit_button = CTkButton(self.acc_detailsbg, text="Edit", font=('Microsoft YaHei UI Light', 20, 'bold'), fg_color="#c93535", 
                                      corner_radius=30, width=40)
        self.edit_button.place(x=810, y=460)

    def profile_settings(self):
        self.cursor.close()
        self.conn.close()

        self.parent.change_frame('GwaCalculator')
   


    def fetch_user_details(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.cursor.fetchone()

        # If user exists, populate the entry fields with user details
        if user:
            self.fname_entry.insert(0, user[1])  
            self.lname_entry.insert(0, user[2])  
            self.username_entry.insert(0, user[3])   
            self.pass_entry.insert(0, user[4])  
            self.email_label.config(text=user[5])
        else:
            tk_messagebox.showinfo("Error", "User not found")

 
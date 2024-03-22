import tkinter as tk
import tkinter.messagebox as tk_messagebox
from customtkinter import *


#change the eligibility code regarding the individual grading validation of having 2.0 

class GwaCalculator(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master

        self.configure(height=620, width=1000, bg='#525252')

        self.fixedsys_font = (('Microsoft YaHei UI Light', 13))

        #Whole Background
        self.bg_frame = tk.Frame(self, bg='#313131', height=620, width=1000)
        self.bg_frame.place(x=0, y=0)

        #Heading Background
        self.heading_frame = tk.Frame(self.bg_frame, bg='#c93535', height=60, width=1000)
        self.heading_frame.place(x=0, y=0)

        self.name_label = tk.Label(self.heading_frame, text="Name", font=('Microsoft YaHei UI Light', 20, 'bold'), bg='#c93535', fg='white')
        self.name_label.place(x=30, y=10)

        self.profile_btn = tk.Button(self.heading_frame, text="Profile", bg="#c93535", fg="black", height=2, width=5,command=self.profile_settings)
        self.profile_btn.place(x=900, y=10)

        self.profile_btn = tk.Button(self.heading_frame, text="Logout", bg="#c93535", fg="black", height=2, width=5,command=self.logout)
        self.profile_btn.place(x=945, y=10)

        #Underheading, background
        self.gwa_background = tk.Frame(self.bg_frame, bg='#313131', height=620, width=1000)
        self.gwa_background.place(x=0, y=60)

        self.title_frame = CTkLabel(self.gwa_background, fg_color="#d9d9d9", 
                                     text_color="black", corner_radius=30, height=50, width=500)
        self.title_frame.place(x=45, y=40)

        self.underline = CTkLabel(self.title_frame , fg_color="#d9d9d9", text="____________________________", height=1, width=5, corner_radius=5)
        self.underline.place(x=165, y=28)

        self.subjects_label = tk.Label(self.title_frame, text='Number of Subjects:', font=('Microsoft YaHei UI Light', 12), bg="#d9d9d9", fg="black")
        self.subjects_label.place(x=10, y=11)
        self.subjects_entry = tk.Entry(self.title_frame, bg='#d9d9d9', bd=0,font=('Microsoft YaHei UI Light', 11), justify='center', fg="black")
        self.subjects_entry.place(x=170, y=15)
        self.create_fields_button = CTkButton(self.title_frame, text="Create Fields", font=('Microsoft YaHei UI Light', 13, 'bold'), fg_color="#c93535", 
                                      corner_radius=30, command=self.create_input_fields)
        self.create_fields_button.place(x=345, y=11)

        self.units_label = tk.Label(self.bg_frame, text="Units", bg="#313131", fg="white")
        self.grades_label = tk.Label(self.bg_frame, text="Grades", bg="#313131", fg="white")
        self.subjects_name_label = tk.Label(self.bg_frame, text="Subject Name", bg="#313131", fg="white")

        self.calculate_button = CTkButton(self.gwa_background, text="Calculate", font=('Microsoft YaHei UI Light', 18, 'bold'), fg_color="#c93535", 
                                      corner_radius=30, width=30, command=self.calculate_gwa)
        self.calculate_button.place(x=786, y=53)

        self.reset_button = CTkButton(self.gwa_background, text="Clear", font=('Microsoft YaHei UI Light', 18, 'bold'), fg_color="#c93535", 
                                      corner_radius=30, width=40, command=self.clear_result)
        self.reset_button.place(x=910, y=53)

        self.add_button = CTkButton(self.gwa_background, text="Add", font=('Microsoft YaHei UI Light', 18, 'bold'), fg_color="#c93535", 
                                      corner_radius=30, width=40, command=self.add_button)
        self.add_button.place(x=899, y=420)

        self.save_button = CTkButton(self.gwa_background, text="Save", font=('Microsoft YaHei UI Light', 18, 'bold'), fg_color="#c93535", 
                                      corner_radius=30, width=40)
        self.save_button.place(x=898, y=460)

        self.delete_button = CTkButton(self.gwa_background, text="Delete", font=('Microsoft YaHei UI Light', 18, 'bold'), fg_color="#c93535", 
                                      corner_radius=30, width=40, command=self.delete_button)
        self.delete_button.place(x=890, y=500)

        self.gwa_label = tk.Label(self.gwa_background, text="", font=("Georgia", 20), bg="#313131", fg="white")
        self.gwa_label.place(x=365, y=120)

        options = ["Highest Point System", "One (1) as the Highest", "Four (4) as the Highest","Five (5) as the Highest"]
        self.selected_option = tk.StringVar(self)
        self.selected_option.set("Highest Point System") 
        
        self.dropdown = tk.OptionMenu(self.gwa_background, self.selected_option, *options)
        self.dropdown.configure(bg="#414141", fg="white", borderwidth=0, font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.dropdown.place(x=570, y=50)
        
        self.units_entries = []
        self.grades_entries = []
        self.subject_number_labels = [] 
        self.subjects_name_entries = []
        self.result_labels = []

    def profile_settings(self):
        self.parent.change_frame('Account_Details')
    
    def logout(self):
        tk_messagebox.askyesno('Confirmation','Do you want to log out this session? ')
        self.clear_result()
        
        gwa_frame = self.parent.frames['GwaCalculator']
        gwa_frame.subjects_entry.delete(0, tk.END)
        gwa_frame.subjects_label.config(text="")
        self.parent.change_frame('Log_In')
        

    def create_input_fields(self):
        if not all(entry.get() != "" and entry.get() is not None for entry in self.subjects_name_entries):
            confirm_reset = tk_messagebox.askyesno("Confirmation", "Do you want to reset your current computation?")
            if not confirm_reset:
                return

        for entry in self.units_entries + self.grades_entries + self.subjects_name_entries:
            entry.destroy()
        self.units_entries.clear()
        self.grades_entries.clear()
        self.subjects_name_entries.clear()

        for label in self.subject_number_labels:
            label.destroy()
        self.subject_number_labels.clear()

        self.subjects_name_label.place_forget()
        self.units_label.place_forget()
        self.grades_label.place_forget()

        try:
            num_subjects = int(self.subjects_entry.get())
            if num_subjects > 12:
                tk_messagebox.showwarning("Warning", "Number of subjects cannot exceed 12")
                return
            
            for i in range(num_subjects):
                subject_number_label = tk.Label(self.bg_frame, text=f"Subject {i + 1}", font=self.fixedsys_font, bg="#313131", fg="white")
                subject_number_label.place(x=100, y=255 + i * 30)
                self.subject_number_labels.append(subject_number_label)

                subjects_name_entry = tk.Entry(self.bg_frame, bg='#525252', font=self.fixedsys_font, justify='center', fg="white")
                subjects_name_entry.place(x=208, y=255 +i*30)
                self.subjects_name_entries.append(subjects_name_entry) 

                units_entry = tk.Entry(self.bg_frame, bg='#525252', font=self.fixedsys_font, justify='center', fg="white")
                units_entry.place(x=408, y=255 + i * 30)
                self.units_entries.append(units_entry)
                units_entry.configure(validate="key", validatecommand=(self.register(self.validate_integer), "%P"))

                grades_entry = tk.Entry(self.bg_frame, bg='#525252', font=self.fixedsys_font, justify='center', fg="white")
                grades_entry.place(x=608, y=255 + i * 30)
                self.grades_entries.append(grades_entry)
                grades_entry.configure(validate="key", validatecommand=(self.register(self.validate_decimal), "%P"))

            self.subjects_name_label.place(x=260, y=210)
            self.units_label.place(x=490, y=210)
            self.grades_label.place(x=685, y=210)

        except ValueError:
            pass
        except tk.TclError:
            pass
        finally:
            self.subjects_entry.delete(0, tk.END)
            self.subjects_entry.focus_set()

    def calculate_gwa(self):
        try:
            if self.selected_option.get() == "Highest Point System":
                tk_messagebox.showinfo("Choose Grading System", "Please choose between the other two grading systems.")
                return

            units = [float(entry.get()) for entry in self.units_entries]
            grades = [float(entry.get()) for entry in self.grades_entries]

            weighted_sum = sum(grade * unit for grade, unit in zip(grades, units))
            total_units = sum(units)
            gwa = weighted_sum / total_units

            for label in self.result_labels:
                label.destroy()
            self.result_labels.clear()

            result_message = ""

            selected_option = self.selected_option.get()

            if selected_option == "One (1) as the Highest":
                if 1.0 <= gwa <= 1.25:
                    result_message = "Qualified for President's Lister"
                elif 1.26 < gwa <= 1.50:
                    result_message = "Qualified for Dean's Lister"
                else:
                    result_message = "No lister qualification"
            elif selected_option == "Five (5) as the Highest":
                if 4.75 <= gwa <= 5.00:
                    result_message = "Qualified for President's Lister"
                elif 4.50 < gwa <= 4.74:
                    result_message = "Qualified for Dean's Lister"
                else:
                    result_message = "No lister qualification"
            elif selected_option == "Four (4) as the Highest":
                if 3.75 <= gwa <= 4.00:
                    result_message = "Qualified for President's Lister"
                elif 3.50 < gwa <= 3.74:
                    result_message = "Qualified for Dean's Lister"
                else:
                    result_message = "No lister qualification"
            

            result_label = tk.Label(self.bg_frame, text=f"Your GWA is: {gwa:.4f}\n{result_message}", font=("Georgia", 18), bg="#313131", fg="white")
            result_label.place(x=380, y=165)

            self.result_labels.append(result_label)

        except ValueError:
            pass

    def clear_result(self):
        confirm_clear = tk_messagebox.askyesno("Confirmation", "Do you want to clear all inputted data?")
        if not confirm_clear:
            return
        for label in self.result_labels:
            label.destroy()
        self.result_labels.clear()

        for entry in self.units_entries:
            entry.delete(0, tk.END)

        for entry in self.grades_entries:
            entry.delete(0, tk.END)

        for entry in self.subjects_name_entries:
            entry.delete(0, tk.END)

    def validate_integer(self, value):
        if value == "" or (value.isdigit() and len(value) <= 1):
            return True
        else:
            return False

    def validate_decimal(self, value):
        if value == "":
            return True

        if self.selected_option.get() == "Four (4) as the Highest":
            try:
                float_value = float(value)
                if len(value.split(".")[-1]) <= 4 and 1 <= float_value <= 4:
                    return True
                else:
                    return False
            except ValueError:
                return False
        else:
            try:
                float_value = float(value)
                if len(value.split(".")[-1]) <= 4 and 1 <= float_value <= 5:
                    return True
                else:
                    return False
            except ValueError:
                return False

    def add_button(self):
        if len(self.units_entries) >= 12:
            tk_messagebox.showwarning("Warning", "You have reached the maximum number of subjects (12).")
            return
        
        num_entries = len(self.units_entries)
        y_coordinate = 255 + num_entries * 30

        subject_number_label = tk.Label(self.bg_frame, text=f"Subject {num_entries + 1}", font=self.fixedsys_font, bg="#313131", fg="white")
        subject_number_label.place(x=100, y=y_coordinate)
        self.subject_number_labels.append(subject_number_label)

        subject_name_entry = tk.Entry(self.bg_frame, bg='#525252', font=self.fixedsys_font, justify='center', fg="white")
        subject_name_entry.place(x=208, y=y_coordinate)
        self.subjects_name_entries.append(subject_name_entry)  

        unit_entry = tk.Entry(self.bg_frame, bg='#525252', font=self.fixedsys_font, justify='center', fg="white")
        unit_entry.place(x=408, y=y_coordinate)
        self.units_entries.append(unit_entry)
        unit_entry.configure(validate="key", validatecommand=(self.register(self.validate_integer), "%P"))

        grade_entry = tk.Entry(self.bg_frame, bg='#525252', font=self.fixedsys_font, justify='center', fg="white")
        grade_entry.place(x=608, y=y_coordinate)
        self.grades_entries.append(grade_entry)
        grade_entry.configure(validate="key", validatecommand=(self.register(self.validate_decimal), "%P"))

        self.units_label.place_forget()
        self.grades_label.place_forget()
        self.subjects_name_label.place_forget()
        
        self.subjects_name_label.place(x=260, y=210)
        self.units_label.place(x=490, y=210)
        self.grades_label.place(x=685, y=210)

        self.add_button.configure(state=tk.NORMAL)

    def delete_button(self):
        if len(self.units_entries) > 0:
            last_units_entry = self.units_entries.pop()
            last_units_entry.destroy()

        if len(self.grades_entries) > 0:
            last_grades_entry = self.grades_entries.pop()
            last_grades_entry.destroy()

        if len(self.subject_number_labels) > 0:
            last_subject_number_label = self.subject_number_labels.pop()
            last_subject_number_label.destroy()

        if len(self.subjects_name_entries) > 0:
            last_subjects_name_entry = self.subjects_name_entries.pop()
            last_subjects_name_entry.destroy()

        if len(self.units_entries) < 12:
            self.add_button.configure(state=tk.NORMAL)
        else:
            self.delete_button.configure(state=tk.DISABLED)
            tk_messagebox.showwarning("Warning", "No subjects anymore to delete")
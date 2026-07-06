from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_password():
    password:str = password_generator.generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 :
        messagebox.showwarning(title="Missing entries", message="Please fill all the entry boxes!")
        return

    is_ok = messagebox.askokcancel(title="Password added", message=f'''Confirm the details entered:
    
Website: {website}

Username: {user}

Password: {password}

Is it ok to save?
    ''')

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {user} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
img_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

user_label = Label(text="Username")
user_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row= 1, column= 1, columnspan= 2)
website_entry.focus()

user_entry = Entry(width= 35)
user_entry.grid(row= 2, column= 1, columnspan= 2)
user_entry.insert(0, "name1.name2@gmail.com")

password_entry = Entry(width= 21)
password_entry.grid(row= 3, column= 1)

# Buttons
generate_password_button = Button(width= 14, text="Generate Password", command=create_password)
generate_password_button.grid(row=3, column= 2)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(row=4, column= 1, columnspan= 2)

window.mainloop()
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for num in range(randint(8, 10))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]
    password_symbols = [choice(symbols) for num in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    user = email_entry.get()
    password = password_entry.get()
    new_data_dict = {
        website: {
            "user": user,
            "password": password,
        }
    }

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        length_warning = messagebox.showwarning(title="bruh", message="You can't be leaving fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You have entered the following details:"
                                                              f" \nUsername: {user} \nPassword: {password} \nContinue?")
        if is_ok:
            try:
                with open("PMdata.json", "r") as pass_data:
                    # Read old data file
                    jason_data = json.load(pass_data)
            except FileNotFoundError:
                with open("PMdata.json", "w") as pass_data:
                    json.dump(new_data_dict, pass_data, indent=4)
            else:
                # Update data file with new data
                jason_data.update(new_data_dict)

                with open("PMdata.json", "w") as pass_data:
                    # Write the updated datafile over old data file
                    json.dump(jason_data, pass_data, indent=4)
            finally:
                    website_entry.delete(0, END)
                    website_entry.focus()
                    email_entry.delete(0, END)
                    email_entry.insert(0, "email@tylerhardwick.co.uk")
                    password_entry.delete(0, END)

# ---------------------------- Search ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("PMdata.json", "r") as pm_data:
            data = json.load(pm_data)
    except FileNotFoundError:
        messagebox.showerror(title="No Data File found", message="Cannot find any saved websites.")
    else:
        if website in data:
            email = data[website]["user"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {email} \nPassword: {password}")
        else:
            messagebox.showerror(title=f"{website} not found", message=f"Cannot find {website} in your password directory.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(height=200, width=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")


# Entries
website_entry = Entry(width=44)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "email@tylerhardwick.co.uk")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="w")


# Buttons
gen_pass_button = Button(text="Generate Password", command=gen_pass)
gen_pass_button.grid(row=3, column=2, sticky="e")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="e")

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=5, column=1, columnspan=2)




window.mainloop()


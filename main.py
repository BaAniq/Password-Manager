from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# ---------------------_GENERATE A PASSWORD_---------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_numbers = randint(2, 4)
nr_symbols = randint(2, 4)

password_letters = [choice(letters) for x in range(nr_letters)]
password_numbers = [choice(numbers) for x in range(nr_numbers)]
password_symbols = [choice(symbols) for x in range(nr_symbols)]

password_list = password_letters+password_numbers+password_symbols

shuffle(password_list)

generated_password = ''.join(password_list)


def generate_password(password=generated_password):
    password_entry.insert(END, password)
# ---------------------_ADDING USER'S PASSWORD TO THE FILE_---------------------
def add_password():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_ = password_entry.get()
    if len(website_name) == 0 or len(email_name) == 0 or password_ == 0:
        messagebox.showinfo(title='Empty fields', message="Please don't leave any fields empty")
    else:
        do_save = messagebox.askokcancel(title='Data to save', message=f'Do you want to save this data: \nWebsite:'
                                                                       f' {website_name}\nEmail: {email_name}\n'
                                                                       f'Password: {password_}')
        if do_save:
            with open('Data.txt', 'a+') as data_storage:
                data_storage.write(f'{website_name} | {email_name} | {password_}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        else:
            messagebox.showinfo(title='Info', message='Please correct your data before saving it')

# ---------------------_CREATING A WINDOW_---------------------
window = Tk()
window.config(padx=50, pady=50)
window.title('Your password manager')

set_background_image = Canvas(width=200, height=200)
image_logo = PhotoImage(file='logo.png')
set_background_image.create_image(100, 100, image=image_logo)
set_background_image.grid(row=1, column=2)

website_label = Label(text='Website:')
website_label.grid(row=2, column=1)


email_label = Label(text='Email/Username:')
email_label.grid(row=3, column=1)

password_label = Label(text='Password:')
password_label.grid(row=4, column=1)

website_entry = Entry(width=46)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()

email_entry = Entry(width=46)
email_entry.grid(row=3, column=2, columnspan=2)
email_entry.insert(END, string='basia@gmail.com')

password_entry = Entry(width=28)
password_entry.grid(row=4, column=2)

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=4, column=3)

add_button = Button(text='Add', width=46, command=add_password)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()

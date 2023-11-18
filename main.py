from tkinter import *


def add_password():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_ = password_entry.get()
    with open('Data.txt', 'a+') as data_storage:
        data_storage.write(f'{website_name} | {email_name} | {password_}\n')
    website_entry.delete(0, END)
    password_entry.delete(0, END)


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

generate_password_button = Button(text='Generate Password')
generate_password_button.grid(row=4, column=3)

add_button = Button(text='Add', width=46, command=add_password)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()

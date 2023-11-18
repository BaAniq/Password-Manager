from tkinter import *

window = Tk()
window.config(padx=50, pady=50)
window.title('Your password manager')
# window.minsize(height=300, width=500)

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

password_entry = Entry(width=28)
password_entry.grid(row=4, column=2)

generate_password_button = Button(text='Generate Password')
generate_password_button.grid(row=4, column=3)

add_button = Button(text='Add', width=46)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()

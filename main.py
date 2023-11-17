from tkinter import *

window = Tk()
window.config(padx=50, pady=50)
window.title('Your password manager')
window.minsize(height=300, width=500)

set_background_image = Canvas(width=200, height=189, highlightthickness=0)
image_logo = PhotoImage(file='logo.png')
set_background_image.create_image(100, 95, image=image_logo)
set_background_image.grid(row=1, column=2)

website_label = Label(text='Website:', font=('Arial', 10), fg='black')
website_label.grid(row=2, column=1)

email_label = Label(text='Email/Username:', font=('Arial', 10), fg='black')
email_label.grid(row=3, column=1)

password_label = Label(text='Password:', font=('Arial', 10), fg='black')
password_label.grid(row=4, column=1)

website_textbox = Entry(width=30)
website_textbox.grid(row=2, column=2)

email_textbox = Entry(width=30)
email_textbox.grid(row=3, column=2)

password_textbox = Entry(width=30)
password_textbox.grid(row=4, column=2)

generate_password_button = Button(text='Generate Password')
generate_password_button.grid(row=4, column=3)

add_button = Button(text='Add')
add_button.grid(row=5, column=2)

window.mainloop()

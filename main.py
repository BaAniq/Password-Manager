from tkinter import *

window = Tk()
window.config(padx=50, pady=50)
window.title('Your password manager')
window.minsize(height=300, width=500)

set_background_image = Canvas(width=200, height=189, highlightthickness=0)
image_logo = PhotoImage(file='logo.png')
set_background_image.create_image(100, 95, image=image_logo)
set_background_image.grid(row=1, column=2)

window.mainloop()
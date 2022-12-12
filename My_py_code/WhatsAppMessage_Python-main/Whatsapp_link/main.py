#import packages
import tkinter
import tkinter as tk
import webbrowser

root = tk.Tk()
root.geometry("300x200")


enter_var = tk.StringVar()

def submit():
    number = enter_var.get()
    url = f"https://wa.me/91{number}"
    new = 1
    #print("The number is : " + number)
    webbrowser.open(url, new=new)
    enter_var.set("")

def endProgam():
    # top.quit()
    root.destroy()

name_label = tk.Label(root, text='Phone Number :', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=enter_var, font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
# Button that will call the endprogam function
sub_btn = tk.Button(root, text='Submit', command=submit)
ext_btn = tk.Button(root , text = "exit", command = endProgam)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
sub_btn.grid(row=2, column=1)
ext_btn.grid(row=3, column=1)

# performing an infinite loop
# for the window to display
#while True:
root.mainloop()


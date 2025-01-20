from tkinter import *
from random import sample
from tkinter import messagebox

lis = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_"

def display():
    try:
        
        character = int(entry.get())  # Get the length from the entry
        if character < 8:
            messagebox.showwarning("Warning", "Password must be above 8 characters!", icon="warning")
        else:
            passkey = "".join(sample(lis, character))
            label1.config(text=f"Your password: {passkey}",font=("Times New Roman", 25, "bold"),fg="lime",bg="black")  # Update label1 with the entry text
    except Exception as e:
        messagebox.showerror("ERROR", e)

def delete():
    entry.delete(0, END)
    label1.config(text="")  # Clear label1 when clearing the entry

window = Tk()


label3=Label(window,text="Password Length must be 8 characters",font=("Times New Roman", 15, "bold"),fg="lime",bg="black")
label3.grid(row=3, column=0, columnspan=2)

entry = Entry(window,fg="white",bg="black",font=(20))
entry.grid(row=6, column=0, columnspan=2)  # Centered

# Positioning buttons below the entry
button = Button(window, text="Submit", command=display,fg="lime",bg="black",activebackground="black",activeforeground="lime")
button1 = Button(window, text="Clear", command=delete,fg="lime",bg="black",activebackground="black",activeforeground="lime")
button.grid(row=7, column=0, padx=5)  # Centered
button1.grid(row=7, column=1, padx=5)  # Centered

label1 = Label(window, text="", font=("Ariel", 25,))
label1.grid(row=10, column=0, columnspan=2)  # Centered

window.geometry("480x480")
window.config(background="black")
window.title("Password Generator")

window.mainloop()

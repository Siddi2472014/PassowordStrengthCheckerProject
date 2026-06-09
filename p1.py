from tkinter import *
window= Tk()
window.title("Password Strength Checker")
window.geometry("400x400")
#Assigning what colour to display depending on length of the password, through one function
def check_password_strength():
    password = entry.get()
    if len(password) <=5:
        strength_label.config(text="Weak",fg="red")
    elif 6<=len(password) <=8:
        strength_label.config(text="Medium",fg="yellow")
    elif 9<=len(password) <=12:
        strength_label.config(text="Strong",fg="light green")
    else:
        strength_label.config(text="Very Strong",fg="dark green")
#Making the password entered display only '*' for every character entered as password
entry = Entry(window, show="*")
entry.pack(pady=10)
#the check button, linked to the function, 'check_password_strength', using the command parameter
check_button=Button(window,text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)
#label that displays the strength of the password
strength_label=Label(window,text="")
strength_label.pack(pady=10)
window.mainloop()
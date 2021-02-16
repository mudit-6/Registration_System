import tkinter as tk
from tkinter import messagebox
import csv

# Reove spaces from string
def removeSpace(string):
    return string.replace(" ", "")

# Show frames
def showFrame(frame):
    frame.tkraise()

# Reister new user
def successul_register():
    # input field should be not null
    if(namevar.get() != "" and password_var.get() != "" and confirm_pass_var.get() != ""):
        # Get username
        user_name = removeSpace(namevar.get())
        # Get Password
        user_password = removeSpace(password_var.get())
        # Get confirm password
        user_confirm_pass = removeSpace(confirm_pass_var.get())

        if(user_password == user_confirm_pass):  
            # Create a file
            f = open("userData.csv", "at")
            # Store data in file
            f.write(f"{user_name},{user_password}\r")
            f.close()
            # show message
            messagebox.showinfo(message = "Successfully Registered")
            # Reset all inputs area
            namevar.set("")   
            password_var.set("")   
            confirm_pass_var.set("") 
            alert_lbl.config(text = "")
        else:
            # Password and confirm password not same
            alert_lbl.config(text = "*Passwords are not same")
    else:
        # Not all input box fill
        alert_lbl.config(text = "*Please fill all above fields")

# Sign in user
def signIn():
    if(namevar_1.get() != "" and password_var_1.get() != ""):
        # Open a "userData.csv" file
        f = open("userData.csv", "rt")
        # Read data of file
        fetch_datas = csv.reader(f)
        # Check variables for password and user name
        check_pawrd = 1
        check_user = 1
        for data in fetch_datas: # ['Mudit',4444] ['pawan',7777]
            if(data[0] == removeSpace(namevar_1.get())):
                check_user = 0
                if(data[1] == removeSpace(password_var_1.get())):
                    # show message
                    messagebox.showinfo(message = "Login successfull :)")
                    check_pawrd = 0
                    namevar_1.set("")
                    password_var_1.set("")
                    alert_lbl1.config(text = "")
                    break  
        f.close()
        if(check_user == 1):
            alert_lbl1.config(text = "*User name not found")
        elif(check_pawrd == 1):
            alert_lbl1.config(text = "*Password incorrect")
    else:
        # Not all input box fill
        alert_lbl1.config(text = "*Please fill all above fields")
# Setup tkinter
root = tk.Tk()
root.geometry("810x571")

# Sign up window
sign_up_window = tk.Frame(root)
sign_up_window.grid(row =0, stick = tk.NSEW)

# Top bar
top_bar = tk.Frame(sign_up_window, borderwidth = 2, relief = tk.SOLID, bg = "red")
top_bar.grid(row = 0)

# App name
app_name = tk.Label(top_bar, text = "Cool.io")
app_name.grid(row = 0, column = 0, padx = (15,599), pady = (15,0))

# Sign in  button
sign_in = tk.Button(top_bar, text = "Sign in", command = lambda: showFrame(sign_in_window))
sign_in.grid(row = 0, column = 1, padx = (0,22), pady = (15,0))

# Sign up button
sign_up = tk.Button(top_bar, text = "Sign up")
sign_up.grid(row = 0, column = 2, padx = (0,15), pady = (15,0))

# Square box
square_box = tk.Frame(sign_up_window, width = 500, height = 300, borderwidth = 2, relief = tk.SOLID, bg = "red")
square_box.grid(row = 1, pady = (100,30))
square_box.grid_propagate(0)

# Heading
heading = tk.Label(square_box, text = "Sign up")
heading.grid(row = 0, column = 0, pady = (20,20))

# Name
name = tk.Label(square_box, text = "Name")
name.grid(row = 1, column = 0, stick = tk.NW, padx = (100,100), pady = (10,10))

# Name Input
namevar = tk.StringVar()
name_input =  tk.Entry(square_box, textvariable = namevar, width = 50)
name_input.grid(row = 2 , column = 0, padx = (100,100))

# Set Password
set_pasword = tk.Label(square_box, text = "Set Password")
set_pasword.grid(row = 3, column = 0, stick = tk.NW, padx = (100,100), pady = (10,10))

# Password Input
password_var = tk.StringVar()
password_input =  tk.Entry(square_box, textvariable = password_var, width = 50)
password_input.grid(row = 4 , column = 0, padx = (100,100))

# Confirm password
confirm_password = tk.Label(square_box, text = "Confirm Password")
confirm_password.grid(row = 5, column = 0, stick = tk.NW, padx = (100,100), pady = (10,10)) 

# Confirm Password Input
confirm_pass_var = tk.StringVar()
confirm_password_input =  tk.Entry(square_box, textvariable = confirm_pass_var, width = 50)
confirm_password_input.grid(row = 6 , column = 0, padx = (100,100))

# Register
register = tk.Button(square_box, text = "Sign up", width = 42, command = successul_register)
register.grid(row = 7, column = 0, pady = (10,10))

# Alert Label
alert_lbl = tk.Label(sign_up_window)
alert_lbl.grid(row = 2, column = 0)

###################################################################################################

# Sign in window
sign_in_window = tk.Frame(root)
sign_in_window.grid(row = 0, stick = tk.NSEW)

# Top bar
top_bar = tk.Frame(sign_in_window, borderwidth = 2, relief = tk.SOLID, bg = "red")
top_bar.grid(row = 0)

# App name
app_name = tk.Label(top_bar, text = "Cool.io")
app_name.grid(row = 0, column = 0, padx = (15,599), pady = (15,0))

# Sign in  button
sign_in = tk.Button(top_bar, text = "Sign in")
sign_in.grid(row = 0, column = 1, padx = (0,22), pady = (15,0))

# Sign up button
sign_up = tk.Button(top_bar, text = "Sign up", command = lambda: showFrame(sign_up_window))
sign_up.grid(row = 0, column = 2, padx = (0,15), pady = (15,0))

# Square box
square_box = tk.Frame(sign_in_window, width = 500, height = 300, borderwidth = 2, relief = tk.SOLID, bg = "red")
square_box.grid(row = 1, pady = (100, 30))
square_box.grid_propagate(0)

# Heading
heading = tk.Label(square_box, text = "Sign in")
heading.grid(row = 0, column = 0, pady = (20,20))

# Name
name = tk.Label(square_box, text = "Name")
name.grid(row = 1, column = 0, stick = tk.NW, padx = (100,100), pady = (10,10))

# Name Input
namevar_1 = tk.StringVar()
name_input =  tk.Entry(square_box, textvariable = namevar_1, width = 50)
name_input.grid(row = 2 , column = 0, padx = (100,100))

# Password
pasword = tk.Label(square_box, text = "Password")
pasword.grid(row = 3, column = 0, stick = tk.NW, padx = (100,100), pady = (10,10))

# Password Input
password_var_1 = tk.StringVar()
password_input =  tk.Entry(square_box, textvariable = password_var_1, width = 50)
password_input.grid(row = 4 , column = 0, padx = (100,100))

# Register
register = tk.Button(square_box, text = "Sign in", width = 42, command = signIn)
register.grid(row = 7, column = 0, pady = (30,30))

# Alert Label
alert_lbl1 = tk.Label(sign_in_window)
alert_lbl1.grid(row = 2, column = 0)

###########################################
showFrame(sign_up_window)
root.mainloop()
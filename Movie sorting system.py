from tkinter import *
from functools import partial

def validateregister(email, username, password):
    email_val = email.get()
    username_val = username.get()
    password_val = password.get()

    if not email_val or not username_val or not password_val:
        # If any field is empty, show "Register Failed" message
        register_failed_window = Toplevel()
        register_failed_window.geometry('300x100')
        register_failed_window.title('Register Failed')

        register_failed_label = Label(register_failed_window, text='Registration failed. Please fill in all fields.')
        register_failed_label.pack()
    else:
        # Create a new window for successful registration message
        success_window = Toplevel()
        success_window.geometry('300x100')
        success_window.title('Success')

        success_label = Label(success_window, text='Registration successful!')
        success_label.pack()

def validatelogin(email, password):
    email_val = email.get()
    password_val = password.get()

    # Assuming some predefined email and password for demonstration purposes
    predefined_email = "School@gmail.com"
    predefined_password = "school123"

    if email_val == predefined_email and password_val == predefined_password:
        # If the email and password match the predefined values, show "Login Successful" message
        login_success_window = Toplevel()
        login_success_window.geometry('300x100')
        login_success_window.title('Login Successful')

        login_success_label = Label(login_success_window, text='Login successful!')
        login_success_label.pack()
    else:
        # If the email and password do not match the predefined values, show "Login Failed" message
        login_failed_window = Toplevel()
        login_failed_window.geometry('300x100')
        login_failed_window.title('Login Failed')

        login_failed_label = Label(login_failed_window, text='Login failed. Invalid email or password.')
        login_failed_label.pack()

def login_screen():
    login_window = Toplevel()
    login_window.geometry('500x300')
    login_window.title('Login')

    # email label and text entry box for login
    emailLabel = Label(login_window, text="Email")
    emailLabel.place(x=100, y=50)
    email = StringVar()
    emailEntry = Entry(login_window, textvariable=email)
    emailEntry.place(x=150, y=50)

    # password label and password entry box for login
    passwordLabel = Label(login_window, text="Password")
    passwordLabel.place(x=90, y=80)
    password = StringVar()
    passwordEntry = Entry(login_window, textvariable=password, show='*')
    passwordEntry.place(x=150, y=80)

    # login button
    loginButton = Button(login_window, text="Login", command=partial(validatelogin, email, password))
    loginButton.place(x=180, y=120)

# window
tkWindow = Tk()
tkWindow.geometry('700x500')

# email label and text entry box
emailLabel = Label(tkWindow, text="Email")
emailLabel.place(x=270, y=160)
email = StringVar()
emailEntry = Entry(tkWindow, textvariable=email)
emailEntry.place(x=320, y=160)

# username label and text entry box
usernameLabel = Label(tkWindow, text="Username")
usernameLabel.place(x=250, y=180)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)
usernameEntry.place(x=320, y=180)

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password")
passwordLabel.place(x=250, y=200)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*')
passwordEntry.place(x=320, y=200)

# register button
registerButton = Button(tkWindow, text="Register", command=partial(validateregister, email, username, password))
registerButton.place(x=320, y=240)

# login button
loginButton = Button(tkWindow, text="Login", command=login_screen)
loginButton.place(x=325, y=280)

tkWindow.mainloop()


  
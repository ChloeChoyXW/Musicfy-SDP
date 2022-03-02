import tkinter as tk
import re
from tkinter import Toplevel, messagebox
from py_SQL import db_connection

db, mycursor = db_connection()


# ===================================== Main =============================================

def raise_frame(frame):
    frame.tkraise()


root = tk.Tk()
root.geometry("500x500")
root.title("Musicfy")
# root.iconbitmap(r"musicfy.ico") # musicfy window icon


main = tk.Frame(root)
signup = tk.Frame(root)

for frame in (main, signup):
    # frame.grid(row=0, column=0, sticky="news")
    frame.place(x=0, y=0, width=500, height=500)

# main page with musicfy logo
mainlabel = tk.Label(main, text='Musicfy Logo')
mainlabel.pack()




# ===================================== User Main =======================================
def user(username):
    root.withdraw()
    top = Toplevel()
    top.geometry("500x500")
    top.title("User Page")

    print(username)

    tk.Label(top, text="Welcome, " +username).grid(row=1, column=7) 


    user_profile_button = tk.Button(top, text="Profile")
    user_profile_button.grid(row=1, column=9)


    user_quit_button = tk.Button(top, text="Quit", command=lambda: quit(top))
    user_quit_button.grid(row=1, column=10)




# ===================================== Admin Main =====================================
def admin(username):
    root.withdraw()
    top = Toplevel()
    top.geometry("500x500")
    top.title("Admin Page")

    print(username)

    tk.Label(top, text="Welcome, " +username).grid(row=1, column=7) 


    user_profile_button = tk.Button(top, text="Profile")
    user_profile_button.grid(row=1, column=9)

    quit_button = tk.Button(top, text="Quit", command=lambda: quit(top))
    quit_button.grid(row=1, column=10)


def quit(top):

    # destroy user / admin window 
    top.destroy()
    root.update()

    # unminimize window
    root.deiconify()
   



# ===================================== Login =========================================

def login_verify():
    username = username_verify.get()
    password = password_verify.get()

    sql = "SELECT * FROM user_tbl WHERE username = %s and password = %s"
    mycursor.execute(sql, [username, password])
    results = mycursor.fetchall()

    print(results)

    # checks whether usertype "listener" is in list
    if 'listener' in results[0]:
        messagebox.showinfo("Musicfy", "User Login Successfull!")
        loguser_entry.delete(0, tk.END)
        logpass_entry.delete(0, tk.END)
        root.withdraw()
        user(username)

    # checks whether usertype "artist" is in list 
    elif 'artist' in results[0]:
        messagebox.showinfo("Musicfy", "User Login Successfull!")
        loguser_entry.delete(0, tk.END)
        logpass_entry.delete(0, tk.END)
        root.withdraw()
        user(username)

    # checks whether usertype "admin" is in list
    elif 'admin' in results[0]:
        messagebox.showinfo("Musicfy", "Admin Login Successfull!")
        loguser_entry.delete(0, tk.END)
        logpass_entry.delete(0, tk.END)
        root.withdraw()
        admin(username)

    # checks whether user status is banned
    elif 'banned' in results[0]:
        messagebox.showinfo("Musicfy", "Your account is banned!")
        loguser_entry.delete(0, tk.END)
        logpass_entry.delete(0, tk.END)

    else:
        messagebox.showinfo("Error", "Incorrect Username or Password!")
        loguser_entry.delete(0, tk.END)
        logpass_entry.delete(0, tk.END)


username_verify = tk.StringVar()
password_verify = tk.StringVar()

# login form code
# username input code
loguser_label = tk.Label(main, text="Username: ", fg="black", font=("Calibri", 12, "bold"))
loguser_label.pack()
# username entry
loguser_entry = tk.Entry(main, textvariable=username_verify)
loguser_entry.pack()
loguser_label1 = tk.Label(main, text="")
loguser_label1.pack()

# password input code
logpass_label = tk.Label(main, text="Password: ", fg="black", font=("Calibri", 12, "bold"))
logpass_label.pack()
# password entry
logpass_entry = tk.Entry(main, textvariable=password_verify, show="*")
logpass_entry.pack()
logpass_label1 = tk.Label(main, text="")
logpass_label1.pack()

# login button in main frame
loginbutton = tk.Button(main, text="Login", command= login_verify)
loginbutton.pack()

# sign up button in main frame
mainbutton = tk.Button(main, text="Sign Up", command=lambda: raise_frame(signup))
mainbutton.pack()




# ===================================== Sign Up =====================================

def reg_verify():
    usern = reg_username.get()
    passw = reg_password.get()
    checkuser = "SELECT username FROM user_tbl WHERE username = %s"
    mycursor.execute(checkuser, (usern, ))
    userexists = mycursor.fetchone()

    valid = 0 
    check_symbol= re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    while True:
        # validate whether the username exists in the database or not
        # checks if the input field is empty or not
        if usern == "" or passw == "":
            messagebox.showinfo("Error", "Username and Password are Required!")
            break

        elif userexists:
            messagebox.showinfo("Error", "Username Already Exists!")
            reguser_entry.delete(0, tk.END)
            regpass_entry.delete(0, tk.END)
            break

        # checks the len of username & password input whether it exceed 10 characters
        elif len(usern) > 10:
            valid = -1
            reguser_entry.delete(0, tk.END)
            break

        # checks the username & password input whether it contains special characters
        elif check_symbol.search(usern):
            valid = -1
            reguser_entry.delete(0, tk.END)
            break

        elif (len(passw) > 10):
            valid = -2
            regpass_entry.delete(0, tk.END)
            break

        elif check_symbol.search(passw):
            valid = -2
            regpass_entry.delete(0, tk.END)
            break

        # username and password contained space, will be removed (with replace function)
        elif usern.replace(" ", ""):
            valid = -3
            reguser_entry.delete(0, tk.END)

        elif passw.replace(" ", ""):
            valid = -3
            regpass_entry.delete(0, tk.END)
            break

        # if all input required fields are correctly identified, data will be inserted into the database
        else:
            valid = 0
            reg_sql = "INSERT INTO user_tbl (usertype, username, password) VALUES (%s, %s, %s)"
            reg_val = ("listener", usern, passw)
            mycursor.execute(reg_sql, reg_val)
            db.commit()
            messagebox.showinfo("Information", "Registration Successfull!")

            reg_username.set("")
            reg_password.set("")

            # clears the input box empty after a successful registration process
            reguser_entry.delete(0, tk.END)
            regpass_entry.delete(0, tk.END)

    # 
    if valid == -1:
        messagebox.showinfo("Error", "Username should not contain special characters or exceed 10 characters")

    elif valid == -2:
        messagebox.showinfo("Error", "Password should not contain special characters or exceed 10 characters")

    elif valid == -3:
        messagebox.showinfo("Error", "Spacing in username and password is allowed!")


# sign up section in signup frame
# signup button, navigate to signup frame
signuplabel = tk.Label(signup, text="Sign Up")
signuplabel.pack()

reg_username = tk.StringVar()
reg_password = tk.StringVar()

# username label
reguser_label = tk.Label(signup, text="Username: *", font=("Calibri", 12, "bold"))
reguser_label.pack()
# username entry
reguser_entry = tk.Entry(signup, textvariable=reg_username)
reguser_entry.pack()

# password label
regpass_label = tk.Label(signup, text="Password: *", font=("Calibri", 12, "bold"))
regpass_label.pack()
# password entry
regpass_entry = tk.Entry(signup, textvariable=reg_password, show="*")
regpass_entry.pack()
regpass_label1 = tk.Label(signup, text="")
regpass_label1.pack()

# optional (artist / listener)
###
# optional (select artist / listener in profile section)
###

# button for signup
signupbutton = tk.Button(signup, text="Confirm", command=reg_verify)
signupbutton.pack()

# button for signup frame to go back to the main frame
signupbuttonb = tk.Button(signup, text="Main", command=lambda: raise_frame(main))
signupbuttonb.pack()

# run gui application window
raise_frame(main)
root.mainloop()
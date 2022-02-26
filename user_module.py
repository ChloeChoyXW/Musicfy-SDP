# ===================================== User Main =====================================
import tkinter as tk
from py_SQL import db_connection

# database connection 
db, cursor = db_connection()

# put username here to test the user function
# username = 'test'

def userprofile():
    # add your function here (for andrew)
    print()


def user(username):
    # root.withdraw()
    top = tk.Toplevel()
    top.geometry("500x500")
    top.title("User Page")

    tk.Label(top, text="Welcome, " +username).grid(row=1, column=7) 


    user_profile_button = tk.Button(top, text="Profile", command=lambda: userprofile)
    user_profile_button.grid(row=1, column=9)

    user_quit_button = tk.Button(top, text="Quit", command=lambda: quit(top))
    user_quit_button.grid(row=1, column=10)


    top.mainloop()
# user(username)
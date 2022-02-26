import tkinter as tk
from tkinter import Listbox, messagebox

from py_SQL import db_connection
from user_module import user

db, mycursor = db_connection()

root = tk.Tk()
root.title("window")
root.geometry("350x350")

def update(data):

    # delete all records in listbox
    list.delete(0, tk.END)

    # updates listbox
    for row in data:
        # showdata = str(row[0])+ '  |  ' +row[1]
        list.insert(list.size()+1, row)


    # for item in data:
    # list.insert(tk.END, data)

def check(e):

    user_input = userEntry.get()

    myquery = "SELECT uid, username FROM user_tbl"
    mycursor.execute(myquery)
    ui_result = mycursor.fetchall()

    # if input field is empty, list of all user is displayed
    if user_input == '':
        showuser()
    else:
        # display users that contains any letter inputted from the search input
        data = []
        for item in ui_result:
            uidata = str(item[0])+ '  |  ' +item[1]
            if user_input in uidata:
                data.append(uidata)

    update(data)

# delete a user in user table 
def deleteuser():

    username_delete = userEntry.get()

    # if user input field is empty, display message 
    if username_delete == "":
        messagebox.showinfo("", "Input field is empty")
    
    # if user exist in database, query will execute and remove user
    else:
        deletequery = "DELETE FROM user_tbl WHERE username = '" + username_delete + "'"
        mycursor.execute(deletequery)

        db.commit()
        messagebox.showinfo("", "User has been removed")

        update()

# display all records in user table database
def showuser():

    showquery = "SELECT uid, username FROM user_tbl"
    mycursor.execute(showquery)
    sdresult = mycursor.fetchall()

    list.delete(0, tk.END)

    for row in sdresult:
        showdata = str(row[0])+ '  |  ' +row[1]
        list.insert(list.size()+1, showdata)


def searchuser():

    username_search = userEntry.get()

    searchquery = "SELECT uid, username FROM user_tbl WHERE username = '" + username_search + "'"
    mycursor.execute(searchquery)
    seresult = mycursor.fetchall()

    print(seresult)

    for item in seresult:
        shdata = str(item[0])+ '  |  ' +item[1]
        list.insert(list.size()+1, shdata)

    # data = []
    # for item in str(list):
    #     if username_search in item:
    #         data.append(list)

    update(shdata)


searchUser = tk.Label(root, text="Username: ")
searchUser.grid(row=2, column=5)

userEntry = tk.Entry(root)
userEntry.bind("<KeyRelease>", check)
userEntry.grid(row=2, column=6)

all_data = tk.Button(root, text="Show All Data", command = showuser)
all_data.grid(row=3, column=5)

search_button = tk.Button(root, text="Search", command = searchuser)
search_button.grid(row=3, column=6)

delete_button = tk.Button(root, text="Delete", command = deleteuser)
delete_button.grid(row=3, column=7)

list = Listbox(root)
list.grid(row=4, column=5)


# searchuser()
showuser()
root.mainloop()
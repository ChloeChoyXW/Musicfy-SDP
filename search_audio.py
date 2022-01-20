import tkinter as tk
from py_SQL import db_connection

db, mycursor = db_connection()
root = tk.Tk()

# ============================= Application Design =============================
# Change Window(Application) Title
root.title("Musicfy")
# Change icon
root.iconbitmap(r"musicfy.ico")
# Change Window's size
root.geometry("400x400")
# Fix window's size
root.resizable(width=False, height=False)

# ------------------- Button to change application Size ------------------------
# def resize():
#     w = 400
#     h = 400
#     root.geometry(f"{w}x{h}") 

# resizeButton = tk.Button(root, text="Resize to 400 x 400", command = resize)
# resizeButton.grid(row=2, column=2)
# ------------------------------------------------------------------------------


# ==============================================================================



# Creating label for search bar
searchLabel = tk.Label(root, text = "Search Audio: ")
# Creating input bar
searchBar = tk.Entry(root)

# Display Search bar
searchLabel.grid(row = 0, column = 0)
searchBar.grid(row = 0, column = 1)

# Collect input data
def collect_search_data():
    u_search = searchBar.get()
    print(u_search)
    print("abd")

showButton = tk.Button(root, text = "Show", command = "collect_seach_data")

# Display button
showButton.grid(row = 1, column = 0)







root.mainloop()
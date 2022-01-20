import tkinter as tk
import pygame as pg

root = tk.Tk()

# ============================= Application Design =============================
# Change Window(Application) Title
root.title("Musicfy")
# Change icon
root.iconbitmap(r"music.ico")
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

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mysql#Pa55",
    database = "musicfy_db"
)

mycursor = db.cursor()

audioQuery = mycursor.execute("select * from audio_tbl")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)



root.mainloop()
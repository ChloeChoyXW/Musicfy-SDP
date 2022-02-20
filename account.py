# ssssssss
import tkinter as tk
from tkinter.ttk import Label
import pygame as pg
from email import message
from tkinter import Image, PhotoImage, messagebox
from PIL import ImageTk, Image
# PIL is to allow to save and display other image file formats cus rn only png works


# Import Local Module
from py_SQL import db_connection

# Connect Database
db, mycursor = db_connection()

# Initialise tkinter
root = tk.Tk()

# initialise pygame mixer
pg.mixer.init()

# ============================= fetching data from database  =====================================


# ============================= Application  =====================================
# Change Window(Application) Title
root.title("Musicfy")
# # Change icon
# root.iconbitmap(r"musicfy.ico")
# Change Window's size
root.geometry("500x500")
# Fix window's size
root.resizable(width=False, height=False)
root.title('User Profile')

#display user profile and alignment
welcome = Label(root, text="User Profile")
welcome.pack(side=tk.TOP, anchor="nw")

#resizing image and position on application
image = Image.open("C:\\Users\\USER\\Desktop\\admin.jpg")#need to research how to retrieve the login data and display the image from there
resize = image.resize((150,100))
finalimage = ImageTk.PhotoImage(resize)
profile_image=Label(image=finalimage)
profile_image.pack(side=tk.TOP, anchor="nw")


#display user data here by retrieving it from database
user_info = Label(root, text="Welcome, User")
user_info.pack(side=tk.TOP, anchor="nw")

root.mainloop()
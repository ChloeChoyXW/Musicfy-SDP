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

#display image
mylabel = Label(root, text="bye world!")
mylabel.pack()
photo = PhotoImage(file="C:\\Users\\USER\\Desktop\\kanna3.png")
labeling = Label(root, image=photo)
labeling.pack()

# converting jpg images so it will appear in in the application
img = ImageTk.PhotoImage(Image.open("xyz.jpg"))  
l=Label(image=img)
l.pack()
root.mainloop()
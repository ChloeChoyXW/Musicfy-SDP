import os
import tkinter as tk
import pygame as pg
from tkinter import StringVar, filedialog, messagebox
from pathlib import Path
from py_SQL import db_connection
import shutil

db, mycursor = db_connection()
root = tk.Tk()

# initialise pygame mixer
pg.mixer.init()

# ============================= Application Design =============================
# Change Window(Application) Title
root.title("Musicfy")
# Change icon
root.iconbitmap(r"musicfy.ico")
# Change Window's size
root.geometry("400x400")
# Fix window's size
root.resizable(width=False, height=False)

# ==============================================================================

# ============================ Functions =======================================
#Show selected filename


#Select audio file
def Select_file():
    global file_path 
    file_name = StringVar()
    #Get file path
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", ".mp3 .wav .flac")])
    #Get file name
    file_name = Path(file_path).name
    file_selected = tk.Label(root, text = file_name, font=('Italic', 10), fg="black", )
    file_selected.grid(sticky='W',row=2,column=2)

#Get menu choice
def get_category():
    global audio_category
    audio_category = []
    #Get selected category
    categoryList = category_list.curselection()
    for c in categoryList:
        c+=1
        audio_category.append(c)

#Upload file
def Upload():
    #Audio name
    global audio_name
    #uid = str(getuserid)
    audio_name = inputName.get() + "_" #+ uid
    #Copy audio to the file (If able to host databse, change to upload to database)
    audio_uploaded = shutil.copy(file_path, 'C:/Users/USER/OneDrive/Documents/GitHub/Musicfy-SDP/audio_files folder/') #change to audio file path
    #rename file to match audio name and aid
    audio_location = 'C:/Users/USER/OneDrive/Documents/GitHub/Musicfy-SDP/audio_files folder/' + audio_name  + '_'+'1'+'.mp3'
    os.rename(audio_uploaded, audio_location) #Rename audio in audio folder as name entered
    
    audio_sql = "INSERT INTO audio_tbl (audio_name, uid, audio_path) VALUES ('{}','{}','{}')".format(audio_name, '1', audio_location)
    
    try:
        mycursor.execute(audio_sql)
        updateAudio_category()
        db.commit()
        messagebox.showinfo('', 'Audio uploaded successfully!')

    except Exception as e:
        messagebox.showerror("Error",  e)
        db.rollback()

    finally:
        if (db):
            mycursor.close()
            db.close()

#Update audio category
def updateAudio_category():
    #Get aid
    audio_id = "SELECT aid FROM audio_tbl WHERE audio_name = %s AND uid = %s "
    audio_tuple = (audio_name, 2)
    # try:
    audioCategory_list = []
    mycursor.execute(audio_id, audio_tuple)
    aid_tuple = mycursor.fetchone()
    
    aid = aid_tuple[0]

    #Get a list of cid with aid
    for x in audio_category:
        audioCategory_list.append((x, aid))


    #Insert list into database
    audio_cat = "INSERT INTO song_in_category (cid, aid) VALUES (%s, %s)"
    mycursor.executemany(audio_cat, audioCategory_list)

#============================================================================

#Create and display upload audio label
uploadAudio = tk.Label(root, text = "Upload Audio", font=('Italic', 14), fg="dark blue")
uploadAudio.grid(row = 0, column = 0)

#Create and display audio name input bar
audioName = tk.Label(root, text = "Audio Name:", font=('Italic', 10), fg="black", )
audioName.grid(sticky='W',row=1,column=0)
inputName = tk.Entry(root)
inputName.grid(row=1,column=1)

#Select audio file label and button
audioFile = tk.Label(root, text = "Select audio file:", font=('Italic', 10), fg="black", )
audioFile.grid(sticky='W',row=2,column=0)

Open_button = tk.Button(root, text='Open', command= Select_file)
Open_button.grid(sticky='W', row=2,column=1)

# Category label
Category = tk.Label(root, text = "Category:", font=('Italic', 10), fg="black", )
Category.grid(sticky='NW',row=3,column=0)

#Create listbox
category_list = tk.Listbox(root, selectmode=tk.MULTIPLE, height=6)
categories = ['Lofi', 'Hit-hop', 'Jazz', 'Meme', 'Game OST', 'Acoustic']
for i in categories:
    category_list.insert(tk.END, i)
    
category_list.grid(row=4, column=1)

#Upload button
Upload_button = tk.Button(root, text='Upload', command=lambda:[get_category(), Upload()])
Upload_button.grid(sticky='W', row=5,column=0)

root.mainloop()

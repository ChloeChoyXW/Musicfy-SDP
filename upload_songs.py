from multiprocessing import connection
import tkinter as tk
import pygame as pg
from tkinter import filedialog
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
#Select audio file
def Select_file():
    global file_path 
    file_path = filedialog.askopenfilename()
    

#Get menu choice
def get_category(self):
    global selected 
    selected = variable.get()

#Upload file
def Upload():
    #Audio name
    audio_name = inputName.get()

    #Copy audio to the file (If able to host databse, change to upload to database)
    shutil.copy(file_path, r'C:/Users/USER/OneDrive/Documents/GitHub/Musicfy-SDP/audio_files folder') #change to audio file path
    audio_location = 'C:/Users/USER/OneDrive/Documents/GitHub/Musicfy-SDP/audio_files folder/' + audio_name
    sql = """INSERT INTO audio_tbl (audio_name, uid, audio_path) VALUES ('{}','{}','{}')""".format(audio_name, '1', audio_location)

    try:
        mycursor.execute(sql)
        db.commit()
        print("Audio uploaded successfully!")

    except Exception as e:
        print("Error: ", e)

    finally:
        if (db):
            mycursor.close()
            db.close()

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

Open_button = tk.Button(root, text='Open', command=Select_file)
Open_button.grid(sticky='W', row=2,column=1)

# ====================== Category label and menu ======================
Category = tk.Label(root, text = "Category:", font=('Italic', 10), fg="black", )
Category.grid(sticky='W',row=3,column=0)

categories = ['Lofi', 'Hit-hop', 'Jazz', 'Meme', 'Game OST', 'Acoustic']

#set variables
variable = tk.StringVar()
variable.set('Select')

#Create menu
menu = tk.OptionMenu(root, variable, *categories, command=get_category)
menu.grid(sticky='W', row=3,column=1)
# ====================================================================

#Upload button
Upload_button = tk.Button(root, text='Upload', command=Upload)
Upload_button.grid(sticky='W', row=4,column=0)



root.mainloop()

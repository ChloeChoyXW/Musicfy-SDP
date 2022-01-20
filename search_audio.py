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
searchLabel = tk.Label(root, text = "Search Audio: ", font = ('Italic', 14), fg="dark blue")
# Creating input bar
searchBar = tk.Entry(root)

# Display Search bar
searchLabel.grid(row = 0, column = 0)
searchBar.grid(row = 0, column = 1)

# Collect input data & Search
def search_data():
    u_search = searchBar.get()
    audio_num = 0

    # Delete search result label After next search, Failed (Search long then short to test)
    # searchValid = tk.Label(root, text = f"")
    # print(searchValid.winfo_exists())
    # if searchValid.winfo_exists() == 1:
    #     searchValid.destroy()

    # Check the length of search
    if len(u_search) >= 31 or u_search =='':
        u_search = ''
        searchValid = tk.Label(root, text = f"Invalid Search")
        searchValid.grid(row=2,column=1)
    else:
        searchValid = tk.Label(root, text = f"Displaying Search Result for: {u_search}")
        searchValid.grid(row=2,column=1)
        
        print(u_search) # -- FOR LOG --

        # Search in Database
        
        searchAudioQuery ="select audio_name, audio_path from audio_tbl where audio_name like" + "'%" + u_search + "%';" 
        mycursor.execute(searchAudioQuery)
        myresult = mycursor.fetchall()

        audioLabel = tk.Label(root, text = f"Number of Result {audio_num}")
        audioLabel.grid(row=3, column=0)

        for x in myresult:
            print(x) # -- FOR LOG --
            a_name = x[0] # Potato code because it will wait until it load all songs (maybe limit/ use pages)
            a_path = x[1]
            audio_num += 1
            # print(a_name) # -- FOR LOG --
            # print(a_path) # -- FOR LOG --


            # Display Audio


            audioButton = tk.Button(root, text = "This song")
            audioButton.grid(row=3, column=1)





# Search Button
searchButton = tk.Button(root, text = "Search", command = search_data)
# Display search button
searchButton.grid(row = 1, column = 0)




root.mainloop()
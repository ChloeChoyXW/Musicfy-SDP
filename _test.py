from tkinter import *



root = Tk()

# ==========================Display Text and Create Window========================================================
# Creating a label Widget
label_1 = Label(root, text = "Hello World")
label_2 = Label(root, text = "This is second label")

# # Display on screen [On the middle]
# label_1.pack()

# Display with Grid ** 'grid' are relative to each other, to create distance, create a blank label as standard
label_1.grid(row = 0, column = 0)
label_2.grid(row = 1, column = 0)

# # Another way to display with grid
# label_3 = Label(root, text = "This is third label")

# ==========================Buttons========================================================


# Constant Loop
root.mainloop()